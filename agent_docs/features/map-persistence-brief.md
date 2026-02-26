# Product Brief: Map Persistence & Marker Loading UX

## Problem Statement
Users on slow connections (e.g., 4G) experience a "vanishing map" effect when opening or closing the detail modal. This is caused by the entire map component being unmounted and remounted to reset marker selection.

## Vision
A seamless map experience where the base map layer remains visible at all times during modal interactions. Data updates (markers) should happen independently without flickering the base map.

## Goals
- **Eliminate Map Flickering**: The map container should stay in the DOM.
- **Marker Loading State**: Provide visual feedback when markers are being updated.
- **Maintain Responsiveness**: Ensure the app remains interactive even during data loading.

## Target Audience
Field health officers and administrators using the RMI Health Dashboard on mobile or limited bandwidth connections.
