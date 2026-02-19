# User Guide: RMI Health Dashboard

## 1. Getting Started

### Accessing the Dashboard
- Open your web browser and navigate to: [http://localhost:8501](http://localhost:8501)
- The dashboard will load the "Blue Map" of the Marshall Islands.

## 2. Navigation & Exploration

### 2.1 The Map
- **Pan/Zoom**: Use your mouse or trackpad to move around the map. Zoom in to see specific atolls (e.g., Majuro, Kwajalein).
- **Markers**: Health centers are shown as colored pins:
    - 🟢 **Green**: High Performance (Score 80+)
    - 🟠 **Orange**: Medium Performance (Score 50-79)
    - 🔴 **Red**: Low Performance (Score <50)

### 2.2 Previewing a Facility
- **Click a Marker**: A popup will appear showing:
    - Name and Island
    - Facility Type (e.g., Dispensary)
    - **Staffing**: Health Assistant and MHD CD Aide names.
    - **Leadership**: Mayor name.
    - Latest Score and Date.
- **View Details**: Inside the popup, click the **"View Details ➝"** button to open the full analysis modal.

### 2.3 Detail Modal
- A centered overlay displays:
    - **Facility Summary**: Aligned with the map popup, showing all location and staff details.
    - **Trend Chart**: How the facility's score has changed over time.
    - **History Log**: A table of all past reports.
- **Close**: Click the "Close Details" button or the "X" in the top right to return to the full map view.

## 3. Analytics Tools

### 3.1 National Trends
- Scroll down below the main map to see the **National Performance Trends** section.
- This chart shows the aggregate performance of all filtered facilities over time.

### 3.2 Filtering Data
- Use the **Sidebar** on the left to filter the view:
    - **Select Atoll/Island**: Focus on specific regions.
    - **Health Centre Type**: Filter by Hospital, Dispensary, etc.
- **Note**: Filters affect the Map, Metrics, and Trend Charts simultaneously.

## 4. Troubleshooting
- **Map not loading?**: Ensure you have an active internet connection (OpenStreetMap tiles require it).
- **"No Data" message?**: Check your filter selection. If you unselect all options or select a combination with no results, the map may be empty.
