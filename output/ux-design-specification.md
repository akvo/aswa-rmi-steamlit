# UX Design Specification: Detail Modal

## 1. Interaction Pattern
The transition from map marker to detail view follows a "Focused Drill-down" pattern.
1. **Trigger**: User clicks "View Details" in the marker popup.
2. **Transition**: The page reloads (standard Streamlit behavior for query params) and the map is overlaid with a centered modal.
3. **Escapability**: The modal can be closed via the "X" button, ESC key, or a prominent "Close" button at the bottom.

## 2. Visual Layout (st.dialog "large")
- **Header**: Large Teal Title (`#0d9488`) with the Health Center Name.
- **Top Row**: Glassmorphism metrics for "Latest Score" and "Trend".
- **Body**:
    - **Comparative Analytics**: A wide-format chart for historical trends.
    - **Historical Log**: A clean data table for reference.
- **Footer**: A secondary "Close" button for convenience.

## 3. Design Tokens
- **Backdrop**: Semi-transparent slate (`rgba(15, 23, 42, 0.4)`) with high blur to maintain spatial context while focusing the modal.
- **Borders**: Subtle teal accents (`#99f6e4`) to match the medical theme.
- **Typography**: Inter (sans-serif) for high legibility.

## 4. Accessibility
- Keyboard support (ESC to close) is handled natively by `st.dialog`.
- High contrast ratios for metric text.
