import altair as alt
import pandas as pd
import streamlit as st


def render_trend_chart(df: pd.DataFrame):
    """
    Renders a time-series line chart for health center scores.
    """
    if df.empty:
        st.info("No data available for charting.")
        return

    # Ensure we have valid dates for Altair
    df = df.dropna(subset=["date"])
    if df.empty:
        st.info("No valid date records found for charting.")
        return

    st.markdown(
        f"""
        <div style="font-size: 0.9rem; opacity: 0.8;
                    margin-bottom: 1rem; color: #94a3b8;">
            Analyzing performance across {len(df)} records.
        </div>
        """,
        unsafe_allow_html=True,
    )

    tab1, tab2 = st.tabs(["Average Trend", "Individual Trends"])

    with tab1:
        # Aggregate data by date to get average score
        agg_df = df.groupby("date", as_index=False)["score"].mean()

        # Base chart
        base = (
            alt.Chart(agg_df)
            .encode(
                x=alt.X(
                    "date:T",
                    title="",
                    axis=alt.Axis(
                        format="%b %Y",
                        labelColor="#475569",
                        gridColor="#e2e8f0",
                    ),
                    scale=alt.Scale(nice=True),
                ),
                y=alt.Y(
                    "score:Q",
                    title="Avg Score",
                    scale=alt.Scale(domain=[0, 100], nice=True),
                    axis=alt.Axis(labelColor="#475569", gridColor="#e2e8f0"),
                ),
                tooltip=[
                    alt.Tooltip("date:T", title="Date", format="%b %Y"),
                    alt.Tooltip("score:Q", title="Avg Score", format=".1f"),
                ],
            )
            .properties(height=300)
        )

        # Smooth Area + Line (Medical Teal)
        line = base.mark_line(
            interpolate="monotone", strokeWidth=4, color="#0d9488"
        )
        area = base.mark_area(
            interpolate="monotone",
            opacity=0.15,
            color=alt.Gradient(
                gradient="linear",
                stops=[
                    alt.GradientStop(color="#0d9488", offset=0),
                    alt.GradientStop(color="transparent", offset=1),
                ],
                x1=1,
                x2=1,
                y1=1,
                y2=0,
            ),
        )

        # Points
        points = base.mark_circle(
            size=80, color="#0d9488", stroke="white", strokeWidth=2
        )

        chart_agg = (area + line + points).interactive()
        st.altair_chart(chart_agg, use_container_width=True)

    with tab2:
        # Individual lines for each center
        chart_ind = (
            alt.Chart(df)
            .mark_line(point=True, strokeWidth=2)
            .encode(
                x=alt.X(
                    "date:T",
                    title="",
                    axis=alt.Axis(
                        format="%b %Y",
                        labelColor="#475569",
                        gridColor="#e2e8f0",
                    ),
                    scale=alt.Scale(nice=True),
                ),
                y=alt.Y(
                    "score:Q",
                    title="Score",
                    scale=alt.Scale(domain=[0, 100], nice=True),
                    axis=alt.Axis(labelColor="#475569", gridColor="#e2e8f0"),
                ),
                color=alt.Color(
                    "healt_centre:N",
                    title="Health Centre",
                    scale=alt.Scale(scheme="viridis"),
                ),
                tooltip=[
                    "date",
                    "healt_centre",
                    "score",
                    "island",
                    "health_centre_type",
                ],
            )
            .properties(height=300)
            .interactive()
        )
        st.altair_chart(chart_ind, use_container_width=True)
