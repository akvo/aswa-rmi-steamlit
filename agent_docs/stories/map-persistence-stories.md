# User Stories: Map Persistence

## Story 1: Stable Map Key Implementation
**As a** Developer
**I want to** use a fixed key for the map component
**So that** Streamlit does not destroy the companion when the state changes.

**Acceptance Criteria:**
- `map_version` is removed from `main.py` if no longer needed for other logic.
- `render_map` is called with `key="health_map_main"`.
- Opening a modal does not cause the map background to flicker.

## Story 2: Preserving Interaction State
**As a** User
**I want** my map zoom and center to be preserved after I close a detail modal
**So that** I don't lose my context and have to re-find the markers.

**Acceptance Criteria:**
- `st.session_state.map_center` and `st.session_state.map_zoom` are updated before modal close.
- The map returns to the exact same state after closing.

## Story 3: marker selection Reset Logic
**As a** Developer
**I want** to ensure closing a modal doesn't immediately re-open it due to persistent selection
**So that** the user experience remains predictable.

**Acceptance Criteria:**
- `ignored_center` logic is verified and optimized.
- Closing the modal resets `detail_center` in session state.

## Story 4: Return to Map Center
**As a** User
**I want** a dedicated button to return the map to its default center and zoom level
**So that** I can easily view the entire country again after inspecting specific islands or markers.

**Acceptance Criteria:**
- A "Return to Center" button is added to the UI (e.g., above or inside the floating metrics).
- Clicking the button resets `st.session_state.map_center` and `st.session_state.map_zoom` to `None` or default default values to trigger a Folium recenter.

## Story 5: Non-Blocking Map Rendering
**As a** User on a slow connection
**I want** the basic map and interface to load immediately before the hundreds of markers finish processing
**So that** I don't stare at a blank screen while the backend iterates through the geolocation data.

**Acceptance Criteria:**
- The base map layers (tiles, bounds) render before iterating through the dataframe to add `folium.Marker` objects.
- A visual indicator (like `st.spinner` or a custom toast) informs the user that markers are being placed.
- Advanced Streamlit components like `st.fragment` (or similar asynchronous rendering techniques) are used to isolate the map drawing from the rest of the UI build to unblock the main thread.
