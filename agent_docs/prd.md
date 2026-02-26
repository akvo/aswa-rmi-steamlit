# PRD: RMI Health Dashboard (Living Document)

## 1. Project Vision
A comprehensive, geospatial health management system for the Republic of the Marshall Islands (RMI). The dashboard provides health administrators and field officers with real-time (daily/monthly) visibility into facility scores, staffing levels, and performance trends across all islands.

## 2. Target Users
- **Ministry of Health (MOH) Administrators**: To monitor national trends and prioritize resource allocation.
- **Island Mayor / Council**: To view health status of their specific region.
- **Health Assistants**: To track their facility's performance over time.

## 3. Core Features
- **Map Interface**: A Folium-based visualization of all health centers with color-coded markers based on performance scores.
- **Interactive Metrics**: High-level KPIs (Total Centers, Average Score, Data Quality indicators) overlaid on the map.
- **Filtering System**: Sidebar filters for Island and Health Center Type.
- **Detail Drilldown**: A comprehensive modal (or drawer) for facility-specific analytics, including historical trends and personnel logs.
- **National Analytics**: A persistent trend section at the bottom for macro-level decision making.

## 4. Technical Constraints
- **Stack**: Python-Streamlit, Dockerized environment.
- **Deployment**: Local and server-based via Streamlit.
- **Connectivity**: Must handle slow 4G/3G connections gracefully (High Priority).

## 5. Success Metrics
- 100% visibility of all health centers with geodata.
- Sub-2 second rendering of map updates on stable connections.
- User adoption by at least 80% of MOH administrators.
