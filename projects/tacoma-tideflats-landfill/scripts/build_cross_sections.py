# -*- coding: utf-8 -*-
# NOTE: Extracted and normalized from Landfill Master Document.docx.
# Archive status: final canonical version. Review configuration before execution.
# Public-safe copy: internal emails, user paths, and organization-specific locations were removed.

"""
XSEC_Build_CrossSection.py  (multi-section version)
===================================================
ONE-SHOT landfill cross-section builder for ArcGIS Pro.

Builds ALL your cross-sections (XS_A ... XS_E) in a single run, one map per
section, from one line feature class that holds all five lines. Run this
whole file in a single ArcGIS Pro notebook cell inside your project.

WHAT IT BUILDS PER SECTION (fixed names, overwritten each run)
--------------------------------------------------------------
  <SEC>_Surface_Line     flat topography line across full section length
  <SEC>_Points           BOTH point sets projected to the section
                           SOURCE = 'CONTAM' or 'TCP'; CATEGORY for symbology
  <SEC>_Depth_Sticks     thin vertical line, ground -> total depth
  <SEC>_Interval_Bands   boxes at documented depth intervals, centered on
                           the stick (single-depth results = 0.5 ft bands)
  <SEC>_Leader_Lines     leader lines (only if LABEL_STYLE = "LEADER")
  <SEC>_Label_Anchors    invisible points carrying the ID labels
                           LABEL_ROLE = 'DEPTH_ID', 'PLAIN_ID' or 'TCP_ID'
  <SEC>_Grid             light background grid (station + depth)
  <SEC>_Axes             bottom (length) + left (depth) axis lines
  <SEC>_Axis_Labels      tick value labels + axis titles

CROSS-SECTION SPACE
-------------------
  X = station along the section line, FEET, 0 at the line's start vertex
  Y = 0 at ground surface (flat site), negative below, times VE
  Depth axis labels show positive "ft bgs" values regardless of VE.

HOW TO RUN
----------
  1. Edit SETTINGS (layer names, SECTION_NAME_FIELD, label style).
  2. New notebook cell -> paste everything -> run.
  3. One map per section appears/updates: XSEC_XS_A, XSEC_XS_B, ...

METHANE (later)
---------------
  add_overlay_bands("XS_A", "MethaneTable", "REPORT_ID",
                    "TOP_FT", "BOT_FT", "CH4_PCT")
  draws value-attributed boxes beside the sticks of that section; symbolize
  with graduated colors on VALUE to get a binned legend like your PCB figure.
"""

import os
import re
import traceback
import arcpy

# =============================================================================
# SETTINGS  -- edit these to match your project
# =============================================================================

# --- INPUT LAYERS (display names as they appear in ANY map in the project) ---
# One line feature class holding ALL section lines (XS_A ... XS_E).
SECTION_LINE_LAYER = "CrossSectionLines"

# Field on that layer naming each section. First existing candidate wins.
SECTION_NAME_FIELD = ["XSEC", "Name", "SECTION", "SectionID", "Label"]

# Only build these sections; [] or None = build every line found.
SECTIONS_TO_BUILD = []            # e.g. ["XS_A", "XS_C"]

# Contamination points (POT landfill points incl. joined depth columns).
CONTAM_POINTS_LAYER = "ContaminationPoints2"

# TCP / Ecology cleanup-site points.
TCP_POINTS_LAYER = "TCP_CleanupSites"

# Maps are named MAP_PREFIX + section name, e.g. "XSEC_XS_A".
MAP_PREFIX = "XSEC_"

# --- FIELD NAME CANDIDATES (first match wins; aliases also checked) ----------
FLD_REPORT_ID   = ["REPORT_ID", "ReportID", "Report_ID"]
FLD_CATEGORY    = ["LOCATION_STATUS", "Landfill___Soil_Observation_Category",
                   "Landfill_Soil_Observation_Cate", "Category",
                   "Landfill / Soil Observation Category"]
FLD_DEPTH_NUM   = ["TOTAL_DEPTH_FT", "Depth_DEPTH", "Total_Depth_Ft"]
FLD_DEPTH_TEXT  = ["Depth"]                       # "65 ft", "10.5-23.5 ft"
FLD_INT_TOP     = ["Depth_Original_Interval_Top_ft_bgs", "Depth_DEPTH_TOP",
                   "Interval_Top_ft"]
