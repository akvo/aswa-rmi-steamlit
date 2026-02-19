# UX Design Specification: RMI Health Dashboard (PoC)

## 1. Design Philosophy
**"Clarity & Geospatial Context"**
The interface prioritizes map visibility ("Blue Map") while using a clean, professional color palette (Teal/Slate). The interaction model separates "Browsing" (Map) from "Analysis" (Drawer/Tray).

## 2. Visual Identity

### 2.1 Color Palette
- **Primary (Teal)**: `#0d9488` (Tailwind teal-600) - Used for Headers, Key Metrics, Active States.
- **Secondary (Slate)**: `#64748b` (Tailwind slate-500) - Used for Body text, Labels.
- **Backgrounds**:
    - **Map**: OpenStreetMap (Standard Blue/Green/White).
    - **Overlays**: White (`#ffffff`) with 90% opacity and 24px Blur (Glassmorphism).
    - **Drawer**: Light Slate (`#f8fafc`).

### 2.2 Typography
- **Font Face**: `Inter`, sans-serif.
- **Weights**:
    - **Headers**: 600 (Semi-Bold).
    - **Body**: 400 (Regular).
    - **Metrics**: 700 (Bold).

## 3. Layout Dimensions
- **Sidebar**: Standard Streamlit width (approx 300px).
- **Map**: Full viewport height/width (padding removed via CSS).
- **Detail Drawer**: Fixed width `420px`, right-aligned, slide-in animation.
- **Metrics Widget**: Top-left, fixed position `top: 1.5rem, left: 24rem` (offset for sidebar).

## 4. Component Specs

### 4.1 Map Markers
- **Type**: Folium Icon (`info-sign`).
- **Colors**:
    - `darkgreen`: Score ≥ 80
    - `orange`: Score 50-79
    - `red`: Score < 50

### 4.2 Popups
- **Content**: HTML-based.
- **Style**: Min-width 200px, Inter font, 14px base size.
- **Fields**: Name (Bold), Island, Type, Assistant, Date, Score.

### 4.3 Analytics Tray
- **Location**: Bottom of page flow (below map fold).
- **Structure**:
    - Header: "National Performance Trends" (Teal H3).
    - Content: Altair Chart (Full width).

## 5. Interaction Patterns
- **Hover**: Map markers show tooltip name.
- **Click (Map)**: Opens Popup -> Shows "View Details" button toast.
- **Click (View Details)**: Opens Detail Drawer -> Update URL param (optional) -> Rerender.
- **Click (Close Drawer)**: Closes drawer, returns to map view.
