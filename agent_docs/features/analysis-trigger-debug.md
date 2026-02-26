# Analysis: Trigger Failure V2

## Symptoms
User reports: "no modal opened" and `Current Query Params: {}`.
This implies the browser did NOT navigate to `?selected_center=...`.

## Potential Causes
1. **JS Execution Blocked**: The `onclick` handler in the Folium Popup might be blocked by CSP or Sandboxing (though Streamlit usually allows scripts).
2. **Race Condition**: `st_folium` captures the click on the map layer, triggers a re-run, and potentially resets the iframe before the JS navigation completes.
3. **Invalid JS**: `window.parent` might not be the correct reference in deep nesting, though `window.top` is safer.

## Proposed Fix: "The Old Reliable"
Instead of JS `onclick`, we should use a standard HTML Anchor with `target="_top"`.
`<a href="?selected_center=XYZ" target="_top">`

### why `target="_top"`?
- It forces the link to open in the full browser window, replacing the current page.
- It bypasses iframe restrictions (usually).
- It is a standard navigation event, not a script.

### Data Handling
- We must ensure `hc_name_encoded` is correctly quoted. `urllib.parse.quote` is correct.

## Action Plan
1. Modify `map_view.py`: Remove `onclick`, use `href` + `target="_top"`.
2. Modify `main.py`: Ensure `st.query_params` are checked immediately at top of script.
