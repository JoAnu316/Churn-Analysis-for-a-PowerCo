import streamlit as st
import streamlit.components.v1 as components

# home.py

def home_page():
    # Your code here
    pass




import streamlit as st

def home_page():
    st.title("Welcome to my web page. Let us help you predict the price of your desired house ")

    st.image("house image.jpg", caption = "House Prediction Prediction", use_column_width=True)

    st.markdown("""
    <h3 style = "colour:blue;">
    Predicting house prices can be a...
    </h3>
    """, unsafe_allow_html=True)

    st.markdown("""
        ### How it works:
        1. nout the feature 
    """)

    st.markdown("""
        ___
        ### About this project:
    """)

    st.info("""
        This project uses a dataset that contains house pricing data from califonia
    """)