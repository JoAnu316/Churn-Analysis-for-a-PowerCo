import streamlit as st
import streamlit.components.v1 as components

def home_page():
    # Title of the page with custom CSS for title color
    st.markdown("""
        <style>
            .main-title {
                color: #FFD580; /* Light Orange color */
                font-size: 48px;
                font-weight: bold;
                text-align: center;
                padding-bottom: 10px;
            }
            .subtitle {
                color: #FFD580; /* Light Orange color */
                font-size: 24px;
                font-weight: bold;
                margin-bottom: 10px;
            }
            .info-box {
                background-color: #000000;
                border-radius: 10px;
                padding: 10px;
                margin-top: 10px;
            }
            .steps {
                background-color: #000000;
                padding: 10px;
                border-radius: 10px;
                margin-top: 10px;
                line-height: 1.8;
            }
        </style>
    """, unsafe_allow_html=True)

    # Main title of the project
    st.markdown('<div class="main-title">Churn Analysis Project</div>', unsafe_allow_html=True)
    
    # Image for visual appeal
    st.image("churn.jpg", caption="Churn Analysis", use_column_width=True)
    
    # Project description section with a styled subtitle
    st.markdown('<div class="subtitle">Predicting Churn with Data</div>', unsafe_allow_html=True)
    
    # Short project intro
    st.markdown("""
    <p style='text-align: justify; font-size: 18px;'>
        Churn analysis helps businesses predict which customers are likely to stop using a product or service.
        This project aims to build a machine learning model to predict churn, helping businesses make better data-driven decisions.
    </p>
    """, unsafe_allow_html=True)

    # How it works section
    st.markdown('<div class="subtitle">How it Works:</div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="steps">
        <ol>
            <li>We start by analyzing customer data from various sources.</li>
            <li>Feature engineering helps in selecting the most relevant predictors of churn.</li>
            <li>Machine learning models are applied to predict churn probability.</li>
            <li>Finally, the model’s performance is evaluated and tuned for accuracy.</li>
        </ol>
    </div>
    """, unsafe_allow_html=True)
    
    # About section
    st.markdown('<div class="subtitle">About this Project:</div>', unsafe_allow_html=True)
    
    # Info box for additional details
    st.markdown("""
    <div class="info-box">
        <p>This project uses a dataset that contains customer data for churn prediction. The goal is to reduce customer attrition by
        understanding the key drivers of churn. This analysis can help businesses retain customers by targeting interventions
        and improving customer satisfaction.</p>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    home_page()