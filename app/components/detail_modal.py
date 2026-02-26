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
                    width: 675px !important;
                    max-width: 675px !important;
                    min-width: 675px !important;
                }
                div[role="dialog"][aria-modal="true"] > div {
                    width: 675px !important;
                    max-width: 675px !important;
                    min-width: 675px !important;
                }
                div[data-testid="stTabs"] {
                    width: 675px !important;
                    max-width: 675px !important;
                    min-width: 675px !important;
                }
                div[role="dialog"][aria-modal="true"] header {
                    display: flex !important;
                    flex-direction: row !important;
                    align-items: center !important;
                    justify-content: space-between !important;
                }
                h2 {
                    font-size: 1.75rem !important;
                    margin: 0 !important;
                    padding: 0 !important;
                    flex-grow: 1 !important;
                }
                hr {
                    display: none !important;
                }
            </style>
            """,
            unsafe_allow_html=True,
        )

        # --- Header Section (Grid Layout) ---
        latest = center_df.iloc[-1]
        hc_type = latest.get("health_centre_type", "N/A")
        island = latest["island"]

        with st.container(border=True):
            col1, col2, col3 = st.columns([1, 1, 1.8])
            with col1:
                st.markdown(
                    "<div style='margin-bottom: 0.5rem;'>"
                    "<div style='font-size: 0.9rem; color: #6c757d; "
                    "font-weight: 600; text-transform: uppercase; "
                    "letter-spacing: 0.5px;'>📍 Location</div>"
                    "<div style='font-size: 1.1rem; color: #1f2937; "
                    f"margin-top: 0.2rem;'>{island}</div>"
                    "</div>",
                    unsafe_allow_html=True,
                )

            with col2:
                st.markdown(
                    "<div style='margin-bottom: 0.5rem;'>"
                    "<div style='font-size: 0.9rem; color: #6c757d; "
                    "font-weight: 600; text-transform: uppercase; "
                    "letter-spacing: 0.5px;'>🏥 Type</div>"
                    "<div style='font-size: 1.1rem; color: #1f2937; "
                    f"margin-top: 0.2rem;'>{hc_type}</div>"
                    "</div>",
                    unsafe_allow_html=True,
                )

            with col3:
                ha = latest.get("health_assistans")
                mayor = latest.get("mayor")
                staff_info = []
                if pd.notnull(ha):
                    staff_info.append(f"Health Assistant: {ha}")
                if pd.notnull(mayor):
                    staff_info.append(f"Mayor: {mayor}")

                staff_html = "<br>".join(staff_info) if staff_info else "N/A"
                st.markdown(
                    "<div style='margin-bottom: 0.5rem;'>"
                    "<div style='font-size: 0.9rem; color: #6c757d; "
                    "font-weight: 600; text-transform: uppercase; "
                    "letter-spacing: 0.5px;'>👥 Personnel</div>"
                    "<div style='font-size: 1.0rem; color: #1f2937; "
                    "margin-top: 0.2rem; line-height: 1.4;'>"
                    f"{staff_html}</div>"
                    "</div>",
                    unsafe_allow_html=True,
                )

        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown("<br>", unsafe_allow_html=True)
        # --- Tabs for Content ---
        tab_overview, tab_history = st.tabs(
            ["📊 Overview & Trends", "📜 Historical Data"]
        )

        with tab_overview:
            # Metrics
            latest_score = latest["score"]
            prev_score = center_df.iloc[-2]["score"] if len(center_df) > 1 else None

            m_col1, m_col2 = st.columns(2)
            with m_col1:
                with st.container(border=True, height=125):
                    st.markdown(
                        "<div style='display: flex; flex-direction: column; "
                        "justify-content: center; align-items: center; "
                        "height: 90px;'>"
                        "<div style='font-size: 1.1rem; color: #6c757d; "
                        "font-weight: 600; margin-bottom: 0.2rem;'>"
                        "Latest Score</div>"
                        "<div style='font-size: 2.2rem; color: #1f2937; "
                        f"font-weight: 700;'>{latest_score:.1f}</div>"
                        "</div>",
                        unsafe_allow_html=True,
                    )
            with m_col2:
                with st.container(border=True, height=125):
                    if prev_score is not None:
                        delta = latest_score - prev_score
                        color = (
                            "#10b981"
                            if delta > 0
                            else "#ef4444" if delta < 0 else "#6b7280"
                        )
                        st.markdown(
                            "<div style='display: flex; "
                            "flex-direction: column; "
                            "justify-content: center; align-items: center; "
                            "height: 90px;'>"
                            "<div style='font-size: 1.1rem; color: #6c757d; "
                            "font-weight: 600; margin-bottom: 0.2rem;'>"
                            "Trend</div>"
                            f"<div style='font-size: 2.2rem; color: {color}; "
                            f"font-weight: 700;'>{delta:+.1f}</div>"
                            "</div>",
                            unsafe_allow_html=True,
                        )
                    else:
                        st.markdown(
                            "<div style='display: flex; "
                            "flex-direction: column; "
                            "justify-content: center; align-items: center; "
                            "height: 90px;'>"
                            "<div style='font-size: 1.1rem; color: #6c757d; "
                            "font-weight: 600; margin-bottom: 0.2rem;'>"
                            "Trend</div>"
                            "<div style='font-size: 2.2rem; color: #6b7280; "
                            "font-weight: 700;'>N/A</div>"
                            "</div>",
                            unsafe_allow_html=True,
                        )

            st.markdown("#### Performance Trend")
            render_trend_chart(center_df)

        with tab_history:
            st.markdown("#### Detailed Logs")
            st.dataframe(
                center_df[["date", "score", "health_assistans", "mayor"]].rename(
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
            # Clear query params to prevent URL re-trigger
            st.query_params.pop("selected_center", None)
            st.rerun()
