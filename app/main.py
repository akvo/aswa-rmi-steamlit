import os
import sys
import pandas as pd
import streamlit as st

# Add the current directory to sys.path
sys.path.append(os.path.dirname(__file__))

# Local imports
from utils.data_loader import (  # noqa: E402
    load_data,
    get_map_data,
    get_missing_geodata_count,
)
from utils.style_utils import (  # noqa: E402
    inject_full_screen_css,
    inject_drawer_css,
)
from components.filters import render_sidebar  # noqa: E402
from components.map_view import render_map  # noqa: E402
from components.detail_drawer import render_detail_drawer  # noqa: E402
from components.floating_widgets import (  # noqa: E402
    render_floating_metrics,
    render_floating_analytics_tray,
)

# Page Config
st.set_page_config(
    page_title="RMI Health Dashboard",
    page_icon="🏥",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Constants
DATA_PATH = "transformers/RMI_OUTPUT.csv"


def main():
    # Inject Styles
    inject_full_screen_css()
    inject_drawer_css()

    # Initialize State
    if "selected_center" not in st.session_state:
        st.session_state.selected_center = None
    if "preview_center" not in st.session_state:
        st.session_state.preview_center = None

    # Load Data
    if not os.path.exists(DATA_PATH):
        st.error(f"Data file not found at: {DATA_PATH}.")
        return

    with st.spinner("Loading RMI Health Data..."):
        df = load_data(DATA_PATH)
    if df.empty:
        st.warning("No data loaded.")
        return

    # Sidebar / Filters
    filtered_df = render_sidebar(df)

    # Metrics
    total_centers = filtered_df["healt_centre"].nunique()
    avg_score = filtered_df["score"].mean()
    missing_geo = get_missing_geodata_count(filtered_df)

    # Map Layer
    # Initialize map state
    if "map_initialized" not in st.session_state:
        st.session_state.map_initialized = False

    if not st.session_state.map_initialized:
        # Phase 1: Render empty map to load tiles immediately
        render_map(pd.DataFrame(), allow_empty=True)
        st.session_state.map_initialized = True
        st.rerun()
    else:
        # Phase 2: Render map with data
        map_df = get_map_data(filtered_df)
        with st.spinner("Updating Markers..."):
            map_data = render_map(map_df)

    # Handle Marker Clicks (Preview Mode)
    if map_data and map_data.get("last_object_clicked_tooltip"):
        clicked_name = map_data["last_object_clicked_tooltip"]
        # If a different center is clicked, update preview but
        # don't auto-open drawer
        if clicked_name != st.session_state.get("preview_center"):
            st.session_state.preview_center = clicked_name
            # Optional: Uncomment if we want to auto-close drawer
            # when switching preview
            # st.session_state.selected_center = None
            st.rerun()

    # Floating UI Layer (Metrics overlay the map)
    render_floating_metrics(total_centers, avg_score, missing_geo)

    # Persistent Analytics Layer (Integrated flow at bottom)
    st.markdown("<br><br>", unsafe_allow_html=True)
    render_floating_analytics_tray(filtered_df)

    # Detail Drawer Overlay
    if st.session_state.selected_center:
        render_detail_drawer(filtered_df, st.session_state.selected_center)

    # Preview Interaction (View Details Button)
    # elif st.session_state.preview_center:
    #     # Simple toast-like notification or floating button
    #     _, col, _ = st.columns([0.4, 0.2, 0.4])
    #     with col:
    #         st.info(f"Selected: {st.session_state.preview_center}")
    #         if st.button(
    #             "View Details ➝",
    #             key="view_details_btn",
    #             use_container_width=True,
    #         ):
    #             st.session_state.selected_center = (
    #                 st.session_state.preview_center
    #             )
    #             st.rerun()


if __name__ == "__main__":
    main()
