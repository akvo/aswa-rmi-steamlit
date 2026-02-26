# ADR-003: Hybrid Layout Hierarchy (Sidebar + Full View Map)

## Context
The user requested a "Maps-First" experience but also valued the original approach with a sidebar. They want a full view map alongside the sidebar, with floating cards and trend charts.

## Decision
We will implement a **Hybrid Layout**:
1.  **Sidebar**: Use Streamlit's native `st.sidebar` for all filtering controls.
2.  **Main View**: The main content area will be a full-bleed map explorer.
3.  **Overlays**: All analytics (metrics, trend charts) will be implemented as floating glassmorphism overlays on top of the map area.

## Rationale
- **Usability**: Keeping filters in the sidebar is a native Streamlit pattern that users find intuitive.
- **Immersion**: Occupying the rest of the viewport with the map maintains the "Maps-First" priority.
- **Aesthetics**: Floating overlays (Glassmorphism) allow data to be visible without creating a "boxy" or "fragmented" layout, keeping the geographic context persistent.

## Consequences
- **CSS Complexity**: Requires careful targeting of Streamlit's main block container to strip padding while respecting the sidebar width.
- **Responsiveness**: Floating charts must be carefully sized to avoid obscuring markers on smaller screens.
- **Z-Index Management**: Multiple overlay layers (Metrics, Trends, Drawer) must be managed to avoid interaction conflicts.
