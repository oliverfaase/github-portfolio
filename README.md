**Tacoma Tideflats Closed Landfill GIS & Cross-Section Automation:**

This project involved developing an integrated GIS database and automated mapping workflow to organize, analyze, and visualize historical environmental information associated with the former Tacoma Tideflats closed landfill. I consolidated records from environmental investigations, parcel reports, historical inspections, methane monitoring, and cleanup-site resources into a structured geospatial framework. The completed inventory included 336 investigation locations, such as boreholes, monitoring wells, test pits, probes, and soil borings.

I cleaned and standardized location identifiers, investigation types, contaminant descriptions, depth measurements, analytical results, and site-status categories. I also developed a data-matching workflow that connected investigation locations with available sampling-depth intervals while preserving match confidence and source-document references. Because many reports reused investigation identifiers, I incorporated composite identifiers and quality-control fields to reduce incorrect joins and maintain traceability to the original records.

Using ArcGIS Pro, I created 2D, 3D, temporal, and cross-sectional visualizations to communicate the horizontal and vertical distribution of available environmental information. These products distinguished between confirmed exceedances, detections below applicable cleanup levels, observed landfill material, and locations without analytical data. The workflow was designed to prevent locations with missing analytical information from being incorrectly interpreted as clean and to avoid extending a single-depth result through an entire boring.

A major component of the project was developing Python and ArcPy scripts to automate environmental cross-section mapping. The multi-section workflow processes cross-section lines, selects nearby investigation points, calculates each point’s station along the section, interprets available depth intervals, and generates separate ArcGIS Pro maps for sections XS_A through XS_E. For each section, the script creates ground-surface lines, investigation points, depth sticks, interval bands, label anchors, grid lines, axes, and distance and depth labels.

The automation includes flexible field-name matching, null-safe depth parsing, duplicate-record handling, spatial-reference validation, configurable vertical exaggeration, automated symbology, and detailed error messaging. I also developed a depth-based concentric-buffer workflow that generated polygon rings at three-foot increments and designed the cross-section framework so additional environmental measurements, such as methane readings, could be added as value-based interval overlays.

This project demonstrates my ability to transform fragmented historical and environmental records into a documented and reproducible GIS workflow. It combines environmental data management, spatial analysis, ArcPy automation, cross-section modeling, QA/QC, and technical communication to make complex subsurface information more accessible for environmental review and long-term site management.

**Skills & Technologies:**

ArcGIS Pro, Python & ArcPy Automation

Environmental GIS Database Development & QA/QC

Subsurface Cross-Section Modeling & Stationing

Contaminant, Depth-Interval & Historical Record Integration

2D, 3D & Temporal Environmental Visualization

Geoprocessing, Symbology & Feature-Class Automation


**Interactive Habitat Assessment StoryMap:**

This project involved the development of an interactive ArcGIS StoryMap designed to showcase habitat assessment sites throughout the Port of Tacoma and communicate environmental conditions in an engaging, accessible format. The StoryMap combines GIS mapping, drone imagery, and site-specific information to provide users with a detailed view of habitat restoration and monitoring areas across the port.

A key component of the project was the creation of an interactive map tour that allows users to explore individual habitat sites by selecting points on the map. Each location includes high-resolution aerial imagery captured by drones, which I helped collect during field operations, along with site descriptions that provide context about habitat characteristics, restoration efforts, and environmental significance. For select locations, the StoryMap also incorporates drone flyover videos that offer a more immersive perspective of site conditions and landscape features.

By integrating geospatial data, aerial imagery, and multimedia content into a single platform, the StoryMap transforms technical environmental information into an intuitive experience for staff, stakeholders, and the public. The project demonstrates the use of GIS storytelling and drone technology to improve environmental communication, increase site accessibility, and support a greater understanding of habitat conditions throughout the Port of Tacoma.

**Skills & Technologies:**

ArcGIS StoryMaps & Map Tour Development

Drone Imagery Collection & Processing

Habitat Assessment & Environmental GIS

Interactive Web Mapping & Multimedia Integration

GIS Storytelling & Public-Facing Communication

Spatial Data Visualization & Site Documentation

https://github.com/user-attachments/assets/10c80feb-7134-409c-aa90-2a8086c44c49







**Port of Tacoma Shoreline Monitoring Experience Builder:**

This project involved the development of an ArcGIS Experience Builder application designed to support long-term shoreline monitoring throughout the Port of Tacoma. The application displays shoreline monitoring locations as interactive map points, providing an organized and accessible way to track environmental conditions across multiple sites over time.

