# Story: Fix Sidebar Visibility Toggle

**ID**: STORY-740
**Title**: Fix Main Sidebar Re-expansion
**Role**: As a Health Administrator
**Action**: I want to be able to reopen the sidebar after collapsing it
**Value**: So that I can adjust filters and access different views without refreshing the page.

## Acceptance Criteria
- [ ] When the sidebar is collapsed, a toggle button (e.g., ">") is visible in the top left corner.
- [ ] Clicking the toggle button re-expands the sidebar.
- [ ] The rest of the Streamlit header (Deploy button, etc.) remains hidden to maintain a clean UI.
- [ ] The fix works across different screen sizes.

## Technical Notes
- Current `header {visibility: hidden;}` in `app/utils/style_utils.py` is too aggressive.
- Use targeted CSS to allow only the sidebar collapse button to be visible.
