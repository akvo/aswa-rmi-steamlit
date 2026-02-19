# RMI Health Dashboard (PoC)

## 1. Problem Statement
The Republic of the Marshall Islands (RMI) Ministry of Health needs a clear, visual way to monitor the status and performance of health centers scattered across multiple atolls and islands. Currently, data is likely viewed in spreadsheets, making it difficult to spot geographical trends or track performance over time.

## 2. Solution Overview
This **Proof of Concept (PoC)** dashboard provides a centralized, interactive view of health center performance. It combines geospatial exploration with temporal tracking to support data-driven decision-making.

### Key Capabilities
- **Geospatial Insight**: Full-screen **OpenStreetMap** integration allows officials to immediately visualize coverage gaps and regional clusters across the atolls.
- **Temporal Tracking**: Interactive charts track performance scores over time (2022-2026), helping identify improving or deteriorating centers.
- **Resource Visibility**: Quick access to essential facility data—including **Health Assistant** names, **Facility Type**, and **Mayor** contacts—directly from the map.

## 3. Features
- **Interactive Map**: Markers are color-coded by performance (Green/Orange/Red) for instant status assessment.
- **Drill-Down Analysis**:
    - **Preview**: Click a marker for a quick summary popup.
    - **Deep Dive**: Open the side drawer to view historical logs and detailed trend analysis without losing map context.
- **National Trends**: A bottom-anchored analytics section provides a high-level view of system-wide performance.

## 4. How to Run
This project runs within a Docker container to ensure a consistent environment.

### Prerequisites
- Docker and Docker Compose installed.

### Start the Application
1. **Build and Start**:
   ```bash
   ./dc.sh up -d       # Starts the application in the background
   ```

2. **Access the Dashboard**:
   Open your browser and navigate to:
   [http://localhost:8501](http://localhost:8501)

3. **Stop the Application**:
   ```bash
   ./dc.sh down
   ```

## 5. Project Documentation
Detailed documentation is available in the `output/` directory:

| Document | Description |
|----------|-------------|
| **[Product Requirements (PRD)](output/prd.md)** | Functional specifications and feature requirements. |
| **[User Stories](output/stories.md)** | User-centric development stories. |
| **[Architecture](output/architecture.md)** | System components and data flow design. |
| **[UX Specification](output/ux-design-specification.md)** | Design guidelines and interaction patterns. |

## 6. Tech Stack
- **Frontend**: Streamlit
- **Mapping**: Folium + OpenStreetMap
- **Data**: Pandas
- **Infrastructure**: Docker
