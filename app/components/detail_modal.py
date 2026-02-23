import streamlit as st
import pandas as pd
from components.charts import render_trend_chart
from streamlit_modal import Modal


def render_detail_modal(df: pd.DataFrame, center_name: str):
    """
    Renders a centered modal dialog using streamlit-modal.
    """
    if not center_name:
        return

    # Initialize Modal
    modal = Modal(title=f"Details: {center_name}", key=f"modal_{center_name}")

    # Use session state to control modal visibility if needed,
    # but here we trigger it based on detail_center state from main.py

    # In streamlit-modal, it usually opens if we enter its container block
    # However, it also has an open() method and is_open() check.
    # To integrate with our existing main.py logic:
    if not modal.is_open():
        # Mark current as ignored to prevent immediate re-open by map loop
        if st.session_state.get("detail_center"):
            st.session_state.ignored_center = st.session_state.detail_center
        st.session_state.detail_center = None
        # Increment map version to clear selection in Folium
        st.session_state.map_version += 1
        # Clear query params to prevent URL re-trigger
        st.query_params.pop("selected_center", None)
        st.rerun()

    with modal.container():
        # Filter data for this specific center
        center_df = df[df["healt_centre"] == center_name].sort_values("date")

        if center_df.empty:
            st.warning(f"No data found for {center_name}")
            return

        # Custom CSS for Modal Width & Styling
        st.markdown(
            """
            <style>
                div[data-testid="stMarkdownContainer"] p {
                    font-size: 1rem;
                }
                div[role="dialog"][aria-modal="true"] {
                    width: 850px !important;
                    max-width: 850px !important;
                    min-width: 850px !important;
                }
                div[role="dialog"][aria-modal="true"] > div {
                    width: 850px !important;
                    max-width: 850px !important;
                    min-width: 850px !important;
                }
                div[data-testid="stTabs"] {
                    width: 850px !important;
                    max-width: 850px !important;
                    min-width: 850px !important;
                }
            </style>
            """,
            unsafe_allow_html=True,
        )

        # --- Header Section (Grid Layout) ---
        latest = center_df.iloc[-1]
        hc_type = latest.get("health_centre_type", "N/A")
        island = latest["island"]

        st.markdown(f"### {center_name}")

        col1, col2, col3 = st.columns(3)
        with col1:
            st.markdown("**📍 Location**")
            st.caption(f"{island}")

        with col2:
            st.markdown("**Type**")
            st.caption(f"{hc_type}")

        with col3:
            st.markdown("**Personnel**")
            ha = latest.get("health_assistans")
            mayor = latest.get("mayor")
            staff_info = []
            if pd.notnull(ha):
                staff_info.append(f"HA: {ha}")
            if pd.notnull(mayor):
                staff_info.append(f"Mayor: {mayor}")

            st.caption(
                "<br>".join(staff_info) if staff_info else "N/A",
                unsafe_allow_html=True,
            )

        st.divider()

        # --- Tabs for Content ---
        tab_overview, tab_history = st.tabs(
            ["📊 Overview & Trends", "📜 Historical Data"]
        )

        with tab_overview:
            # Metrics
            latest_score = latest["score"]
            prev_score = (
                center_df.iloc[-2]["score"] if len(center_df) > 1 else None
            )

            m_col1, m_col2 = st.columns(2)
            with m_col1:
                st.metric("Latest Score", f"{latest_score:.1f}")
            with m_col2:
                if prev_score is not None:
                    delta = latest_score - prev_score
                    st.metric("Trend", f"{delta:+.1f}", delta_color="normal")

            st.markdown("#### Performance Trend")
            render_trend_chart(center_df)

        with tab_history:
            st.markdown("#### Detailed Logs")
            st.dataframe(
                center_df[
                    ["date", "score", "health_assistans", "mayor"]
                ].rename(
                    columns={
                        "date": "Date",
                        "score": "Score",
                        "health_assistans": "Health Assistant",
                        "mayor": "Mayor",
                    }
                ),
                use_container_width=True,
                hide_index=True,
            )

        st.markdown("<br>", unsafe_allow_html=True)
        if st.button(
            "Close Details",
            key=f"close_modal_{center_name}",
            use_container_width=True,
        ):
            st.session_state.ignored_center = center_name
            st.session_state.detail_center = None
            # Increment map version to clear selection in Folium
            st.session_state.map_version += 1
            # Clear query params to prevent URL re-trigger
            st.query_params.pop("selected_center", None)
            st.rerun()