FLD_INT_BOT     = ["Depth_Original_Interval_Bottom_ft_bgs", "Depth_DEPTH",
                   "Interval_Bottom_ft"]
FLD_CONTAM_GRP  = ["Depth_Contaminant_Group", "Contaminant_Groups",
                   "Contaminant_Group", "Contaminant Groups"]
FLD_EXCEED      = ["Depth_Exceedance_Flag", "Exceedance_Flag"]
FLD_TCP_NAME    = ["Site_Name", "SiteName", "Site Name", "CleanupSiteId"]

# --- GEOMETRY / DISPLAY ------------------------------------------------------
BUFFER_FT               = 200.0  # max offset of a point from its section line
VERTICAL_EXAGGERATION   = 1.0    # 1:1; bump to 5.0 if the ribbon is too thin
GROUND_ELEV_FT          = 0.0    # flat site: surface drawn at Y = 0
POINT_BAND_THICKNESS_FT = 0.5    # single-depth result -> 0.5 ft display band
BLOCK_HALF_WIDTH_FT     = 5.0    # interval band half-width (10 ft wide box)
MIN_DISPLAY_DEPTH_FT    = 10.0
BOTTOM_PADDING_FT       = 5.0
MAX_REASONABLE_DEPTH_FT = 300.0  # sanity cap on parsed depths

HORIZONTAL_INTERVAL_FT  = 100.0  # vertical grid spacing (station)
DEPTH_INTERVAL_FT       = 5.0    # horizontal grid spacing (depth)

# "TOP"    = ID label floats at the top of each stick (like your reference
#            figure: LAD-10, B-05 ...). Recommended.
# "LEADER" = detached leader line from the dot to an offset label.
LABEL_STYLE = "TOP"

# Leader/label offsets in section feet; None = auto-scale to section length.
LEADER_START_DX = None
LEADER_START_DY = None
LEADER_END_DX   = None
LEADER_END_DY   = None
LABEL_GAP_DX    = None

SAVE_PROJECT = True

# Output workspace: None = project default geodatabase.
OUTPUT_GDB = None

OUT_SUFFIXES = {
    "surface":  "Surface_Line",
    "points":   "Points",
    "sticks":   "Depth_Sticks",
    "bands":    "Interval_Bands",
    "leaders":  "Leader_Lines",
    "anchors":  "Label_Anchors",
    "grid":     "Grid",
    "axes":     "Axes",
    "axlabels": "Axis_Labels",
}

# =============================================================================
# MESSAGE HELPER
# =============================================================================

def message(text, severity=0):
    text = str(text)
    if severity == 2:
        arcpy.AddError(text)
    elif severity == 1:
        arcpy.AddWarning(text)
    else:
        arcpy.AddMessage(text)
    print(text)


# =============================================================================
# GENERAL HELPERS
# =============================================================================

def clean_text(value):
    if value is None:
        return ""
    text = str(value).strip()
    if text.lower() in ("", "none", "null", "nan", "no data",
                        "not specified", "unknown"):
        return ""
    return text


def safe_name(text):
    return re.sub(r"[^A-Za-z0-9_]", "_", text.strip())


def find_map(project, map_name, create=False):
    maps = project.listMaps(map_name)
    if maps:
        return maps[0]
    if create:
        message("Map '{}' not found - creating it.".format(map_name))
        return project.createMap(map_name)
    raise ValueError("No map named '{}' was found.".format(map_name))


def find_layer_anywhere(project, layer_name):
    target = layer_name.strip().lower()
    for m in project.listMaps():
        for lyr in m.listLayers():
            if lyr.name.strip().lower() == target:
                return lyr
    raise ValueError(
        "No layer named '{}' was found in any map of this project."
        .format(layer_name))


def find_field(dataset, candidates, required=True):
    fields = arcpy.ListFields(dataset)
    for cand in candidates:
        for f in fields:
            if f.name.lower() == cand.lower():
                return f.name
    for cand in candidates:
        for f in fields:
            if (f.aliasName or "").lower() == cand.lower():
                return f.name
    if required:
        raise ValueError(
            "None of the fields {} exist in {}.".format(candidates, dataset))
    return None


