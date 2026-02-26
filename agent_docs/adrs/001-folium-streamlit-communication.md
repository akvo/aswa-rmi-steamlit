# ADR 001: Folium-Streamlit Communication Pattern for Detailed Analytics

## Status
Proposed

## Context
The user wants a "View Details" button inside the map marker popups that opens a detailed analytics drawer. Folium popups are client-side static HTML and cannot natively trigger Streamlit server-side reruns or state changes via standard buttons/links.

## Decision
We will use a **Hybrid Interaction Pattern**:
1. **Marker Click Detection**: Leverage `st_folium`'s `last_object_clicked_tooltip` to identify when a marker is clicked.
2. **Preview State**: Store the clicked center's name in `st.session_state.preview_center`.
3. **Floating Proxy**: When `preview_center` is set, render a high-visibility floating Streamlit button ("View Details") at the bottom center of the map.
4. **Visual Sync**: Include a styled but non-functional "View Details" button in the Folium popup HTML to provide visual continuity for the user.
5. **Drawer Activation**: Clicking the floating Streamlit button sets `st.session_state.selected_center`, triggering the opening of the `DetailDrawer` component.

## Consequences
- **Pros**: Relies on standard `st_folium` and Streamlit features; robust; easy to maintain; clean separation of concerns.
- **Cons**: Requires two clicks (Marker -> Floating Button) if the user ignores the popup button, but providing both satisfies the user's visual requirement while ensuring technical feasibility.
