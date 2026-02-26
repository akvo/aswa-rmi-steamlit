# Research Findings: Direct Modal Trigger from Folium

## Context
The user wants the "View Details" button inside the Folium marker popup to "directly" trigger the modal.

## Problem Analysis
1. **Iframe Isolation**: Folium popups are rendered in an iframe (`target="_top"` or `target="_parent"` is needed to reach the Streamlit URL).
2. **State Reset on Reload**: When using `target="_top"`, the Streamlit app reloads. If the query parameter is present, it should work.
3. **Mismatched Expectations**: The user might expect the modal to open *without* a page reload. This is only possible if we use a Streamlit component that listens for JavaScript events from the map.
4. **Current failure**: The previous attempt showed empty query params in the debug dashboard. This suggests either:
   - The link click is being intercepted or blocked by the browser.
   - The reload is losing the query parameter because of some reroute logic.

## Proposed Strategy: "The Hybrid Directness"
1. **Refined Link**: Use a standard `<a>` tag with `target="_self"` (if `st_folium` supports it) or rely on `st_folium`'s returned objects.
2. **Session State Persistence**: Ensure that once `detail_center` is set via query params, it is NOT cleared immediately but handled by the modal's internal close logic.
3. **Alternative**: If the link approach remains flaky, we will move the "View Details" button *outside* the popup but make it so prominent (pulsing or sticky) that it feels like a single interaction flow. **However**, the requirement specifically asks for the button *inside* the marker.

## Recommendation
We will re-implement the query parameter sync but REMOVE the `st.query_params.clear()` line. Clearing it immediately might be triggering a second rerun that wipes the state before the modal can render.
