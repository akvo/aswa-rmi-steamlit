import streamlit as st
from components.charts import render_trend_chart


def render_floating_metrics(total_centers, avg_score, missing_geo):
    """
    Renders top-left floating glassmorphism metrics.
    """
    st.markdown(
        f"""
        <div style="position: fixed; top: 1.5rem; right: 1.5rem; z-index: 500;
                    display: flex; gap: 1rem; pointer-events: none;">
            <div class="glass-overlay"
                 style="pointer-events: auto;
                        border-left: 5px solid #0d9488;">
                <div class="metric-label">Centers</div>
                <div style="font-size: 1.75rem; font-weight: 600;">
                    {total_centers}
                </div>
            </div>
            <div class="glass-overlay"
                 style="pointer-events: auto;
                        border-left: 5px solid #0d9488;">
                <div class="metric-label">Global Avg</div>
                <div style="font-size: 1.75rem; font-weight: 600;
                            color: #0d9488;">
                    {avg_score:.1f}
                </div>
            </div>
             <div class="glass-overlay"
                  style="pointer-events: auto;
                         border-left: 5px solid #e11d48;">
                <div class="metric-label">Missing Geo</div>
                <div style="font-size: 1.75rem; font-weight: 600;
                            color: #e11d48;">
                    {missing_geo}
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_floating_analytics_tray(df):
    """
    Renders a persistent bottom-floating tray for trend charts.
    """
    # Simply render the tray without any toggle logic
    # Use columns to create padding (1:10:1 ratio approximates padding)
    _, col, _ = st.columns([0.05, 0.9, 0.05])

    with col:
        st.markdown(
            "<div>"
            '<h3 style="margin-top:0; color:#0d9488; font-size:1.1rem;">'
            "National Performance Trends</h3>",
            unsafe_allow_html=True,
        )
        render_trend_chart(df)
        st.markdown("</div>", unsafe_allow_html=True)
