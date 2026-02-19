# User Stories: RMI Health Dashboard (PoC)

## Epic 1: Professional Theme
**Story 1.1: Light Mode Styling**
- **As a** User,
- **I want** a clean, professional interface with white backgrounds and Teal accents,
- **So that** the dashboard feels authoritative and easy to read.
- **Acceptance Criteria**:
    - Background is White (`#ffffff`) or Light Slate (`#f8fafc`).
    - Primary color is Teal (`#0d9488`).
    - Font is Inter.
    - No dark mode elements remain.

## Epic 2: Map Experience (Blue Map)
**Story 2.1: OpenStreetMap Integration**
- **As a** User,
- **I want** to see the Marshall Islands on a standard "Blue/Green" map (OpenStreetMap),
- **So that** I have clear geographic context of the atolls and oceans.
- **Acceptance Criteria**:
    - Map tiles are set to OpenStreetMap.
    - Default Zoom Level is 6.

**Story 2.2: Rich Popups & View Details Trigger**
- **As a** User,
- **I want** to click a marker and see a quick summary (Name, Assistant, Type, Score) and a "View Details" button,
- **So that** I can trigger the deep dive directly from the marker.
- **Acceptance Criteria**:
    - Clicking a marker opens a Folium Popup.
    - Popup contains: Name, Island, Type, Health Assistant, Date, Score.
    - Popup includes a styled "View Details" button/link.
    - Clicking the "View Details" link in the popup triggers the Detail Modal.

## Epic 3: Deep Dive Analytics
**Story 3.1: Detail Modal**
- **As a** User,
- **I want** to click "View Details" to open a centered modal overlay,
- **So that** I can view historical performance for a specific center with high focus.
- **Acceptance Criteria**:
    - Clicking "View Details" triggers a centered Modal (`st.dialog`).
    - Modal width is "large".
    - Modal content includes: Facility Header, Key Metrics, Trend Chart, Historical Data Table.
    - Modal is dismissible via "X", ESC, or "Close" button.

**Story 3.2: Integrated National Trends**
- **As a** User,
- **I want** to scroll down from the map to see national performance trends,
- **So that** I can understand the bigger picture after exploring the map.
- **Acceptance Criteria**:
    - "National Performance Trends" section is located below the map fold.
    - Chart is persistent (not hidden behind a toggle).
    - Layout uses a contained width (not full-bleed) for readability.

## Epic 4: Data & Filtering
**Story 4.1: Empty State Filters**
- **As a** User,
- **I want** sidebar filters to start empty (showing all data),
- **So that** I am not overwhelmed by pre-selected options.
- **Acceptance Criteria**:
    - "Island" and "Type" filters default to no selection.
    - Logic interprets "No Selection" as "Show All".
