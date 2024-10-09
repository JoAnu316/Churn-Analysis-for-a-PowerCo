# streamlit web file

import streamlit as st
from streamlit_option_menu import option_menu
from home import home_page
from prediction import pred_page

# Set page configuration
st.set_page_config(
    page_title="Churn Analysis",  # Title of the browser tab
    page_icon="analysis.png",      # Favicon (icon in the browser tab)
    layout = "wide",
    initial_sidebar_state= "expanded",
)

# Custom CSS for sidebar and main content
st.markdown("""
    <style>
        /* Body background color */
        body {
            background-color: #FF7518;
        }

        /* Sidebar styles */
        .sidebar .sidebar-content {
            background-color: #FF7518; /* White background for sidebar */
            border-radius: 10px;
            padding: 20px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        }

        /* Option menu styles */
        .sidebar .stSelectbox, .sidebar .stButton, .sidebar .stRadio {
            border-radius: 5px;
            background-color: #FF7518; /* Button background */
            color: white; /* Button text color */
            padding: 10px;
            margin-bottom: 10px;
            font-size: 16px;
            transition: background-color 0.3s;
        }
        
        .sidebar .stSelectbox:hover, .sidebar .stButton:hover, .sidebar .stRadio:hover {
            background-color: #1A4B7D; /* Darker shade on hover */
        }

        /* Main title styles */
        .main-title {
            color: #000000; /* Black color */
            font-size: 48px;
            font-weight: bold;
            text-align: center;
            padding: 20px 0;
        }

        /* Subtitle styles */
        .subtitle {
            color: #1F618D;
            font-size: 24px;
            font-weight: bold;
            margin-bottom: 10px;
        }

        /* Info box styles */
        .info-box {
            background-color: #F4ECF7;
            color: #000000; /* Black text */
            border-radius: 10px;
            padding: 20px;
            margin-top: 20px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        }

        /* Steps box styles */
        .steps {
            background-color: #F9E79F;
            color: #000000; /* Black text */
            padding: 10px;
            border-radius: 10px;
            margin-top: 20px;
            line-height: 1.8;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        }
    </style>
""", unsafe_allow_html=True)

# Sidebar with option menu
with st.sidebar:
    selected = option_menu(
        menu_title=None,
        options=["Home", "Prediction"],
        icons=["house", "check2-circle"],  # You can choose suitable icons here
        menu_icon="cast",
        default_index=0,
        styles={
            "container": {"padding": "5px"},
            "icon": {"font-size": "22px"},  # Customize icon size
            "nav-link": {"font-size": "18px", "color": "#FF7518"},  # Customize link color
            "nav-link-selected": {"background-color": "#D1E8E2"},  # Selected option background
        }
    )

# Page selection
if selected == "Home":
    home_page()

elif selected == 'Prediction':
    pred_page()

else:
    pass
