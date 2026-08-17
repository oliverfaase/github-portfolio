<!--
===============================================================================
OLIVER FAASE | ENVIRONMENTAL GIS PORTFOLIO
===============================================================================

CONTACT INFORMATION
Email:    faaseoliver@gmail.com
LinkedIn: https://www.linkedin.com/in/oliverfaase/

BEFORE PUBLISHING
1. Replace every instance of YOUR-GITHUB-USERNAME.
2. Add a landfill PDF and preview image when they are ready.
3. Confirm that both StoryMaps open while signed out of ArcGIS.
4. Confirm that all employer-related screenshots and videos are approved.
5. GitHub does not support interactive iframe embeds in README files.
   The StoryMaps are presented as clickable visual previews instead.
===============================================================================
-->

<div align="center">

# 🌎 Oliver Faase

### Environmental GIS • Geospatial Automation • Drone Mapping • Spatial Storytelling

**Transforming environmental data into reproducible GIS workflows,  
interactive applications, and decision-ready visualizations.**

<br>

#-featured-projects
  https://img.shields.io/badge/Explore-Featured_GIS_Projects-2E7D32?style=for-the-badge&logo=googleearth&logoColor=white
</a>

<a href="mailto:faaseoliver@gmail.com">
  https://img.shields.io/badge/Email-faaseoliver%40gmail.com-00796B?style=for-the-badge&logo=gmail&logoColor=white
</a>

<a href="https://www.linkedin.com/in/oliverfaase/">
  https://img.shields.io/badge/LinkedIn-Oliver_Faase-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white
</a>

<br><br>

https://komarev.com/ghpvc/?username=YOUR-GITHUB-USERNAME&label=Portfolio%20Views&color=2e7d32&style=flat-square

</div>

---

## 🧭 Portfolio Navigation

<div align="center">

#-about-meAbout</a>
&nbsp;&nbsp;•&nbsp;&nbsp;
#-featured-projectsProjects</a>
&nbsp;&nbsp;•&nbsp;&nbsp;
#️-technical-toolkitTechnical Toolkit</a>
&nbsp;&nbsp;•&nbsp;&nbsp;
#-project-workflowWorkflow</a>
&nbsp;&nbsp;•&nbsp;&nbsp;
#-connect-with-meContact</a>

</div>

---

## 🌿 About Me

I am an **Environmental GIS Intern** specializing in environmental data
management, ArcGIS automation, subsurface visualization, drone imagery,
interactive web mapping, and public-facing GIS communication.

My work focuses on transforming fragmented technical information into
geospatial systems that are:

- **Traceable**, with clear links to original records and source documents
- **Reproducible**, through Python, ArcPy, and documented GIS workflows
- **Spatially accurate**, with validated coordinate systems and QA/QC procedures
- **Accessible**, through maps, StoryMaps, applications, imagery, and multimedia
- **Decision-ready**, for environmental review, monitoring, and site management

### Current areas of interest

- Environmental and coastal GIS
- Python and ArcPy automation
- Subsurface data visualization
- Drone-based environmental monitoring
- Geospatial artificial intelligence
- Web GIS and interactive storytelling
- GIS database development and QA/QC

---

## 📍 Portfolio at a Glance

<div align="center">

<table>
  <tr>
    <td align="center" width="33%">
      <h3>336+</h3>
      <strong>Investigation Locations</strong><br>
      <sub>Organized within an environmental GIS inventory</sub>
    </td>
    <td align="center" width="33%">
      <h3>5</h3>
      <strong>Automated Cross Sections</strong><br>
      <sub>Generated through Python and ArcPy</sub>
    </td>
    <td align="center" width="33%">
      <h3>2D + 3D + Temporal</h3>
      <strong>Environmental Visualization</strong><br>
      <sub>Multidimensional GIS communication</sub>
    </td>
  </tr>
  <tr>
    <td align="center">
      <h3>🚁</h3>
      <strong>Drone Monitoring</strong><br>
      <sub>Repeatable aerial imagery collection</sub>
    </td>
    <td align="center">
      <h3>🌊</h3>
      <strong>Coastal GIS</strong><br>
      <sub>Shoreline and bathymetric analysis</sub>
    </td>
    <td align="center">
      <h3>🗺️</h3>
      <strong>Interactive GIS</strong><br>
      <sub>StoryMaps and Experience Builder</sub>
    </td>
  </tr>
</table>

</div>

---

# 🗺️ Featured Projects

## 01. Tacoma Tideflats Closed Landfill GIS and Cross-Section Automation

> **Environmental database development, subsurface modeling, QA/QC, and ArcPy automation**

<div align="center">

https://img.shields.io/badge/ArcGIS_Pro-2C7AC3?style=flat-square&logo=esri&logoColor=white
https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white
https://img.shields.io/badge/ArcPy-Automation-2E7D32?style=flat-square
https://img.shields.io/badge/Data-QA%2FQC-D97706?style=flat-square
https://img.shields.io/badge/Visualization-2D_%7C_3D_%7C_Temporal-6B46C1?style=flat-square

</div>

### Project overview

I developed an integrated GIS database and automated mapping workflow for
historical environmental information associated with the former Tacoma
Tideflats closed landfill.

The completed inventory includes **336 investigation locations**, including
boreholes, monitoring wells, test pits, probes, and soil borings. Records from
environmental investigations, parcel reports, historical inspections, methane
monitoring, and cleanup-site resources were consolidated into a structured and
traceable geospatial framework.

