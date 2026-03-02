# User Stories: Map Persistence

## Story 1: Stable Map Key Implementation [x]
**As a** Developer
**I want to** use a fixed key for the map component
**So that** Streamlit does not destroy the companion when the state changes.

**Acceptance Criteria:**
- [x] `map_version` is removed.
- [x] `render_map` is called with `key="health_map_main"`.
- [x] Opening a modal does not cause the map background to flicker.

## Story 2: Preserving Interaction State [x]
**As a** User
**I want** my map zoom and center to be preserved after I close a detail modal
**So that** I don't lose my context and have to re-find the markers.

**Acceptance Criteria:**
- [x] `st.session_state.map_center` and `st.session_state.map_zoom` are updated before modal close.
- [x] The map returns to the exact same state after closing.

## Story 3: marker selection Reset Logic [x]
**As a** Developer
**I want** to ensure closing a modal doesn't immediately re-open it due to persistent selection
**So that** the user experience remains predictable.

**Acceptance Criteria:**
- [x] `ignored_center` logic is verified and optimized.
- [x] Closing the modal resets `detail_center` in session state.

## Story 4: Return to Map Center [x]
**As a** User
**I want** a dedicated button to return the map to its default center and zoom level
**So that** I can easily view the entire country again after inspecting specific islands or markers.

**Acceptance Criteria:**
- [x] A "Return to Center" button is added to the UI (inside map).
- [x] Clicking the button resets to default values.

## Story 5: Non-Blocking Map Rendering [x]
**As a** User on a slow connection
**I want** the basic map and interface to load immediately before the hundreds of markers finish processing
**So that** I don't stare at a blank screen while the backend iterates through the geolocation data.

**Acceptance Criteria:**
- [x] A visual indicator (like `st.spinner`) informs the user.
- [x] Advanced Streamlit components like `st.fragment` isolate the map drawing.
