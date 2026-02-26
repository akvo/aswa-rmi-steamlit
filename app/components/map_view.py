import folium
from branca.element import Template, MacroElement
from streamlit_folium import st_folium
import pandas as pd
import streamlit as st


class ResetViewControl(MacroElement):
    """Adds a custom Leaflet control button to reset map view."""

    def __init__(self, lat, lon, zoom):
        super().__init__()
        self._template = Template(
            """
            {% macro script(this, kwargs) %}
                var resetBtn = L.control({position: 'topleft'});
                resetBtn.onAdd = function (map) {
                    var div = L.DomUtil.create(
                        'div',
                        'leaflet-bar leaflet-control leaflet-control-custom'
                    );
                    div.style.backgroundColor = 'white';
                    div.style.width = '34px';
                    div.style.height = '34px';
                    div.style.cursor = 'pointer';
                    div.style.display = 'flex';
                    div.style.justifyContent = 'center';
                    div.style.alignItems = 'center';
                    div.innerHTML = "<span title='Return to Center' " +
                                    "style='font-size: 18px;'>📍</span>";
                    div.onclick = function(e) {
                        e.preventDefault();
                        map.setView(["""
            + str(lat)
            + """, """
            + str(lon)
            + """], """
            + str(zoom)
            + """);
                    }
                    return div;
                };
                resetBtn.addTo({{ this._parent.get_name() }});
            {% endmacro %}
            """
        )


def render_map(
    df: pd.DataFrame,
    allow_empty: bool = False,
    key: str = "main_map",
    center: list = None,
    zoom: int = 6,
):
    """
    Renders a Folium map with health centers.

    Args:
        df: Pandas DataFrame containing health center data with
        'latitude' and 'longitude'.
        allow_empty: If True, renders map even if invalid/empty data.
    """
    if df.empty and not allow_empty:
        st.warning("No data available to display on map.")
        return

    # Center map on RMI
    # 7.1315° N, 171.1845° E
    default_lat = 7.5
    default_lon = 170.0

    # Use average if available, otherwise default
    center_lat = df["latitude"].mean() if not df.empty else default_lat
    center_lon = df["longitude"].mean() if not df.empty else default_lon

    # Create map with standard tiles for 'blue map' aesthetic
    m = folium.Map(
        location=center if center else [center_lat, center_lon],
        zoom_start=zoom if zoom else 6,
        tiles="OpenStreetMap",
        control_scale=True,
        zoom_control=True,
    )

    for _, row in df.iterrows():
        # Determine color based on score (Emerald, Amber, Rose)
        score = row.get("score", 0)
        if pd.isna(score):
            color = "gray"
        elif score >= 80:
            color = "darkgreen"  # Emerald
        elif score >= 50:
            color = "orange"  # Amber
        else:
            color = "red"  # Rose

        # Tooltip content
        # No extra tooltip content needed here as it's handled by healt_centre

        # Additional Fields
        ha = row.get("health_assistans", "")
        ha = ha if pd.notnull(ha) and str(ha).strip() != "" else "N/A"

        mhd = row.get("mhd_cd_aide", "")
        mhd = mhd if pd.notnull(mhd) and str(mhd).strip() != "" else "N/A"

        mayor = row.get("mayor", "")
        mayor = mayor if pd.notnull(mayor) and str(mayor).strip() != "" else "N/A"

        folium.Marker(
            location=[row["latitude"], row["longitude"]],
            tooltip=row["healt_centre"],
            icon=folium.Icon(color=color, icon="info-sign"),
        ).add_to(m)

    # Add custom Return to Center control
    m.add_child(ResetViewControl(default_lat, default_lon, 6))

    # Render map
    output = st_folium(
        m,
        width="100%",
        height=800,
        key=key,
    )
    return output