### Project impact

- Standardized investigation identifiers and investigation types
- Cleaned contaminant descriptions and analytical-result categories
- Standardized depth measurements and sampling intervals
- Connected investigation locations to available sampling-depth records
- Preserved source-document references and data-match confidence
- Used composite identifiers to reduce incorrect joins
- Distinguished exceedances, detections, landfill material, and missing results
- Prevented missing analytical information from being interpreted as clean
- Avoided extending one sampling result through an entire boring

### Automated cross-section workflow

The Python and ArcPy automation:

1. Processes cross-section lines
2. Selects nearby investigation locations
3. Calculates each location's station along the section
4. Interprets and validates sampling-depth intervals
5. Generates maps for sections **XS_A through XS_E**
6. Creates ground-surface lines and investigation points
7. Creates depth sticks and analytical interval bands
8. Generates label anchors, grids, axes, and annotations
9. Applies configurable vertical exaggeration
10. Automates feature-class creation and symbology

<details>
<summary><strong>🔍 View technical and QA/QC details</strong></summary>

<br>

The automation incorporates:

- Flexible field-name matching
- Null-safe depth parsing
- Duplicate-record handling
- Composite investigation identifiers
- Spatial-reference validation
- Configurable selection distances
- Configurable vertical exaggeration
- Automated symbology
- Source-document traceability
- Match-confidence fields
- Detailed error and status messages

I also developed a depth-based concentric-buffer workflow that generates
polygon rings at three-foot increments.

The cross-section framework was designed so additional environmental
measurements, including methane readings, can be added as value-based
depth-interval overlays.

</details>

### Project files

> [!NOTE]
> The downloadable project package and PDF case study will be added after the
> project has been prepared and approved for portfolio use.

<!--
ADD THE LANDFILL MATERIALS HERE LATER.

Suggested layout:

<div align="center">

LINK-TO-LANDFILL-PDF
  LINK-TO-LANDFILL-PREVIEW
</a>

<br><br>

LINK-TO-LANDFILL-PDF
  https://img.shields.io/badge/Open-PDF_Case_Study-C62828?style=for-the-badge&logo=adobeacrobatreader&logoColor=white
</a>

LINK-TO-PROJECT-PACKAGE
  https://img.shields.io/badge/Download-ArcGIS_Pro_Package-2C7AC3?style=for-the-badge&logo=esri&logoColor=white
</a>

</div>
-->

**Skills and technologies:** ArcGIS Pro, Python, ArcPy, environmental GIS
database development, subsurface modeling, cross-section stationing,
geoprocessing, QA/QC, 3D visualization, and technical communication.

<div align="right">

#️-featured-projects

</div>

---

## 02. Interactive Habitat Assessment StoryMap

> **Habitat mapping, drone imagery, restoration documentation, and environmental storytelling**

<div align="center">

https://img.shields.io/badge/ArcGIS-StoryMaps-7E57C2?style=flat-square&logo=esri&logoColor=white
https://img.shields.io/badge/Environmental-Habitat_Assessment-4D7C0F?style=flat-square
https://img.shields.io/badge/Drone-Aerial_Imagery-00796B?style=flat-square
https://img.shields.io/badge/Format-Interactive_Web_GIS-2563EB?style=flat-square

<br><br>

<a href="https://storymaps.arcgis.com/stories/d689d97a246a4b07b0ca6b90a1dcd5a0">
  <img
    src="https://github.com/user-attachments/assets/10c80feb-7134-409c-aa90-2a8086c44c49"
    alt="Interactive Habitat Assessment ArcGIS StoryMap"
    width="850"
  >
</a>

<br><br>

<a href="https://storymaps.arcgis.com/stories/d689d97a246a4b07b0ca6b90a1dcd5a0">
  https://img.shields.io/badge/Explore-Live_Habitat_StoryMap-7E57C2?style=for-the-badge&logo=esri&logoColor=white
</a>

<p>
  <em>Select the preview or button to explore the public StoryMap.</em>
</p>

</div>

### Project overview

I developed an interactive ArcGIS StoryMap showcasing habitat assessment and
restoration sites throughout the Port of Tacoma.

The StoryMap combines interactive GIS mapping, high-resolution drone imagery,
site descriptions, and aerial flyover videos. Visitors can navigate between
habitat locations and explore environmental conditions, restoration work, and
the environmental significance of individual sites.

### Project contributions

- Developed an interactive habitat-site map tour
- Organized site-specific environmental information
- Integrated high-resolution drone imagery
- Helped collect aerial imagery during field operations
- Incorporated drone flyover video for selected locations
- Created an accessible public-facing GIS experience
- Translated technical environmental information into a visual narrative
- Designed content for staff, stakeholders, and public audiences

### Original project video

The following GitHub-hosted media demonstrates the Habitat Assessment StoryMap:

https://github.com/user-attachments/assets/10c80feb-7134-409c-aa90-2a8086c44c49

<details>
<summary><strong>🌿 View the environmental communication workflow</strong></summary>

<br>

```text
Habitat Assessment Locations
             ↓
Site-Specific Environmental Information
             ↓
Drone Imagery and Flyover Video
             ↓
Interactive Map Tour
             ↓
Environmental Storytelling
             ↓
Staff, Stakeholder, and Public Communication
Environmental Review and Documentation