_DEPTH_NUM_RE = re.compile(r"(\d+(?:\.\d+)?)")

def parse_depth_text(text):
    """'65 ft' -> (None, 65.0); '10.5-23.5 ft' -> (10.5, 23.5)."""
    text = clean_text(text)
    if not text:
        return None, None
    nums = [float(n) for n in _DEPTH_NUM_RE.findall(text)]
    nums = [n for n in nums if 0 < n <= MAX_REASONABLE_DEPTH_FT]
    if not nums:
        return None, None
    if len(nums) == 1:
        return None, nums[0]
    return min(nums), max(nums)


def as_float(value):
    try:
        v = float(value)
    except (TypeError, ValueError):
        return None
    if v <= 0 or v > MAX_REASONABLE_DEPTH_FT:
        return None
    return v


def recreate_fc(workspace, name, geom_type, fields):
    path = os.path.join(workspace, name)
    if arcpy.Exists(path):
        arcpy.management.Delete(path)
    arcpy.management.CreateFeatureclass(workspace, name, geom_type)
    for fname, ftype, flen in fields:
        if ftype == "TEXT":
            arcpy.management.AddField(path, fname, ftype,
                                      field_length=flen or 255)
        else:
            arcpy.management.AddField(path, fname, ftype)
    return path


# =============================================================================
# SECTION LINES + STATIONING
# =============================================================================

def get_section_lines(project):
    """Return [(section_name, geometry, sr, to_ft, length_ft), ...]"""
    lyr = find_layer_anywhere(project, SECTION_LINE_LAYER)
    name_field = find_field(lyr, SECTION_NAME_FIELD)
    wanted = {s.strip().lower() for s in (SECTIONS_TO_BUILD or [])}
    out = []
    with arcpy.da.SearchCursor(lyr, [name_field, "SHAPE@"]) as cur:
        for name, geom in cur:
            name = clean_text(name)
            if not name or geom is None:
                continue
            if wanted and name.lower() not in wanted:
                continue
            sr = geom.spatialReference
            if sr is None or sr.name in ("", "Unknown"):
                raise ValueError(
                    "Section line '{}' has no spatial reference.".format(name))
            if sr.linearUnitName and "foot" in sr.linearUnitName.lower():
                to_ft = 1.0
            else:
                to_ft = 1.0 / 0.3048
            out.append((name, geom, sr, to_ft, geom.length * to_ft))
    if not out:
        raise ValueError(
            "No section lines found in '{}' (field '{}', filter {}).".format(
                SECTION_LINE_LAYER, name_field, SECTIONS_TO_BUILD))
    message("Found {} section line(s): {}".format(
        len(out), ", ".join(n for n, *_ in out)))
    return out


def station_points(layer, line_geom, line_sr, to_ft, label_field,
                   extra_fields=None):
    """Points within BUFFER_FT of this section line, with station in ft."""
    extra_fields = extra_fields or {}
    fetch = ["SHAPE@", label_field] + [f for f in extra_fields.values() if f]
    results = []
    with arcpy.da.SearchCursor(layer, fetch) as cur:
        for row in cur:
            shp = row[0]
            if shp is None:
                continue
            pt = shp.projectAs(line_sr)
            try:
                _, dist_along, dist_from, right = \
                    line_geom.queryPointAndDistance(pt)
            except Exception:
                continue
            dist_from_ft = dist_from * to_ft
            if dist_from_ft > BUFFER_FT:
                continue
            attrs = {}
            idx = 2
            for key, fld in extra_fields.items():
                if fld:
                    attrs[key] = row[idx]
                    idx += 1
                else:
                    attrs[key] = None
            results.append({
                "label": clean_text(row[1]),
                "station_ft": dist_along * to_ft,
                "dist_ft": dist_from_ft * (1 if right else -1),
                "attrs": attrs,
            })
    return results


# =============================================================================
# PER-SECTION BUILD
# =============================================================================

