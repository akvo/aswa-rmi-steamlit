# Product Requirements Document (PRD): RMI Health Dashboard (PoC)

## 1. Goal Description
The **RMI Health Dashboard** provides a professional, high-fidelity spatial interface for the RMI Ministry of Health. It combines a "Maps-First" exploration experience with deep analytical drill-downs, styled in a clean, modern aesthetic to support data-driven decision-making for remote health centers.

## 2. Target Users
- **Ministry Officials**: Need high-level national status and specific facility details.
- **Health Admins**: Monitor facility performance, staffing (Health Assistants), and reporting compliance.

## 3. User Journeys
- **National Overview**: Immediate view of the entire archipelago with high-level metrics (Total Centers, Global Avg).
- **Geographic Exploration**: Pan/Zoom the "Blue Map" to clusters of atolls.
- **Preview & Context**: Click a marker to see a quick popup summary (Name, Assistant, Type, Score).
- **Deep Dive**: Click "View Details" to open the **Detail Modal** for historical trends and comparative analytics.
- **National Analysis**: Scroll below the map to see the **National Performance Trends** integrated section.

## 4. Functional Requirements

### 4.1 Data & Integestion
- **FR-01**: System must load data from `transformers/RMI_OUTPUT.csv`.
- **FR-02**: System must parse date fields (YYYY-MM-DD); missing lat/longs must be handled gracefully without crashing the map.

### 4.2 Interactive Map (Blue Map)
- **FR-03**: Map must use **OpenStreetMap** tiles (Standard Blue/Green) for clear geographic context.
- **FR-04**: Default view must be Zoom Level **6**, centered on RMI archipelago.
- **FR-05**: Markers must be color-coded by Performance Score:
    - **Emerald (Dark Green)**: ≥ 80
    - **Amber (Orange)**: 50 - 79
    - **Rose (Red)**: < 50
- **FR-06**: Clicking a marker must open a Rich HTML popup displaying:
    - **Health Centre Name** (Bold)
    - Island
    - **Type** (e.g., Dispensary)
    - **Health Assistant** Name
    - **Date** (Formatted Month Day, Year)
    - **Score** (Colored)
    - **"View Details" Link/Button**: A clickable element to trigger the detail view.

### 4.3 Interaction Flow (Preview -> Detail)
- **FR-07**: **Interaction Trigger**: The "View Details" button inside the map marker popup must trigger the **Detail Modal** (implemented via `st.dialog`) for that center.
- **FR-07a**: The transition must use `st.session_state` to track the "active dialog" center and trigger the dialog function on app rerun.
- **FR-08**: **Detail State**: The modal must display with `width="large"` to ensure analytics charts are readable.
- **FR-09**: The Detail Modal must display:
    - Facility Header (Name, Island, Type)
    - Key Metrics (Latest Score, Trend vs Previous)
    - Trend Chart (Score over Time)
    - Historical Data Table

### 4.4 Analytics & Visualization
- **FR-10**: **Floating Metrics**: Show Key KPIs (Centers, Global Avg, Missing Geo) in Glassmorphism cards at the Top Left.
- **FR-11**: **Integrated Trends**: Display "National Performance Trends" section flowing naturally below the map (not floating).

### 4.5 Filters
- **FR-12**: Sidebar must contain multi-select filters for **Atoll/Island** and **Health Centre Type**.
- **FR-13**: Filters must default to "Empty" (implying All/None selected logic handles full data display).

## 5. Technical Details
- **State Management**: Use `st.session_state.preview_center` to store the name of the health center returned by `st_folium['last_object_clicked_tooltip']`.
- **UI Trigger**: A floating `st.button` will be displayed when `preview_center` is active.
- **Folium Ingestion**: The marker popup HTML in `map_view.py` will be updated to include a CSS-styled "View Details" button for visual continuity.
- **Reruns**: The transition from map click to floating button display requires a Streamlit rerun, which is automatically triggered by `st_folium`.

## 6. Non-Functional Requirements
- **NFR-01**: **Theme**: Application must use **Professional Light Mode**.
    - Primary: Teal (`#0d9488`)
    - Secondary: Slate (`#475569`)
    - Background: White/Frosted Glass
    - Font: **Inter** (sans-serif)
- **NFR-02**: **Performance**: Dashboard must load within 3 seconds locally.
- **NFR-03**: **Stability**: Floating elements must not overlap or create "Ghost Boxes".

## 6. Out of Scope
- Real-time DB write-back.
- Authentication.
