# ADR 002: Direct Navigation via Query Parameters

## Status
Proposed

## Context
The "Hybrid" button approach was deemed redundant. The user wants the Folium popup button to act as the direct trigger for the Detail Drawer.

## Decision
We will use **URL Query Parameters** to bridge the client-side Folium popup and the server-side Streamlit state:
1.  **Popup Link**: The "View Details" button in `map_view.py` will be an `<a>` tag with `href="/?selected_center={center_name}"` and `target="_parent"`.
2.  **State Synchronization**: `main.py` will use `st.query_params.get("selected_center")` on initialization to set `st.session_state.selected_center`.
3.  **Removal of Floating Proxy**: The floating activation button and its associated logic in `main.py` and `style_utils.py` will be removed.

## Consequences
- **Pros**: Matches user expectation of "direct" click; robust across reloads; removes UI clutter.
- **Cons**: Causes a page-level rerun (standard in Streamlit).
