# Research Findings: Hybrid Maps-First Dashboard

## 1. User Research & Layout Selection
- **The Challenge**: Users wanted a "Maps-First" experience but found full-screen overlays for filters less intuitive than the native Streamlit sidebar.
- **The Solution**: A **Hybrid Layout** was identified as the ideal balance.
    - **Persistent Filters**: Kept in the `st.sidebar` for structured navigation.
    - **Immersive Exploration**: The main canvas is a full-bleed map explorer.
    - **Float-Over Analysis**: Real-time metrics and trend charts occupy the map foreground as glassmorphism overlays.

## 2. Technical Feasibility
- **Streamlit Wide Mode**: Essential for providing the map with 100% of usable width.
- **Glassmorphism (CSS Blur)**: Successfully tested using `backdrop-filter: blur(12px)`. This ensures that data overlays don't feel like "interruptions" but rather "contextual layers" on top of the geography.
- **Folium Interaction**: bi-directional communication (marker click -> sidebar drawer) is stable via `st.session_state`.

## 3. Component Hierarchy
1.  **Primary**: Folkum Map (CartoDB Dark Matter).
2.  **Functional**: Sidebar Filters.
3.  **Informational**: Floating scorecards and Trend Tray.
4.  **Drill-down**: Right-side Detail Drawer.

## 4. Data Quality & Structure

### Dataset Overview
- **Source**: `transformers/RMI_OUTPUT.csv`
- **Total Records**: 78
- **Columns**: `id`, `island`, `healt_centre`, `latitude`, `longitude`, `health_centre_type`, `health_assistans`, `mhd_cd_aide`, `mayor`, `date`, `score`

### Critical Findings
- **Missing Coordinates**: 10 records (~12%) have missing 'latitude' and 'longitude'.
    - *Impact*: These health centers cannot be plotted on the map.
    - *Mitigation*: We will exclude these from the map view but include them in the data tables and charts.
- **Data Types**:
    - `date`: String format (YYYY-MM-DD), needs parsing.
    - `score`: Float, range seems to be 0-100 (needs validation, max seen 88, min 18).
    - `latitude`/`longitude`: Float.

## 2. Technical Constraints
- **Streamlit**: Selected framework.
- **Mapping**: `folium` via `streamlit-folium` is recommended over `st.map` because we need rich tooltips (HTML support) and custom markers (colors based on logic), which `st.map` (deck.gl) handles less flexibly for simple setups without more complex layer configuration.
- **Charts**: `altair` or `plotly` are good candidates. `st.line_chart` is simplest but `altair` offers better customization for tooltips and interactivity.

## 3. Refined Requirements (Additions to PRD)
- **FR-03 (Refined)**: System must filter out records with null lat/long *before* passing data to the map component.
- **FR-New**: Dashboard should display a "Data Completeness" metric or warning indicating how many centers are missing geolocation.
