# Research Findings: Hardening the Direct Trigger

## Problem
The user reports that clicking the "View Details" link doesn't open the modal directly but instead seems to lead them to the secondary "Open full analysis" button. This implies the page reload (via JS) is NOT happening, or it's happening but the query parameter isn't being picked up before the secondary UI renders.

## Root Cause Hypotheses
1. **JS Syntax Error**: The multi-line `onclick` string in Python f-string might be rendering invalid JS.
2. **Event Cancellation**: `return false;` might be stopping the link AND the JS? No, that's standard.
3. **Iframe Isolation**: `window.parent` might be restricted in some Docker/Streamlit network setups (Cross-Origin), though unlikely on localhost.
4. **Race Condition**: `st_folium` might be triggering a Python-side rerun (updating `last_object_clicked`) *simultaneously* with the JS click. If the Python rerun finishes first and renders the "Secondary Trigger" UI, the user sees that.

## Solution Strategy
1. **Simplify JS**: Use valid, single-line JS or `target="_parent"` with a robust URL.
   - *Actually, `target="_top"` was tried and supposedly fixed it, but maybe not?*
2. **Remove Secondary UI**: If the goal is directness, **DELETE** the secondary trigger entirely. If the link fails, it fails, but the secondary UI is confusing the user ("that wil show another div").
3. **Hybrid Trigger**:
   - Keep the URL param logic.
   - ALSO, in `main.py`, if `st_folium` returns a clicked object (`last_object_clicked_tooltip`), **automatically** promote it to `detail_center` if the user just clicked it.
   - *Risk*: Clicking a marker to *just* see the popup would open the modal. This might be too aggressive.
   - *Correction*: The user said "WHEN CLICK VIEW DETAILS". So they want the popup first, *then* the link.

## Plan
1. **Remove Secondary UI**: It is a distraction.
2. **Fix JS Link**: Ensure the JS is absolutely correct. Use `window.top.location.href` to be sure.
3. **Fallback**: If JS fails, `target="_top"` with `href` is better. We will set BOTH `href` and `onclick`.