The monitoring program uses drone imagery collected from pre-defined flight locations and automated flight schedules, ensuring photographs are captured from the same positions and viewing angles during each survey. By maintaining consistent image collection methods, the application enables year-over-year comparisons of shoreline conditions, allowing users to visually assess changes in vegetation, sediment deposition, erosion, bank stability, and other environmental factors.

To enhance analysis capabilities, the project incorporates GeoAI workflows that compare imagery captured across different time periods and identify potential shoreline changes. These automated comparisons help streamline the detection of erosion, habitat shifts, and other environmental changes that may otherwise require extensive manual review. The resulting Experience Builder serves as a centralized platform for organizing drone imagery, visualizing shoreline conditions, and supporting data-driven environmental management and monitoring efforts throughout the Port of Tacoma.

**Skills & Technologies:**

ArcGIS Experience Builder & ArcGIS Online

Drone Imagery Management & Temporal Change Detection

Shoreline Monitoring & Environmental GIS Analysis

GeoAI-Assisted Image Comparison

Interactive Web Application Development

Spatial Data Integration & Visualization



https://github.com/user-attachments/assets/52ce3565-4f6b-4721-a516-202b5a457347




**Port of Tacoma Bathymetric Surface Development:**

Contributed to the development of a high-resolution bathymetric GIS dataset for the Port of Tacoma, transforming hydrographic survey data into an accurate representation of underwater terrain and seafloor topography. As part of the workflow, I processed and converted Triangulated Irregular Network (TIN) surfaces into raster datasets, enabling more efficient analysis, visualization, and integration with other geospatial resources. I also developed raster surfaces constrained to complex, curved shoreline and waterway boundaries, ensuring the final products accurately reflected real-world conditions while maintaining spatial precision.

This project required extensive spatial data processing, terrain modeling, quality assurance, and geodatabase management to create a reliable depiction of submerged environments across active port facilities. The resulting bathymetric layers provide critical information for maritime infrastructure planning, dredging operations, navigational assessments, environmental monitoring, and long-term coastal management. By converting complex survey measurements into accessible geospatial products, this work helped support data-driven decision-making within one of the Pacific Northwest's largest and most strategically important ports.

**Skills & Technologies:**

ArcGIS Pro

Bathymetric Mapping

Hydrographic Survey Data Processing

TIN-to-Raster Conversion

Raster Surface Development

Spatial Analysis

Terrain Modeling

Geodatabase Management

Quality Assurance / Quality Control (QA/QC)

Coastal & Maritime GIS Applications





<img width="2550" height="3300" alt="Bathy2" src="https://github.com/user-attachments/assets/86672c1a-431e-477c-8235-b6744dfeac63" />
<img width="2550" height="3300" alt="Bathy1" src="https://github.com/user-attachments/assets/b775447a-be58-466d-baff-3a50a5d25ca0" />






**Cal Poly CRP Studio Project GIS Database & StoryMap**

This project is a GIS-based database and interactive StoryMap created to organize, map, and showcase past Cal Poly City and Regional Planning studio projects. I built the project by compiling studio project records, cleaning and organizing the attribute data, and geocoding each project by location so it could be displayed spatially in an interactive web map.

The database allows users to explore projects by location, year, program level, project type, instructor, and major planning topics such as housing, transportation, climate change, policy planning, and urban design. By turning a list of past studio work into a mapped and searchable resource, the project makes it easier to understand the geographic reach and impact of Cal Poly planning studios across California and beyond.

I also developed an ArcGIS StoryMap to present the database in a more public-facing and visually engaging format. The StoryMap includes an interactive project map as well as a featured studio example that walks viewers through the planning process, including site analysis and GIS, community outreach and engagement, design development, public presentations, and final deliverables.

As part of the project, I presented the database and StoryMap to faculty, my department head, the Dean of Students, and an alumni group. These presentations focused on how the project could be added to the Cal Poly website as a recruitment, outreach, and fundraising tool. The goal was to help prospective students, alumni, donors, and community partners better understand the value of the City and Regional Planning program and the real-world impact of student studio work.


**Skills and Technologies:**

Geocoding

ArcGIS Online

ArcGIS StoryMaps

GIS data cleaning

Spatial database design

Interactive web mapping

Project categorization

Public presentation

Stakeholder communication

Urban planning storytelling

**To the project here:** https://storymaps.arcgis.com/stories/e9f5d7deea894d049f6b7b41eb5e7232
<img width="1317" height="633" alt="Screenshot 2026-05-19 at 2 25 01 PM" src="https://github.com/user-attachments/assets/86b1b34c-a945-4d38-a827-779c4a398fd2" />
