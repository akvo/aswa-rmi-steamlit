import streamlit as st


def inject_full_screen_css():
    """
    Injects custom CSS to remove Streamlit's default margins and padding,
    allowing the map to occupy the full viewport while respecting the sidebar.
    """
    st.markdown(
        """
        <link href="https://fonts.googleapis.com/css2?family=Inter"
            rel="stylesheet">
        <style>
            /* Global Font */
            html, body, [data-testid="stAppViewContainer"] {
                font-family: 'Inter', sans-serif;
            }

            /* Hide Streamlit header and footer */
            header {visibility: hidden;}
            footer {visibility: hidden;}

            /* Remove padding from the main block-container */
            .main .block-container, .stMainBlockContainer {
                padding-top: 0rem;
                padding-bottom: 0rem;
                padding-left: 0rem;
                padding-right: 0rem;
                margin: 0;
                max-width: 100%;
            }

            .stMainBlockContainer > .stVerticalBlock {
                gap: 0;
            }

            /* Custom class for Frosted Medical Glass */
            .glass-overlay {
                background: rgba(255, 255, 255, 0.85);
                backdrop-filter: blur(12px) saturate(180%);
                -webkit-backdrop-filter: blur(12px) saturate(180%);
                border: 1px solid rgba(15, 118, 110, 0.15);
                border-radius: 12px;
                padding: 1.25rem;
                color: #1e293b; /* Slate-800 */
                box-shadow: 0 4px 15px -1px rgba(0, 0, 0, 0.05),
                            0 2px 6px -1px rgba(0, 0, 0, 0.05);
                transition: transform 0.2s ease, box-shadow 0.2s ease;
            }

            .glass-overlay:hover {
                transform: translateY(-2px);
                box-shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.1);
                border-color: rgba(15, 118, 110, 0.3);
            }

            /* Sidebar Header Styling (Medical Teal) */
            [data-testid="stSidebar"] h1, [data-testid="stSidebar"] h2 {
                color: #0d9488; /* Teal-600 */
                font-weight: 600;
            }

            /* Metric Label Styling */
            .metric-label {
                font-size: 0.75rem;
                opacity: 0.7;
                text-transform: uppercase;
                letter-spacing: 0.05em;
                margin-bottom: 0.25rem;
                color: #475569; /* Slate-600 */
            }
        </style>
        """,
        unsafe_allow_html=True,
    )
