# PRD: Map Persistence & Marker Loading Optimization

## 1. Requirement Overview
The application must maintain the base map layer when opening and closing the detail modal. Marker updates should be non-blocking or show a clear loading indicator without destroying the map instance.

## 2. User Stories
| ID | User Story | Acceptance Criteria |
|----|------------|---------------------|
| US.1 | As a user, I want the map to stay visible when I open a modal. | Map background does not flicker or turn white. |
| US.2 | As a user, I want markers to load asynchronously. | Spinner is localized to markers/info area, not the whole map. |
| US.3 | As a user, I want the map zoom and center to be preserved. | Interaction with modal does not reset map view. |

## 3. Technical Constraints
- The solution must work within the constraints of `streamlit-folium`.
- Marker selection must still be clearable to allow re-clicking.
- Must perform well on 4G connections.

## 4. Functional Requirements
- **FR.1 Stable Map Component**: Use a static key for `st_folium`.
- **FR.2 State Management**: Move map state capture to a more robust mechanism.
- **FR.3 Loading Indicators**: Implement `st.empty()` or `st.spinner` in a way that doesn't obscure the base map.
