# User Stories: RMI Health Dashboard (PoC)

## Epic 1: Professional Theme
**Story 1.1: Light Mode Styling [x]**
- **As a** User,
- **I want** a clean, professional interface with white backgrounds and Teal accents,
- **So that** the dashboard feels authoritative and easy to read.
- **Acceptance Criteria**:
    - [x] Background is White (`#ffffff`) or Light Slate (`#f8fafc`).
    - [x] Primary color is Teal (`#0d9488`).
    - [x] Font is Inter.
    - [x] No dark mode elements remain.

## Epic 2: Map Experience (Blue Map)
**Story 2.1: OpenStreetMap Integration [x]**
- **As a** User,
- **I want** to see the Marshall Islands on a standard "Blue/Green" map (OpenStreetMap),
- **So that** I have clear geographic context of the atolls and oceans.
- **Acceptance Criteria**:
    - [x] Map tiles are set to OpenStreetMap.
    - [x] Default Zoom Level is 6.

**Story 2.2: Rich Popups & View Details Trigger [x]**
- **As a** User,
- **I want** to click a marker and see a quick summary (Name, Assistant, Type, Score) and a "View Details" button,
- **So that** I can trigger the deep dive directly from the marker.
- **Acceptance Criteria**:
    - [x] Clicking a marker triggers the Detail Modal (Optimized to skip popup for directness).
    - [x] Modal contains: Name, Island, Type, Health Assistant, Date, Score.

## Epic 3: Deep Dive Analytics
**Story 3.1: Detail Modal [x]**
- **As a** User,
- **I want** to click "View Details" to open a centered modal overlay,
- **So that** I can view historical performance for a specific center with high focus.
- **Acceptance Criteria**:
    - [x] Clicking a marker triggers a centered Modal (`st.dialog` or `streamlit-modal`).
    - [x] Modal width is "large".
    - [x] Modal content includes: Facility Header, Key Metrics, Trend Chart, Historical Data Table.
    - [x] Modal is dismissible.

**Story 3.2: Integrated National Trends [x]**
- **As a** User,
- **I want** to scroll down from the map to see national performance trends,
- **So that** I can understand the bigger picture after exploring the map.
- **Acceptance Criteria**:
    - [x] "National Performance Trends" section is located below the map fold.
    - [x] Chart is persistent.
    - [x] Layout uses a contained width.

## Epic 4: Data & Filtering
**Story 4.1: Empty State Filters [x]**
- **As a** User,
- **I want** sidebar filters to start empty (showing all data),
- **So that** I am not overwhelmed by pre-selected options.
- **Acceptance Criteria**:
    - [x] "Island" and "Type" filters default to no selection.
    - [x] Logic interprets "No Selection" as "Show All".