def build_section(project, workspace, sec_name, line_geom, line_sr, to_ft,
                  length_ft, contam_lyr, tcp_lyr, flds):
    sec = safe_name(sec_name)
    message("-" * 70)
    message("SECTION {} ({:.0f} ft long)".format(sec_name, length_ft))
    xsec_map = find_map(project, MAP_PREFIX + sec, create=True)

    contam_rows = station_points(
        contam_lyr, line_geom, line_sr, to_ft, flds["rid"],
        {"cat": flds["cat"], "dnum": flds["dnum"], "dtxt": flds["dtxt"],
         "itop": flds["itop"], "ibot": flds["ibot"],
         "cgrp": flds["cgrp"], "exc": flds["exc"]})
    tcp_rows = station_points(
        tcp_lyr, line_geom, line_sr, to_ft, flds["tcp"], {})
    message("  Within {} ft: {} contamination rows, {} TCP points.".format(
        int(BUFFER_FT), len(contam_rows), len(tcp_rows)))
    if not contam_rows and not tcp_rows:
        message("  Nothing near this line - section skipped.", 1)
        return

    # Collapse joined duplicates: one location record, all its intervals.
    locations = {}
    for r in contam_rows:
        label = r["label"]
        if not label:
            continue
        key = (label, round(r["station_ft"], 1))
        a = r["attrs"]
        depth = as_float(a.get("dnum"))
        t_top, t_bot = parse_depth_text(a.get("dtxt"))
        if depth is None:
            depth = t_bot
        loc = locations.setdefault(key, {
            "label": label,
            "station": r["station_ft"],
            "dist": r["dist_ft"],
            "category": clean_text(a.get("cat")) or "Uncategorized",
            "depth": None,
            "intervals": [],
        })
        if depth is not None:
            loc["depth"] = max(loc["depth"] or 0.0, depth)
        itop = as_float(a.get("itop"))
        ibot = as_float(a.get("ibot"))
        if itop is None and ibot is None:
            itop, ibot = t_top, t_bot
        if ibot is not None:
            if itop is None or abs(ibot - itop) < POINT_BAND_THICKNESS_FT:
                mid = ibot if itop is None else (itop + ibot) / 2.0
                itop = max(0.0, mid - POINT_BAND_THICKNESS_FT / 2.0)
                ibot = mid + POINT_BAND_THICKNESS_FT / 2.0
            loc["intervals"].append({
                "top": itop, "bot": ibot,
                "group": clean_text(a.get("cgrp")) or "Unspecified",
                "exceed": clean_text(a.get("exc")) or "Unknown",
            })
    message("  {} unique locations ({} with depth).".format(
        len(locations),
        sum(1 for v in locations.values() if v["depth"])))

    # Vertical extent.
    ve = float(VERTICAL_EXAGGERATION)
    max_depth = MIN_DISPLAY_DEPTH_FT
    for loc in locations.values():
        if loc["depth"]:
            max_depth = max(max_depth, loc["depth"])
        for iv in loc["intervals"]:
            max_depth = max(max_depth, iv["bot"])
    max_depth += BOTTOM_PADDING_FT
    max_depth = DEPTH_INTERVAL_FT * (int(max_depth / DEPTH_INTERVAL_FT) + 1)
    y_bottom = (GROUND_ELEV_FT - max_depth) * ve
    y_top = GROUND_ELEV_FT * ve
    message("  Depth extent: 0 to {:.0f} ft bgs.".format(max_depth))

    scale = max(1.0, length_ft / 400.0)
    l_sdx = LEADER_START_DX if LEADER_START_DX is not None else 3.0 * scale
    l_sdy = LEADER_START_DY if LEADER_START_DY is not None else 1.0 * scale
    l_edx = LEADER_END_DX if LEADER_END_DX is not None else 8.0 * scale
    l_edy = LEADER_END_DY if LEADER_END_DY is not None else 3.0 * scale
    l_gap = LABEL_GAP_DX if LABEL_GAP_DX is not None else 1.5 * scale
    top_label_dy = 2.0 * scale        # "TOP" style: label height above surface
    tcp_label_dy = 5.0 * scale        # TCP labels float a bit higher

    # Feature classes for this section.
    fc = {}
    fc["surface"] = recreate_fc(workspace, "{}_{}".format(sec, OUT_SUFFIXES["surface"]),
                                "POLYLINE", [("FEATURE", "TEXT", 50)])
    fc["points"] = recreate_fc(workspace, "{}_{}".format(sec, OUT_SUFFIXES["points"]),
                               "POINT", [
        ("SOURCE", "TEXT", 20), ("LABEL_ID", "TEXT", 100),
        ("CATEGORY", "TEXT", 100), ("STATION_FT", "DOUBLE", None),
        ("DEPTH_FT", "DOUBLE", None), ("DIST_FROM_LINE_FT", "DOUBLE", None),
        ("HAS_DEPTH", "SHORT", None)])
    fc["sticks"] = recreate_fc(workspace, "{}_{}".format(sec, OUT_SUFFIXES["sticks"]),
                               "POLYLINE", [
        ("LABEL_ID", "TEXT", 100), ("DEPTH_FT", "DOUBLE", None),
        ("CATEGORY", "TEXT", 100)])
    fc["bands"] = recreate_fc(workspace, "{}_{}".format(sec, OUT_SUFFIXES["bands"]),
                              "POLYGON", [
        ("LABEL_ID", "TEXT", 100), ("CATEGORY", "TEXT", 100),
        ("CONTAM_GROUP", "TEXT", 100), ("EXCEEDANCE", "TEXT", 60),
        ("TOP_FT", "DOUBLE", None), ("BOT_FT", "DOUBLE", None),
        ("DISPLAY_CLASS", "TEXT", 100)])
    fc["leaders"] = recreate_fc(workspace, "{}_{}".format(sec, OUT_SUFFIXES["leaders"]),
                                "POLYLINE", [("LABEL_ID", "TEXT", 100)])
    fc["anchors"] = recreate_fc(workspace, "{}_{}".format(sec, OUT_SUFFIXES["anchors"]),
                                "POINT", [
        ("LABEL_TEXT", "TEXT", 150), ("LABEL_ROLE", "TEXT", 20)])
    fc["grid"] = recreate_fc(workspace, "{}_{}".format(sec, OUT_SUFFIXES["grid"]),
                             "POLYLINE", [("GRID_TYPE", "TEXT", 20)])
    fc["axes"] = recreate_fc(workspace, "{}_{}".format(sec, OUT_SUFFIXES["axes"]),
                             "POLYLINE", [("AXIS", "TEXT", 20)])
    fc["axlabels"] = recreate_fc(workspace, "{}_{}".format(sec, OUT_SUFFIXES["axlabels"]),
                                 "POINT", [
        ("LABEL_TEXT", "TEXT", 100), ("LABEL_TYPE", "TEXT", 20)])

    # Surface line.
    with arcpy.da.InsertCursor(fc["surface"], ["FEATURE", "SHAPE@"]) as cur:
        cur.insertRow(["Ground Surface (flat)",
                       [(0.0, y_top), (length_ft, y_top)]])

    # Points / sticks / bands / labels.
    cur_pts = arcpy.da.InsertCursor(fc["points"], [
        "SOURCE", "LABEL_ID", "CATEGORY", "STATION_FT", "DEPTH_FT",
        "DIST_FROM_LINE_FT", "HAS_DEPTH", "SHAPE@XY"])
    cur_stk = arcpy.da.InsertCursor(fc["sticks"],
                                    ["LABEL_ID", "DEPTH_FT", "CATEGORY",
                                     "SHAPE@"])
    cur_bnd = arcpy.da.InsertCursor(fc["bands"], [
        "LABEL_ID", "CATEGORY", "CONTAM_GROUP", "EXCEEDANCE",
        "TOP_FT", "BOT_FT", "DISPLAY_CLASS", "SHAPE@"])
    cur_ldr = arcpy.da.InsertCursor(fc["leaders"], ["LABEL_ID", "SHAPE@"])
    cur_anc = arcpy.da.InsertCursor(fc["anchors"],
                                    ["LABEL_TEXT", "LABEL_ROLE", "SHAPE@XY"])

    n_sticks = n_bands = 0
    for loc in sorted(locations.values(), key=lambda d: d["station"]):
        x = loc["station"]
        has_depth = 1 if loc["depth"] else 0
        cur_pts.insertRow(["CONTAM", loc["label"], loc["category"], x,
                           loc["depth"], loc["dist"], has_depth, (x, y_top)])
        if has_depth:
            y_bot = (GROUND_ELEV_FT - loc["depth"]) * ve
            cur_stk.insertRow([loc["label"], loc["depth"], loc["category"],
                               [(x, y_top), (x, y_bot)]])
            n_sticks += 1
            if LABEL_STYLE.upper() == "LEADER":
                cur_ldr.insertRow([loc["label"],
                                   [(x + l_sdx, y_top + l_sdy),
                                    (x + l_edx, y_top + l_edy)]])
                cur_anc.insertRow([loc["label"], "DEPTH_ID",
                                   (x + l_edx + l_gap, y_top + l_edy)])
            else:  # "TOP": label floats at the top of the stick
                cur_anc.insertRow([loc["label"], "DEPTH_ID",
                                   (x, y_top + top_label_dy)])
        else:
            cur_anc.insertRow([loc["label"], "PLAIN_ID",
                               (x, y_top + top_label_dy)])
        for iv in loc["intervals"]:
            top_y = (GROUND_ELEV_FT - iv["top"]) * ve
            bot_y = (GROUND_ELEV_FT - iv["bot"]) * ve
            ring = [(x - BLOCK_HALF_WIDTH_FT, top_y),
                    (x + BLOCK_HALF_WIDTH_FT, top_y),
                    (x + BLOCK_HALF_WIDTH_FT, bot_y),
                    (x - BLOCK_HALF_WIDTH_FT, bot_y),
                    (x - BLOCK_HALF_WIDTH_FT, top_y)]
            cur_bnd.insertRow([loc["label"], loc["category"], iv["group"],
                               iv["exceed"], iv["top"], iv["bot"],
                               loc["category"], [ring]])
            n_bands += 1

    for r in sorted(tcp_rows, key=lambda d: d["station_ft"]):
        if not r["label"]:
            continue
        x = r["station_ft"]
        cur_pts.insertRow(["TCP", r["label"], "TCP Cleanup Site", x, None,
                           r["dist_ft"], 0, (x, y_top)])
        cur_anc.insertRow([r["label"], "TCP_ID", (x, y_top + tcp_label_dy)])

    for c in (cur_pts, cur_stk, cur_bnd, cur_ldr, cur_anc):
        del c
    message("  Wrote {} sticks, {} interval bands.".format(n_sticks, n_bands))

    # Grid, axes, tick labels.
    cur_grd = arcpy.da.InsertCursor(fc["grid"], ["GRID_TYPE", "SHAPE@"])
    cur_axs = arcpy.da.InsertCursor(fc["axes"], ["AXIS", "SHAPE@"])
    cur_lbl = arcpy.da.InsertCursor(fc["axlabels"],
                                    ["LABEL_TEXT", "LABEL_TYPE", "SHAPE@XY"])
    station = 0.0
    while station <= length_ft + 0.01:
        cur_grd.insertRow(["STATION", [(station, y_top), (station, y_bottom)]])
        cur_lbl.insertRow(["{:.0f}".format(station), "STATION",
                           (station, y_bottom - 1.5 * scale)])
        station += HORIZONTAL_INTERVAL_FT
    depth = 0.0
    while depth <= max_depth + 0.01:
        y = (GROUND_ELEV_FT - depth) * ve
        cur_grd.insertRow(["DEPTH", [(0.0, y), (length_ft, y)]])
        cur_lbl.insertRow(["{:.0f}".format(depth), "DEPTH",
                           (-2.0 * scale, y)])
        depth += DEPTH_INTERVAL_FT
    cur_axs.insertRow(["BOTTOM", [(0.0, y_bottom), (length_ft, y_bottom)]])
    cur_axs.insertRow(["LEFT", [(0.0, y_bottom), (0.0, y_top)]])
    cur_axs.insertRow(["SURFACE", [(0.0, y_top), (length_ft, y_top)]])
    cur_lbl.insertRow(["Distance Along Section (ft)", "TITLE_X",
                       (length_ft / 2.0, y_bottom - 4.0 * scale)])
    cur_lbl.insertRow(["Depth Below Ground Surface (ft)", "TITLE_Y",
                       (-6.0 * scale, (y_top + y_bottom) / 2.0)])
    for c in (cur_grd, cur_axs, cur_lbl):
        del c

    # Add to map in draw order & style (bottom -> top).
    ours = {"{}_{}".format(sec, s) for s in OUT_SUFFIXES.values()}
    for lyr in list(xsec_map.listLayers()):
        if lyr.name in ours:
            xsec_map.removeLayer(lyr)
    draw_order = ["grid", "axes", "surface", "bands", "sticks", "leaders",
                  "points", "anchors", "axlabels"]
    added = {}
    for key in reversed(draw_order):
        added[key] = xsec_map.addDataFromPath(fc[key])
    style_layers(added)


