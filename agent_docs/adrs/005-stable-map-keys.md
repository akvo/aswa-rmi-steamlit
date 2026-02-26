# ADR 005: Stable Map Keys for UI Persistence

## Status
Proposed

## Context
Currently, the application uses a dynamic `map_version` concatenated to the `st_folium` component key. Every time a modal opens or closes, `map_version` is incremented. This was intended to clear the marker selection in Folium. However, changing the key causes Streamlit to destroy and recreate the entire component, leading to a "vanishing map" effect that is especially problematic on slow connections.

## Decision
We will use a stable (fixed) key for the `st_folium` component (`health_map_main`).

## Rationale
- **User Experience**: A stable key prevents the component from unmounting. The browser retains the map tiles and JavaScript state, leading to a much smoother transition when opening and closing overlays.
- **Performance**: On 4G/slow connections, reloading the map component's assets (JS/CSS) introduces a significant delay. A stable key avoids this.
- **State Preservation**: Folium's zoom and center are already being captured. With a stable key, these will be applied as updates rather than a fresh load.

## Consequences
- **Selection Persistence**: The "last click" state in `st_folium` will persist across reruns.
- **Mitigation**: We will handle the selection state in the parent logic using `ignored_center` or periodic state clearing, ensuring that closing a modal doesn't immediately trigger its reopening, while still allowing the user to interact with the map normally.
