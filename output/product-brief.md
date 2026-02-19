# Product Brief: RMI Health Dashboard PoC

## 1. Problem Statement
The Republic of the Marshall Islands (RMI) Ministry of Health needs a clear, visual way to monitor the status and performance of health centers scattered across multiple atolls and islands. Currently, data is likely viewed in spreadsheets, making it difficult to spot geographical trends or track performance over time.

## 2. Vision & Value Proposition
**Vision**: A centralized, interactive dashboard that provides real-time visibility into health center performance and staffing across the RMI.
**Value**:
- **Geospatial Insight**: Immediately see coverage gaps or regional issues via the map.
- **Temporal Tracking**: Monitor performance trends (scores) over time to identify improving or deteriorating centers.
- **Resource Visibility**: Quick access to staffing (Health Assistants, MHD CD Aides) and local leadership (Mayor) contacts.

## 3. Target Users
- **Ministry of Health Officials**: For high-level strategic planning and resource allocation.
- **Field Coordinators**: To monitor specific health centers and plan visits.

## 4. Core Features (PoC Scope)
- **Interactive Map**: Display all health centers on a map of RMI.
    - Color-coded markers based on Health Center Type (Main vs. Other) or Score status.
    - Rich popups displaying key info (Name, Island, Staff, Mayor, Score, Date) and a **"View Details" button**.
- **Time-Series Performance**: Line charts showing the evolution of 'Score' from 2022 to 2026.
- **Filtering**: Ability to filter the view by Island or Health Center Type.

## 5. Success Metrics
- Successful visualization of all data points from `RMI_OUTPUT.csv`.
- Interactive filtering works without lag.
- User can identify a specific health center's trend over 4 years within 3 clicks.
