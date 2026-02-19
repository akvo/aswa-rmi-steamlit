# Architecture Design: RMI Health Dashboard (PoC)

## 1. System Overview
The **RMI Health Dashboard** is a Streamlit-based geospatial analytics application. It uses a "Hybrid" architecture where the map is the primary interface (using `folium` / `leaflet`), supported by a persistent sidebar for filtering and an integrated analytics section for deep dives.

## 2. Component Hierarchy

```mermaid
graph TD
    A[Main App: main.py] --> B[Sidebar: components/filters.py]
    A --> C[Map View: components/map_view.py]
    A --> D[Floating UI: components/floating_widgets.py]
    A --> E[Detail Modal: components/detail_modal.py]
    C --> F[Folium Map Layer]
    C --> G[Markers & Popups]
    D --> H[Floating Metrics (Top Left)]
    D --> I[Integrated Trends (Bottom Page)]
```

### 2.1 Core Components
- **Sidebar (`filters.py`)**: Persistent filtering by Island and Type. Changes update `filtered_df`.
- **Map View (`map_view.py`)**: Renders OpenStreetMap with color-coded markers. Handles Popup generation.
- **Floating Widgets (`floating_widgets.py`)**:
    - `render_floating_metrics`: Displays high-level stats (Total Centers, Avg Score) over the map.
    - `render_floating_analytics_tray`: Renders the national trend chart at the bottom of the page.
- **Detail Modal (`detail_modal.py`)**: A centered modal overlay (via `@st.dialog`) that appears when `st.session_state.detail_center` is set. It shows facility-specific history and analytics.

## 3. Data Flow & State Management

### 3.1 Data Pipeline
1. **Load**: `utils/data_loader.py` reads `RMI_OUTPUT.csv`.
2. **Cache**: Data is cached via `@st.cache_data` to ensure speed.
3. **Filter**: `main.py` applies Sidebar selection -> produces `filtered_df`.
4. **Render**: `filtered_df` is passed to Map, Metrics, and Analytics Tray.

### 3.2 Interaction State
- `st.query_params.selected_center`: The primary entrance for direct drawer navigation from the map popup.
- `st.session_state.detail_center`: Set either by query params or internal logic. Triggers the **Detail Modal** to open.
- `st.session_state.preview_center`: (Legacy/Fallback) Set when a user clicks a marker to track the active popup.

## 4. UI/UX Specifications
- **Theme**: Light Mode "Professional".
- **Design System**:
    - **Teal (#0d9488)**: Primary accents, headers.
    - **Slate (#475569)**: Text, secondary elements.
    - **White/Frosted**: Backgrounds to ensure readability on top of the map.
- **CSS Injection**: `utils/style_utils.py` handles advanced styling (removing padding, glassmorphism, drawer animations).

## 5. Deployment
- **Docker**: Containerized via `./dc.sh` and `docker-compose.yml`.
- **Local Run**: `streamlit run app/main.py`.
