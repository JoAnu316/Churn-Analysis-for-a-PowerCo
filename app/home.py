import streamlit as st
import streamlit.components.v1 as components



def home_page():
    # Title of the page with custom CSS for title color
    st.markdown("""
        <style>
            .main-title {
                color: #FF7518; /* Light Orange color */
                font-size: 30px;
                font-weight: bold;
                text-align: center;
                padding-bottom: 10px;
            }
            .subtitle {
                color: #FF7518; /* Light Orange color */
                font-size: 20px;
                font-weight: bold;
                margin-bottom: 10px;
            }
            .info-box {
                background-color: #630330;
                color: #FFFFFF; /* White text */
                font-weight: bold;
                border-radius: 20px;
                padding: 50px;
                margin-bottom: 10px;
            }
            .steps {
                background-color: #630330;
                color: #FFFFFF; /* White text */
                padding: 10px;
                font-weight: bold;
                border-radius: 20px;
                margin-bottom: 10px;
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
    <p style='text-align: justify; font-size: 15px;'>
        Churn analysis helps businesses predict which customers are likely to stop using a product or service.
        This project is built with a machine learning model to predict churnning based on price sensitivity.  
        This analysis would help businesses make better data-driven decisions.
    </p>
    """, unsafe_allow_html=True)

 # About section
    st.markdown('<div class="subtitle">About this Project:</div>', unsafe_allow_html=True)
    
    # Info box for additional details
    st.markdown("""
    <p style='text-align: justify; font-size: 15px;'>
        This project uses a dataset that contains customer data for churn prediction. The goal is to reduce customer attrition by
        understanding the key drivers of churn. This analysis can help businesses retain customers by targeting interventions
        and improving customer satisfaction.
    </p>
    """, unsafe_allow_html=True)

    # How it works section
    st.markdown('<div class="subtitle">How it Works:</div>', unsafe_allow_html=True)

    st.markdown("""
    <p style='text-align: justify; font-size: 15px;'>
        <ol>
            <li>We start by analyzing customer data from various sources.</li>
            <li>Feature engineering helps in selecting the most relevant predictors of churn.</li>
            <li>Machine learning models are applied to predict churn probability.</li>
            <li>Finally, the model’s performance is evaluated and tuned for accuracy.</li>
        </ol>
    </p>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    home_page()