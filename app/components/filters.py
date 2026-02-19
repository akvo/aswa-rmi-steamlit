import streamlit as st
import pandas as pd


def render_sidebar(df: pd.DataFrame) -> pd.DataFrame:
    """
    Renders sidebar filters and returns the filtered dataframe.
    """
    st.sidebar.header("Filters")

    if df.empty:
        return df

    # Island Filter
    all_islands = sorted(df["island"].unique().tolist())
    selected_islands = st.sidebar.multiselect(
        "Select Atoll/Island", options=all_islands
    )

    # Health Centre Type Filter
    all_types = sorted(df["health_centre_type"].astype(str).unique().tolist())
    selected_types = st.sidebar.multiselect(
        "Health Centre Type", options=all_types
    )

    # Apply filters
    filtered_df = df.copy()

    if selected_islands:
        filtered_df = filtered_df[filtered_df["island"].isin(selected_islands)]

    if selected_types:
        filtered_df = filtered_df[
            filtered_df["health_centre_type"].astype(str).isin(selected_types)
        ]

    return filtered_df
