import streamlit as st
import pandas as pd
from components.charts import render_trend_chart


def render_detail_drawer(df: pd.DataFrame, center_name: str):
    """
    Renders a floating side drawer with details for the selected health center.
    """
    if not center_name:
        return

    # Filter data for this specific center
    center_df = df[df["healt_centre"] == center_name].sort_values("date")

    if center_df.empty:
        return

    # Use a container with a custom key for CSS targeting if needed,
    # but here we use the fixed position div via inject_drawer_css

    st.markdown(
        f"""
        <div class="detail-drawer">
            <div style="display: flex; justify-content: space-between; align-items: start; margin-bottom: 1.5rem;">
                <h2 style="margin: 0; color: #0d9488; font-size: 1.8rem;">{center_name}</h2>
            </div>
            <div style="background: #f8fafc; padding: 1.25rem; border: 1px solid #e2e8f0;
                        border-radius: 12px; margin-bottom: 2rem;">
                <p style="margin: 0 0 0.5rem 0; font-size: 0.95rem; color: #475569; display: flex; justify-content: space-between;">
                    <strong>Island:</strong> <span>{center_df.iloc[-1]['island']}</span>
                </p>
                <p style="margin: 0; font-size: 0.95rem; color: #475569; display: flex; justify-content: space-between;">
                    <strong>Type:</strong> <span>{center_df.iloc[-1].get('health_centre_type', 'N/A')}</span>
                </p>
            </div>
    """,
        unsafe_allow_html=True,
    )

    # Metrics
    latest_score = center_df.iloc[-1]["score"]
    prev_score = center_df.iloc[-2]["score"] if len(center_df) > 1 else None

    m_col1, m_col2 = st.columns(2)
    with m_col1:
        st.metric("Latest Score", f"{latest_score:.1f}")
    with m_col2:
        if prev_score is not None:
            delta = latest_score - prev_score
            st.metric("Trend", f"{delta:+.1f}", delta_color="normal")

    st.markdown(
        "<h4 style='color: #1e293b; margin-top: 2rem; border-bottom: 2px solid #e2e8f0; padding-bottom: 0.5rem;'>Comparative Analytics</h4>",
        unsafe_allow_html=True,
    )
    # Re-use existing trend chart logic but filtered
    render_trend_chart(center_df)

    st.markdown(
        "<h4 style='color: #1e293b; margin-top: 2rem; border-bottom: 2px solid #e2e8f0; padding-bottom: 0.5rem;'>Historical Log</h4>",
        unsafe_allow_html=True,
    )
    st.dataframe(
        center_df[["date", "score"]].rename(
            columns={"date": "Date", "score": "Score"}
        ),
        use_container_width=True,
        hide_index=True,
    )

    st.markdown("<br>", unsafe_allow_html=True)
    if st.button(
        "Close Drawer", key="close_drawer_btn", use_container_width=True
    ):
        st.session_state.selected_center = None
        st.rerun()

    st.markdown("</div>", unsafe_allow_html=True)