# =============================================================================
# SYMBOLOGY + LABELING (best-effort; never fatal)
# =============================================================================

def style_layers(added):
    def try_style(fn, what):
        try:
            fn()
        except Exception as e:
            message("  Styling skipped for {} ({}).".format(what, e), 1)

    def _points():
        lyr = added["points"]
        sym = lyr.symbology
        sym.updateRenderer("UniqueValueRenderer")
        sym.renderer.fields = ["CATEGORY"]
        lyr.symbology = sym

    def _bands():
        lyr = added["bands"]
        sym = lyr.symbology
        sym.updateRenderer("UniqueValueRenderer")
        sym.renderer.fields = ["DISPLAY_CLASS"]
        lyr.symbology = sym

    def _sticks():
        lyr = added["sticks"]
        sym = lyr.symbology
        sym.renderer.symbol.color = {"RGB": [110, 110, 110, 100]}
        sym.renderer.symbol.width = 0.5
        lyr.symbology = sym

    def _anchors():
        lyr = added["anchors"]
        sym = lyr.symbology
        sym.renderer.symbol.size = 0
        try:
            sym.renderer.symbol.color = {"RGB": [0, 0, 0, 0]}
        except Exception:
            pass
        lyr.symbology = sym
        lc = lyr.listLabelClasses()[0]
        lc.expression = "$feature.LABEL_TEXT"
        lyr.showLabels = True

    def _axlabels():
        lyr = added["axlabels"]
        sym = lyr.symbology
        sym.renderer.symbol.size = 0
        lyr.symbology = sym
        lc = lyr.listLabelClasses()[0]
        lc.expression = "$feature.LABEL_TEXT"
        lyr.showLabels = True

    def _grid():
        lyr = added["grid"]
        sym = lyr.symbology
        sym.renderer.symbol.color = {"RGB": [210, 210, 210, 45]}
        sym.renderer.symbol.width = 0.4
        lyr.symbology = sym

    try_style(_points, "Points")
    try_style(_bands, "Interval_Bands")
    try_style(_sticks, "Depth_Sticks")
    try_style(_anchors, "Label_Anchors")
    try_style(_axlabels, "Axis_Labels")
    try_style(_grid, "Grid")


