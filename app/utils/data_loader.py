import pandas as pd
import streamlit as st
import os

CACHE_TTL = 3600  # Cache data for 1 hour


@st.cache_data(ttl=CACHE_TTL)
def load_data(filepath: str) -> pd.DataFrame:
    """
    Loads data from a CSV file, parses dates, and handles missing values.

    Args:
        filepath: Path to the CSV file.

    Returns:
        pd.DataFrame: The loaded and processed dataframe.
    """
    if not os.path.exists(filepath):
        st.error(f"File not found: {filepath}")
        return pd.DataFrame()

    try:
        df = pd.read_csv(filepath)

        # Parse dates
        if "date" in df.columns:
            df["date"] = pd.to_datetime(df["date"], errors="coerce")

        # Ensure numeric types for coordinates and score
        numeric_cols = ["latitude", "longitude", "score"]
        for col in numeric_cols:
            if col in df.columns:
                df[col] = pd.to_numeric(df[col], errors="coerce")

        return df
    except Exception as e:
        st.error(f"Error loading data: {e}")
        return pd.DataFrame()


def get_map_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Filters dataframe for map visualization:
    1. Requires valid lat/long.
    2. Returns only the LATEST record for each health center.
    """
    if df.empty:
        return df

    # Filter rows with valid latitude and longitude
    valid_geo_df = df.dropna(subset=["latitude", "longitude"])

    if valid_geo_df.empty:
        return valid_geo_df

    # Sort by date descending and drop duplicates to keep
    # only the latest record per center
    latest_df = valid_geo_df.sort_values("date", ascending=False).drop_duplicates(
        subset=["healt_centre"]
    )

    return latest_df


def get_missing_geodata_count(df: pd.DataFrame) -> int:
    """
    Returns the count of records missing valid geolocation data.
    """
    if df.empty:
        return 0
    return (
        df["latitude"].isna().sum()
        + df[df["latitude"].notna()]["longitude"].isna().sum()
    )
