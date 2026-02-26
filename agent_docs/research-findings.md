# Research Findings: Map Marker "View Details"

## Folium-Streamlit Interaction
Folium popups are rendered as static HTML on the client side. `st_folium` provides bi-directional communication, but only for certain events (map clicks, marker clicks, zoom, etc.).

### Findings
1. **Popup Limitations**: Standard Folium popups cannot execute Python code or directly trigger Streamlit reruns via HTML buttons/links without complex JavaScript bridges.
2. **Marker Click Event**: `st_folium` consistently returns the `last_object_clicked_tooltip` (Health Centre Name) when a marker is clicked.
3. **State Management**: We can leverage `st.session_state` to track the "previewed" facility vs the "selected" (drawer open) facility.

### Proposed Strategy (Hybrid Approach)
To satisfy the user's request for a button "there" while ensuring functionality:
1. **Visual Guide**: Include a styled "View Details" element in the Folium popup.
2. **Immediate Action**: When a marker is clicked, the `st_folium` component notifies the backend.
3. **Floating Trigger**: A prominent, styled floating button (using Streamlit's `st.button`) will appear at the bottom of the map when a facility is "previewed" (i.e., its popup is open).
4. **Transition**: Clicking this floating button will set `st.session_state.selected_center`, which opens the existing `DetailDrawer`.

### Chart Integration
The chart for the selected marker is already implemented in `components/detail_drawer.py`. By opening the drawer, we fulfill the requirement to "show the chart of selected marker".