# =============================================================================
# MAIN
# =============================================================================

def main():
    message("=" * 70)
    message("Multi-section cross-section build (VE = {}x, label style = {})"
            .format(VERTICAL_EXAGGERATION, LABEL_STYLE))
    message("=" * 70)
    arcpy.env.overwriteOutput = True
    project = arcpy.mp.ArcGISProject("CURRENT")
    workspace = OUTPUT_GDB or project.defaultGeodatabase
    message("Output geodatabase: {}".format(workspace))

    contam_lyr = find_layer_anywhere(project, CONTAM_POINTS_LAYER)
    tcp_lyr = find_layer_anywhere(project, TCP_POINTS_LAYER)
    flds = {
        "rid":  find_field(contam_lyr, FLD_REPORT_ID),
        "cat":  find_field(contam_lyr, FLD_CATEGORY, required=False),
        "dnum": find_field(contam_lyr, FLD_DEPTH_NUM, required=False),
        "dtxt": find_field(contam_lyr, FLD_DEPTH_TEXT, required=False),
        "itop": find_field(contam_lyr, FLD_INT_TOP, required=False),
        "ibot": find_field(contam_lyr, FLD_INT_BOT, required=False),
        "cgrp": find_field(contam_lyr, FLD_CONTAM_GRP, required=False),
        "exc":  find_field(contam_lyr, FLD_EXCEED, required=False),
        "tcp":  find_field(tcp_lyr, FLD_TCP_NAME),
    }
    message("Contam fields -> id:{rid} cat:{cat} depth:{dnum}/{dtxt} "
            "interval:{itop}/{ibot}".format(**flds))

    for sec_name, geom, sr, to_ft, length_ft in get_section_lines(project):
        build_section(project, workspace, sec_name, geom, sr, to_ft,
                      length_ft, contam_lyr, tcp_lyr, flds)

    if SAVE_PROJECT:
        try:
            project.save()
        except Exception:
            message("Could not save project - save manually.", 1)
    message("=" * 70)
    message("DONE. One map per section (prefix '{}').".format(MAP_PREFIX))
    message("=" * 70)


