# Tacoma Tideflats Closed Landfill GIS Automation

This project demonstrates an ArcGIS Pro and ArcPy workflow for organizing
historical environmental investigation records and generating measured
subsurface cross-section visualizations.

## Project Summary

The workflow supports:

- 336 investigation-location records
- Boreholes, monitoring wells, test pits, probes, and soil borings
- Standardized environmental status categories
- Sampling-depth and analytical-interval integration
- Automated cross sections XS_A through XS_E
- Depth sticks and analytical interval bands
- Configurable section buffers and vertical exaggeration
- Automated grids, axes, labels, and symbology
- QA/QC and source-record traceability

## Repository Contents

### Cross-Section Automation

scripts/build_cross_sections.py

Builds all configured cross sections in one run. For each section, the script
creates:

- Ground-surface line
- Investigation-location points
- Total-depth sticks
- Analytical interval bands
- Label anchors and optional leader lines
- Station and depth grids
- Axes and axis labels

### Depth-Based Buffer Rings

scripts/create_depth_buffer_rings.py

Creates point-specific concentric polygon rings at configurable depth
increments.

## General Workflow

```text
Historical Environmental Records
                ↓
Data Cleaning and Standardization
                ↓
Investigation-Location Database
                ↓
Depth-Interval Integration
                ↓
Spatial Selection and Stationing
                ↓
Automated Cross-Section Features
                ↓
Symbology, Labels, Grids, and Axes
                ↓
QA/QC and Technical Communication
