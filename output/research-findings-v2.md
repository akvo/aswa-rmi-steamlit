# Research Findings v2: Direct Popup-to-Drawer Interaction

## Analysis
The previously implemented "Hybrid" pattern (Popup -> Floating Button -> Drawer) was deemed redundant by the user. They require a single-click transition from the popup button to the analytics drawer.

## Implementation Options

### 1. Query Parameters (Recommended)
- **Mechanism**: The "View Details" button in the Folium popup becomes an `<a>` tag pointing to `/?selected_center=CenterName`.
- **Target**: `target="_parent"` ensures the whole Streamlit application handles the link.
- **Handling**: `st.query_params` in `main.py` detects the parameter on reload and sets `st.session_state.selected_center`.
- **Pros**: Direct, standard web behavior, functional within static HTML popups.
- **Cons**: Triggers a page reload (though Streamlit stays in session).

### 2. Auto-Open on Marker Click
- **Mechanism**: Whenever `st_folium` returns a `last_object_clicked_tooltip`, automatically set `selected_center`.
- **Pros**: Immediate transition.
- **Cons**: Bypasses the popup entirely; may be unexpected if the user just wants quick info. *Not recommended as the user specifically asked for the button in the popup to be the trigger.*

## Selected Approach
We will proceed with **Option 1 (Query Parameters)** to maintain the requested visual "View Details" button in the popup while making it functionally direct.
