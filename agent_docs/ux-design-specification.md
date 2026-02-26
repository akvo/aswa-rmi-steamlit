# UX Design Specification: Detail Modal & Map Persistence

## 1. Interaction Pattern
The transition from map marker to detail view follows a "Focused Drill-down" pattern.
1. **Trigger**: User clicks a map marker.
2. **Transition**: The map remains visible and interactive in the background. A centered modal overlays the map. **Zero flicker** is achieved by using a stable component key.
3. **Escapability**: The modal can be closed via the "X" button, ESC key, or a prominent "Close" button.
4. **Resumption**: After closing, the user remains at the same map coordinates and zoom level.

## 2. Visual Stability
- **Background Persistence**: The map layer MUST NOT vanish or turn white during transitions.
- **Loading Phase**: If markers need to be recalculated (e.g., after filter change), a localized spinner is shown in the top-right or overlaying the data area, but the map tiles remain.

## 3. Visual Layout (st_modal)
- **Modal Width**: Fixed at 675px for optimal readability on tablet/desktop.
- **Header**: Large Title with the Health Center Name.
- **Information Grid**: Location, Type, and Personnel grouped in a clean card.
- **Tabs**:
    - **Overview**: Latest Score & Trend metrics + Trend Chart.
    - **History**: Detailed data table.

## 4. Accessibility
- Keyboard support (ESC to close).
- High contrast ratios for metric text.
- Map interaction remains possible (panning/zooming) while modal is backgrounded, though focus is on the modal.
