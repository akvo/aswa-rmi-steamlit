import os
import sys
import streamlit as st
import urllib.parse

# Add the current directory to sys.path
sys.path.append(os.path.dirname(__file__))

# Local imports
from utils.data_loader import (  # noqa: E402
    load_data,
    get_map_data,
    get_missing_geodata_count,
)
from utils.style_utils import inject_full_screen_css  # noqa: E402
from components.filters import render_sidebar  # noqa: E402
from components.map_view import render_map  # noqa: E402
from components.detail_modal import render_detail_modal  # noqa: E402
from streamlit_modal import Modal  # noqa: E402
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

    # Initialize State
    if "detail_center" not in st.session_state:
        st.session_state.detail_center = None
    if "last_clicked_center" not in st.session_state:
        st.session_state.last_clicked_center = None
    if "ignored_center" not in st.session_state:
        st.session_state.ignored_center = None
    if "map_center" not in st.session_state:
        st.session_state.map_center = None
    if "map_zoom" not in st.session_state:
        st.session_state.map_zoom = 6
    if "rerun_count" not in st.session_state:
        st.session_state.rerun_count = 0
    # st.session_state.rerun_count += 1

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

    # 1. Sync Query Params to State (Direct Navigation)
    query_params = st.query_params.to_dict()
    query_center_raw = query_params.get("selected_center")

    if query_center_raw:
        query_center = urllib.parse.unquote(query_center_raw)
        if query_center != st.session_state.detail_center:
            st.session_state.detail_center = query_center
            # Force modal open for URL triggers
            Modal(
                title=f"Details: {query_center}",
                key=f"modal_{query_center}",
            ).open()
            st.rerun()

    # 2. Map Layer
    @st.fragment
    def render_map_layer():
        map_df = get_map_data(filtered_df)
        map_key = "health_map_main"

        with st.spinner("Loading health center locations..."):
            map_data = render_map(
                map_df,
                key=map_key,
                center=st.session_state.map_center,
                zoom=st.session_state.map_zoom,
            )

        # Capture map state for persistence across version resets
        if map_data:
            if "center" in map_data:
                st.session_state.map_center = [
                    map_data["center"]["lat"],
                    map_data["center"]["lng"],
                ]
            if "zoom" in map_data:
                st.session_state.map_zoom = map_data["zoom"]

        # 3. Handle Marker Clicks (Direct Interaction)
        if map_data and map_data.get("last_object_clicked_tooltip"):
            clicked_name = map_data["last_object_clicked_tooltip"]

            # Only open if it's NOT what we just closed and NOT already open
            if clicked_name == st.session_state.get("ignored_center"):
                pass
            elif clicked_name != st.session_state.get("detail_center"):
                st.session_state.detail_center = clicked_name
                st.session_state.last_clicked_center = clicked_name
                st.session_state.ignored_center = None
                # Force modal open for Click triggers
                Modal(
                    title=f"Details: {clicked_name}",
                    key=f"modal_{clicked_name}",
                ).open()
                st.rerun()

        if map_data and map_data.get("last_clicked"):
            # If the user interacts with the map (clicks anything), we check
            # if they clicked the background. If so, we can clear the ignored
            # state so they can re-click the marker. It's not perfect
            # (doesn't fix double-clicking exactly), but it helps.

            # If they close the modal, and then click the marker again, the
            # ONLY THING that happens is browser thinks the tooltip is the same
            pass
        else:
            st.session_state.ignored_center = None
            st.session_state.last_clicked_center = None

    # Call the fragment
    render_map_layer()

    # Fragment ends here

    # --- DEBUG DASHBOARD (Commented out for production) ---
    # with st.expander("🔍 Debugging: State & Map Data", expanded=False):
    #     st.write("detail_center:", st.session_state.get("detail_center"))
    #     st.write("ignored_center:", st.session_state.get("ignored_center"))
    #     st.write("map_key:", map_key)
    #     st.write(
    #         "map_data (last click):",
    #         map_data.get("last_clicked") if map_data else None,
    #     )
    #     st.write("Rerun Count:", st.session_state.rerun_count)
    # -----------------------

    # Floating UI Layer (Metrics overlay the map)
    render_floating_metrics(total_centers, avg_score, missing_geo)

    # Persistent Analytics Layer (Integrated flow at bottom)
    st.markdown("<br><br>", unsafe_allow_html=True)
    render_floating_analytics_tray(filtered_df)

    # Detail Modal Overlay
    if st.session_state.detail_center:
        render_detail_modal(filtered_df, st.session_state.detail_center)


if __name__ == "__main__":
    main()