# =============================================================================
# METHANE / FUTURE OVERLAY
# =============================================================================

def add_overlay_bands(section, table, id_field, top_field, bot_field,
                      value_field, out_suffix="Methane_Bands"):
    """
    Run AFTER the main build, once methane data exists. Example:

        add_overlay_bands("XS_A", "MethaneTable", "REPORT_ID",
                          "TOP_FT", "BOT_FT", "CH4_PCT")

    Draws value-attributed boxes offset right of the existing sticks on that
    section, matched by report ID. Symbolize with graduated colors on VALUE
    for a binned legend like the PCB reference figure. If methane arrives as
    single depths instead of intervals, pass the same field for top and
    bottom - it becomes a 0.5 ft band automatically.
    """
    project = arcpy.mp.ArcGISProject("CURRENT")
    workspace = OUTPUT_GDB or project.defaultGeodatabase
    sec = safe_name(section)
    xsec_map = find_map(project, MAP_PREFIX + sec)
    pts = os.path.join(workspace, "{}_{}".format(sec, OUT_SUFFIXES["points"]))
    stations = {}
    with arcpy.da.SearchCursor(pts, ["LABEL_ID", "STATION_FT"]) as cur:
        for lab, sta in cur:
            stations[lab] = sta
    out = recreate_fc(workspace, "{}_{}".format(sec, out_suffix), "POLYGON", [
        ("LABEL_ID", "TEXT", 100), ("VALUE", "DOUBLE", None),
        ("TOP_FT", "DOUBLE", None), ("BOT_FT", "DOUBLE", None)])
    off = BLOCK_HALF_WIDTH_FT * 1.2
    ve = float(VERTICAL_EXAGGERATION)
    n = 0
    with arcpy.da.InsertCursor(
            out, ["LABEL_ID", "VALUE", "TOP_FT", "BOT_FT", "SHAPE@"]) as ins, \
         arcpy.da.SearchCursor(
            table, [id_field, top_field, bot_field, value_field]) as cur:
        for lab, top, bot, val in cur:
            lab = clean_text(lab)
            if lab not in stations:
                continue
            top, bot = as_float(top), as_float(bot)
            if bot is None:
                continue
            if top is None or abs(bot - top) < POINT_BAND_THICKNESS_FT:
                mid = bot if top is None else (top + bot) / 2.0
                top = max(0.0, mid - POINT_BAND_THICKNESS_FT / 2.0)
                bot = mid + POINT_BAND_THICKNESS_FT / 2.0
            x = stations[lab]
            ty = (GROUND_ELEV_FT - top) * ve
            by = (GROUND_ELEV_FT - bot) * ve
            ring = [(x + off, ty), (x + off + BLOCK_HALF_WIDTH_FT, ty),
                    (x + off + BLOCK_HALF_WIDTH_FT, by), (x + off, by),
                    (x + off, ty)]
            ins.insertRow([lab, float(val) if val is not None else None,
                           top, bot, [ring]])
            n += 1
    xsec_map.addDataFromPath(out)
    message("Overlay '{}': {} bands added to {}.".format(
        out_suffix, n, MAP_PREFIX + sec))


# =============================================================================
# SCRIPT ENTRY POINT
# =============================================================================

if __name__ == "__main__":
    try:
        main()
    except Exception as error:
        message("Cross-section build failed: {}".format(error), 2)
        message(traceback.format_exc(), 2)
        try:
            gp = arcpy.GetMessages(2)
            if gp:
                message(gp, 2)
        except Exception:
            pass
        raise

