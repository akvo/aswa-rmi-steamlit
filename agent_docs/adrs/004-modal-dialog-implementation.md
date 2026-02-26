# ADR-004: Modal Dialog Implementation for Detail View

- **Status**: Accepted
- **Context**: The previous "Detail Drawer" implementation used custom CSS and HTML hacks to create a slide-out panel that contained Streamlit widgets. This approach was fragile, difficult to style, and broke easily because Streamlit does not natively support wrapping its widgets in raw HTML `div` tags.
- **Decision**: We will replace the custom Detail Drawer with Streamlit's native `@st.dialog` component (available in v1.54.0).
- **Alternatives Considered**:
    - **Custom Drawer (Previous)**: Too fragile, broken.
    - **`streamlit-modal`**: Community component, but `st.dialog` is native and requires no extra dependencies.
- **Consequences**:
    - **Improved Reliability**: Native Streamlit widget support inside the modal.
    - **Simplified Code**: Removal of complex custom CSS in `utils/style_utils.py`.
    - **User Experience**: Transition from a slide-out drawer to a centered modal overlay.
    - **State Management**: Migration to a simpler state trigger for the dialog.
