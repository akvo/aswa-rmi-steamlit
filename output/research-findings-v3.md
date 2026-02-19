# Research Findings: Modal Implementation in Streamlit

## Research Objective
Identify the most robust and standard way to implement a "Detail Modal" in a Streamlit application (v1.54.0).

## Findings

### 1. `st_dialog` (Native) vs `streamlit-modal` (Community)
- **`st.dialog`**: Added in Streamlit 1.34.0. It is a native decorator that transforms a function into a modal dialog.
    - **Pros**: Zero dependencies, native state management integration, high performance, mobile responsive.
    - **Cons**: None for our use case.
- **`streamlit-modal`**: A community component.
    - **Pros**: Established.
    - **Cons**: Requires additional package installation, might have slight lag compared to native, potentially less stable across Streamlit upgrades.

### 2. Native Dialog Capabilities
- **Size Options**: `small` (500px), `medium` (750px), `large` (1280px).
- **Control**: Handles its own lifecycle; content is just standard Streamlit code.
- **Dismissal**: Supports "X" button, ESC key, and clicking outside.

## Actionable Recommendation
Use the native **`st.dialog`** component. It aligns perfectly with our PRD requirements (FR-07, FR-08, FR-09) and eliminates the need for external libraries or custom CSS hacks used in the previous drawer implementation.

## PRD Hardening Requirements
- **AR-01**: The detail view logic must be encapsulated in a function decorated with `@st.dialog`.
- **AR-02**: The dialog width should be set to `large` to accommodate the comparative analytics charts.
- **AR-03**: State transition from Map Click -> Dialog Trigger must be handled via `st.session_state`.
