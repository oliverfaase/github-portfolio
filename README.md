<div align="center">

# 🌎 Oliver Faase

### GIS • Environmental Planning • Geospatial Automation • Drone Mapping • Spatial Storytelling

I transform complex environmental information into reproducible GIS workflows,  
interactive applications, and decision-ready visualizations.

<br>

[![Email](https://img.shields.io/badge/Email-faaseoliver%40gmail.com-00796B?style=for-the-badge&logo=gmail&logoColor=white)](mailto:faaseoliver@gmail.com)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Oliver_Faase-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/oliverfaase/)

</div>

---

## 🌿 About Me

I am an **Environmental GIS Intern** specializing in environmental planning, spatial data management, ArcGIS automation, subsurface visualization, drone imagery, interactive web mapping, and public-facing GIS communication.

My work focuses on creating geospatial systems that are:

- **Traceable**, with clear connections to original records and source documents
- **Reproducible**, through Python, ArcPy, and documented GIS workflows
- **Spatially accurate**, with validated coordinate systems and QA/QC procedures
- **Accessible**, through maps, imagery, applications, and multimedia
- **Decision-ready**, for environmental monitoring, planning, review, and site management

### Areas of Interest

- Environmental planning and GIS
- Coastal and shoreline analysis
- Python and ArcPy automation
- Subsurface data visualization
- Drone-based environmental monitoring
- GeoAI-assisted image analysis
- Interactive web mapping and GIS storytelling
- Spatial database development and QA/QC

---

## 📍 Portfolio at a Glance

<div align="center">
<table>
<tr>
<td align="center" width="33%"><h3>336+</h3><strong>Investigation Locations</strong><br><sub>Environmental GIS inventory</sub></td>
<td align="center" width="33%"><h3>5</h3><strong>Automated Cross Sections</strong><br><sub>Python and ArcPy workflow</sub></td>
<td align="center" width="33%"><h3>2D + 3D + Temporal</h3><strong>GIS Visualization</strong><br><sub>Environmental communication</sub></td>
</tr>
<tr>
<td align="center"><h3>🚁</h3><strong>Drone Monitoring</strong><br><sub>Repeatable aerial imagery</sub></td>
<td align="center"><h3>🌊</h3><strong>Coastal GIS</strong><br><sub>Shoreline and bathymetry</sub></td>
<td align="center"><h3>🗺️</h3><strong>Interactive GIS</strong><br><sub>StoryMaps and applications</sub></td>
</tr>
</table>
</div>

---

# 🗺️ Featured Projects

## 01 | Tacoma Tideflats Closed Landfill GIS and Cross-Section Automation

> **Environmental database development, subsurface modeling, QA/QC, and ArcPy automation**

<div align="center">

![ArcGIS Pro](https://img.shields.io/badge/ArcGIS_Pro-2C7AC3?style=flat-square&logo=esri&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![ArcPy Automation](https://img.shields.io/badge/ArcPy-Automation-2E7D32?style=flat-square)
![Data QA/QC](https://img.shields.io/badge/Data-QA%2FQC-D97706?style=flat-square)

</div>

### Project Overview

I developed an integrated GIS database and automated mapping workflow for historical environmental information associated with the former Tacoma Tideflats closed landfill.

The completed inventory includes **336 investigation locations**, including boreholes, monitoring wells, test pits, probes, and soil borings. Records from environmental investigations, parcel reports, historical inspections, methane monitoring, and cleanup-site resources were consolidated into a structured and traceable geospatial framework.

### Project Contributions

- Standardized investigation identifiers, investigation types, contaminant descriptions, and depth measurements
- Connected investigation locations to available sampling-depth records
- Preserved source-document references and data-match confidence
- Used composite identifiers to reduce incorrect joins
- Distinguished exceedances, detections, landfill material, and missing data
- Prevented missing analytical information from being interpreted as clean
- Avoided extending a single-depth result through an entire boring

### Automated Cross-Section Workflow

1. Processes cross-section lines
2. Selects nearby investigation locations
3. Calculates each location's station along the section
4. Interprets and validates sampling-depth intervals
5. Generates maps for sections **XS_A through XS_E**
6. Creates ground-surface lines, investigation points, and depth sticks
7. Creates analytical interval bands, labels, grids, and axes
8. Applies configurable vertical exaggeration and automated symbology

<details>
<summary><strong>View technical and QA/QC details</strong></summary>

<br>

- Flexible field-name matching
- Null-safe depth parsing
- Duplicate-record handling
- Composite investigation identifiers
- Spatial-reference validation
- Configurable selection distances and vertical exaggeration
- Automated feature-class creation and symbology
- Source-document traceability and match-confidence fields
- Detailed error and status messages

I also developed a depth-based concentric-buffer workflow that generates polygon rings at three-foot increments. The framework can incorporate additional measurements, including methane readings, as value-based depth-interval overlays.

</details>

### Portfolio Materials

<div align="center">

[![Read the Complete Project Fact Sheet](https://img.shields.io/badge/Read-Complete_Project_Fact_Sheet-C62828?style=for-the-badge&logo=adobeacrobatreader&logoColor=white)](https://oliverfaase.github.io/github-portfolio/tacoma-tideflats.html)

[![Download the ArcGIS Pro Project](https://img.shields.io/badge/Download-ArcGIS_Pro_Project-2C7AC3?style=for-the-badge&logo=esri&logoColor=white)](https://github.com/oliverfaase/github-portfolio/releases/tag/TacomaTideflats)

<br><br>

<sub>
Read the complete 20-page project fact sheet in the scrollable GitHub Pages viewer, or open the GitHub Release to download the ZIP containing the packaged ArcGIS Pro project.
</sub>

</div>

### Project Value

This project demonstrates my ability to transform fragmented historical and environmental records into a documented and reproducible GIS workflow. It combines environmental data management, spatial analysis, ArcPy automation, subsurface modeling, QA/QC, and technical communication.

**Skills and technologies:** ArcGIS Pro, Python, ArcPy, environmental GIS, database development, subsurface modeling, cross-section stationing, geoprocessing, QA/QC, 3D visualization, and technical communication.

---

## 02 | Interactive Habitat Assessment StoryMap

> **Habitat mapping, drone imagery, restoration documentation, and environmental storytelling**

<div align="center">

![ArcGIS StoryMaps](https://img.shields.io/badge/ArcGIS-StoryMaps-7E57C2?style=flat-square&logo=esri&logoColor=white)
![Habitat Assessment](https://img.shields.io/badge/Focus-Habitat_Assessment-4D7C0F?style=flat-square)
![Drone Imagery](https://img.shields.io/badge/Media-Drone_Imagery-00796B?style=flat-square)

</div>

### Project Overview

I developed an interactive ArcGIS StoryMap showcasing habitat assessment and restoration sites throughout the Port of Tacoma.

The StoryMap combines interactive GIS mapping, high-resolution drone imagery, site descriptions, and aerial flyover videos. Visitors can navigate among habitat locations and explore environmental conditions, restoration work, and the significance of individual sites.

### Project Contributions

- Developed an interactive habitat-site map tour
- Organized site-specific environmental information
- Integrated high-resolution drone imagery
- Helped collect aerial imagery during field operations
- Incorporated drone flyover videos for selected locations
- Translated technical environmental information into an accessible visual narrative

### Project Video

https://github.com/user-attachments/assets/10c80feb-7134-409c-aa90-2a8086c44c49

<div align="center">

<br>

[![Explore the Habitat StoryMap](https://img.shields.io/badge/Explore_the-Habitat_StoryMap-4D7C0F?style=for-the-badge&logo=esri&logoColor=white)](https://storymaps.arcgis.com/stories/d689d97a246a4b07b0ca6b90a1dcd5a0)

<br><br>

<sub>Select the button to open the public ArcGIS StoryMap.</sub>

</div>

<details>
<summary><strong>View the environmental communication workflow</strong></summary>

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
Public and Stakeholder Communication
```

</details>

### Project Value

By combining geospatial data, aerial imagery, and multimedia content, the StoryMap transforms technical environmental information into an intuitive and engaging experience. It demonstrates how GIS storytelling and drone technology can improve environmental communication and understanding of habitat conditions and restoration activities.

**Skills and technologies:** ArcGIS StoryMaps, ArcGIS Online, drone imagery, habitat assessment, environmental GIS, interactive web mapping, multimedia integration, site documentation, and public-facing GIS communication.

---

## 03 | Shoreline OIC 2026 Experience Builder

> **Repeatable drone monitoring, oriented imagery, temporal comparison, and shoreline change assessment**

<div align="center">

![ArcGIS Experience Builder](https://img.shields.io/badge/ArcGIS-Experience_Builder-007AC2?style=flat-square&logo=esri&logoColor=white)
![Drone Imagery](https://img.shields.io/badge/Monitoring-Drone_Imagery-00796B?style=flat-square)
![Temporal Change](https://img.shields.io/badge/Analysis-Temporal_Change-7C3AED?style=flat-square)
![GeoAI](https://img.shields.io/badge/Workflow-GeoAI-9333EA?style=flat-square)

</div>

### Project Overview

I developed an ArcGIS Experience Builder application supporting long-term shoreline monitoring throughout the Port of Tacoma. The application displays monitoring locations as interactive map points and organizes environmental conditions across multiple sites and time periods.

### Project Contributions

- Developed an interactive shoreline-monitoring application
- Organized monitoring locations within a centralized GIS platform
- Integrated repeatable drone imagery from predefined flight locations
- Supported year-over-year comparison of shoreline conditions
- Structured imagery for consistent temporal analysis
- Incorporated GeoAI-assisted image-comparison workflows
- Designed the application for environmental review and documentation

### Project Media


https://github.com/user-attachments/assets/f150c141-529b-4cb0-be04-7f30ffeb5613


</div>

### Monitoring and Analysis

Predefined drone flight locations and automated flight plans allow imagery to be collected from consistent positions and viewing angles. This supports comparison of vegetation change, sediment deposition, erosion, bank stability, habitat shifts, and other visible environmental changes.

The project also incorporates GeoAI-assisted workflows that compare imagery from different monitoring periods and identify locations that may require closer review.

<details>
<summary><strong>View the shoreline-monitoring workflow</strong></summary>

<br>

```text
Predefined Drone Flight Locations
                ↓
Repeatable Aerial Surveys
                ↓
Time-Stamped Shoreline Imagery
                ↓
Oriented Imagery Organization
                ↓
Experience Builder Visualization
                ↓
Temporal Image Comparison
                ↓
GeoAI-Assisted Change Identification
```

</details>

### Project Value

The application centralizes drone imagery, shoreline visualization, temporal comparison, and environmental documentation. It improves monitoring consistency and reduces the time required to locate and compare imagery from different survey periods.

> **Sharing note:** The live application and its underlying environmental data are not linked. The approved media and description demonstrate the workflow without sharing restricted content.

**Skills and technologies:** ArcGIS Experience Builder, ArcGIS Online, oriented imagery, drone imagery, temporal comparison, shoreline monitoring, environmental GIS, GeoAI-assisted image comparison, and interactive web application development.

---

## 04 | Port of Tacoma Bathymetric Surface Development

> **Hydrographic data processing, TIN-to-raster conversion, terrain modeling, and coastal GIS**

<div align="center">

![Bathymetric Mapping](https://img.shields.io/badge/GIS-Bathymetric_Mapping-0369A1?style=flat-square)
![TIN to Raster](https://img.shields.io/badge/Workflow-TIN_to_Raster-475569?style=flat-square)
![Terrain Modeling](https://img.shields.io/badge/Analysis-Terrain_Modeling-00796B?style=flat-square)
![Coastal GIS](https://img.shields.io/badge/Focus-Coastal_GIS-0284C7?style=flat-square)

</div>

### Project Overview

I contributed to the development of a high-resolution bathymetric GIS dataset for the Port of Tacoma by transforming hydrographic survey information into an accurate representation of underwater terrain and seafloor topography.

I converted Triangulated Irregular Network surfaces into raster datasets and developed raster surfaces constrained to complex, curved shoreline and waterway boundaries. This improved analysis, visualization, integration, and spatial precision.

### Project Contributions

- Processed hydrographic survey information
- Converted TIN surfaces into raster datasets
- Developed rasters constrained to complex shoreline boundaries
- Maintained spatial precision around curved waterways
- Conducted terrain-modeling and spatial-processing operations
- Evaluated outputs for gaps and boundary inconsistencies
- Performed geodatabase management and quality assurance

### Project Media

<div align="center">
<table>
<tr>
<td width="50%" valign="top"><img src="https://github.com/user-attachments/assets/86672c1a-431e-477c-8235-b6744dfeac63" alt="Port of Tacoma bathymetric surface visualization" width="100%"></td>
<td width="50%" valign="top"><img src="https://github.com/user-attachments/assets/b775447a-be58-466d-baff-3a50a5d25ca0" alt="Port of Tacoma bathymetric mapping product" width="100%"></td>
</tr>
</table>
<p><em>Bathymetric mapping products developed from hydrographic survey data.</em></p>
</div>

### Project Applications

- Maritime infrastructure planning
- Dredging operations
- Navigational assessments
- Underwater-terrain visualization
- Environmental monitoring
- Coastal and waterway management
- Long-term port planning

<details>
<summary><strong>View the bathymetric surface-development workflow</strong></summary>

<br>

```text
Hydrographic Survey Data
             ↓
Data Review and Preparation
             ↓
Triangulated Irregular Network
             ↓
TIN-to-Raster Conversion
             ↓
Shoreline Boundary Constraints
             ↓
Surface QA/QC
             ↓
Bathymetric Visualization
```

</details>

### Project Value

The project transformed complex hydrographic measurements into accessible geospatial surfaces that can be used alongside infrastructure, environmental, and operational datasets. Constraining raster surfaces to shoreline and waterway boundaries created a more realistic representation of submerged terrain.

**Skills and technologies:** ArcGIS Pro, bathymetric mapping, hydrographic survey processing, TIN-to-raster conversion, raster surface development, spatial analysis, terrain modeling, geodatabase management, coastal GIS, and QA/QC.

---

## 05 | Cal Poly City and Regional Planning GIS Database and StoryMap

> **Geocoding, spatial database design, interactive planning history, and stakeholder communication**

<div align="center">

![GIS Geocoding](https://img.shields.io/badge/GIS-Geocoding-C2410C?style=flat-square)
![ArcGIS StoryMaps](https://img.shields.io/badge/ArcGIS-StoryMaps-7E57C2?style=flat-square&logo=esri&logoColor=white)
![Urban Planning](https://img.shields.io/badge/Focus-Urban_Planning-B45309?style=flat-square)
![Stakeholder Communication](https://img.shields.io/badge/Skill-Stakeholder_Communication-334155?style=flat-square)

</div>

### Project Overview

I created a GIS database and interactive StoryMap to organize, map, and showcase past Cal Poly City and Regional Planning studio projects.

I compiled historical studio-project records, cleaned and standardized their attributes, and geocoded each project for display in an interactive web map. The database transformed a list of studio work into a spatial and searchable resource demonstrating the geographic reach and impact of the program.

### Project Contributions

- Compiled historical planning-studio project records
- Cleaned and standardized project attributes
- Geocoded projects by location
- Designed a structured and searchable GIS database
- Categorized projects by topic, year, program level, and instructor
- Developed an interactive ArcGIS StoryMap
- Created a featured planning-studio narrative
- Presented the project to university and alumni stakeholders
- Demonstrated recruitment, outreach, and fundraising applications

### Project Media

<div align="center">

<img src="https://github.com/user-attachments/assets/86b1b34c-a945-4d38-a827-779c4a398fd2" alt="Cal Poly City and Regional Planning Studio Project StoryMap" width="850">

<br><br>

[![Explore the Cal Poly StoryMap](https://img.shields.io/badge/Explore_the-Cal_Poly_StoryMap-B45309?style=for-the-badge&logo=esri&logoColor=white)](https://storymaps.arcgis.com/stories/e9f5d7deea894d049f6b7b41eb5e7232)

<br><br>

<sub>Select the button to open the public ArcGIS StoryMap.</sub>

</div>

### Searchable Project Categories

Location • Year • Program level • Project type • Instructor • Housing • Transportation • Climate change • Policy planning • Urban design

### Interactive Storytelling

The StoryMap includes an interactive project map and a featured studio example covering site analysis and GIS, community outreach, design development, public presentations, and final deliverables.

### Stakeholder Communication

I presented the database and StoryMap to faculty, my department head, university leadership, and an alumni group. The presentations demonstrated how the project could support recruitment, outreach, alumni engagement, community partnerships, fundraising, and communication of student-project impact.

<details>
<summary><strong>View the GIS database and StoryMap workflow</strong></summary>

<br>

```text
Historical Studio Records
             ↓
Attribute Cleaning
             ↓
Project Categorization
             ↓
Location Geocoding
             ↓
Spatial Database Development
             ↓
Interactive Web Map
             ↓
ArcGIS StoryMap
             ↓
Recruitment and Public Outreach
```

</details>

### Project Value

The project makes planning-studio work easier to explore by connecting each project to its location, year, topic, instructor, program level, and planning focus. It gives prospective students, alumni, donors, faculty, and community partners an accessible way to understand the program's geographic reach and real-world impact.

**Skills and technologies:** Geocoding, ArcGIS Online, ArcGIS StoryMaps, GIS data cleaning, spatial database design, interactive web mapping, project categorization, urban planning, public presentation, and stakeholder communication.

---

# 🛠️ Technical Toolkit

<div align="center">

![ArcGIS Pro](https://img.shields.io/badge/ArcGIS_Pro-2C7AC3?style=for-the-badge&logo=esri&logoColor=white)
![ArcGIS Online](https://img.shields.io/badge/ArcGIS_Online-1D4ED8?style=for-the-badge&logo=esri&logoColor=white)
![StoryMaps](https://img.shields.io/badge/StoryMaps-7E57C2?style=for-the-badge&logo=esri&logoColor=white)
![Experience Builder](https://img.shields.io/badge/Experience_Builder-007AC2?style=for-the-badge&logo=esri&logoColor=white)

<br>

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![ArcPy](https://img.shields.io/badge/ArcPy-2E7D32?style=for-the-badge)
![SQL](https://img.shields.io/badge/SQL-336791?style=for-the-badge&logo=postgresql&logoColor=white)
![Geodatabases](https://img.shields.io/badge/Geodatabases-475569?style=for-the-badge)

<br>

![Environmental Planning](https://img.shields.io/badge/Environmental_Planning-4D7C0F?style=for-the-badge)
![Drone Imagery](https://img.shields.io/badge/Drone_Imagery-00796B?style=for-the-badge)
![Terrain Modeling](https://img.shields.io/badge/Terrain_Modeling-92400E?style=for-the-badge)
![GeoAI](https://img.shields.io/badge/GeoAI-7C3AED?style=for-the-badge)

</div>

---

# 🔄 Project Approach

```mermaid
flowchart LR
    A[Environmental Records] --> B[Data Cleaning]
    B --> C[QA and Validation]
    C --> D[Geospatial Database]
    D --> E[Spatial Analysis]
    E --> F[Python and ArcPy]
    F --> G[Maps and Applications]
    G --> H[Planning and Environmental Decisions]
```

### Core Principles

- Preserve traceability to original records
- Document assumptions and limitations
- Distinguish missing information from confirmed absence
- Automate repeatable processes where appropriate
- Validate spatial references and data structures
- Design outputs for technical and nontechnical audiences
- Communicate environmental information accurately and responsibly

---

# 📫 Connect With Me

I am interested in GIS, environmental planning, geospatial automation, spatial data science, shoreline monitoring, drone-based mapping, coastal planning, and tools that make environmental information easier to understand.

<div align="center">

[![Email](https://img.shields.io/badge/Email-faaseoliver%40gmail.com-00796B?style=for-the-badge&logo=gmail&logoColor=white)](mailto:faaseoliver@gmail.com)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Oliver_Faase-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/oliverfaase/)

<br><br>

### 🌎 GIS • 🌿 Environmental Planning • 🗺️ Automation • 🌊 Spatial Communication

</div>
