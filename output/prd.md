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
- **Deep Dive**: Click "View Details" to open the **Detail Drawer** for historical trends and comparative analytics.
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

### 4.3 Interaction Flow (Preview -> Detail)
- **FR-07**: **Preview State**: When a marker is clicked, a "View Details" button must appear (Toast/Floating) at the bottom of the screen.
- **FR-08**: **Detail State**: Clicking "View Details" must open the **Detail Drawer** sliding in from the right.
- **FR-09**: The Detail Drawer must display:
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

## 5. Non-Functional Requirements
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
