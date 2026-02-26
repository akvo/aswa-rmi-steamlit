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
