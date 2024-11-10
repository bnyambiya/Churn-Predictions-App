import streamlit as st
import pandas as pd
import pickle
from sklearn.preprocessing import LabelEncoder

# Set page configuration
st.set_page_config(page_title="Customer Churn Prediction", layout="wide")

# Custom CSS for styling
st.markdown("""
    <style>
        .main { 
            background-color: #f9f9f9; 
        }
        h1 {
            color: #4CAF50;
            text-align: center;
        }
        .option-title {
            color: #4CAF50;
            font-size: 1.5em;
            margin: 10px 0;
        }
        .footer {
            text-align: center;
            color: #9E9E9E;
            padding: 15px;
            margin-top: 20px;
            border-top: 1px solid #ccc;
        }
        .sidebar .sidebar-content {
            background-color: #ffffff;
            padding: 10px;
            border-radius: 8px;   
        }
        .sidebar .sidebar-header {
            font-size: 1.5em;
            color: #4CAF50;
        }
        .stButton {
            text-align: center;
            margin: 10px 0;
            border-radius: 8px;
            background-color: #4CAF50;
            color: white;
        }
        .stButton:hover {
            background-color: #45a049;
        }
    </style>
""", unsafe_allow_html=True)

# Set the title of the web app
st.markdown("<h1>Customer Churn Prediction System</h1>", unsafe_allow_html=True)

# Provide a description of what churn prediction is
st.markdown("""
### What is Churn Prediction?
Churn prediction is the process of identifying customers who are likely to stop using a service or product. Understanding churn helps businesses retain customers, improve satisfaction, and ultimately drive profitability.

By analyzing customer behavior and historical data, businesses can proactively take steps to engage at-risk customers and enhance their experience.

### Why is Churn Prediction Important?
- **Customer Retention**: Reducing churn rates can lead to significant increases in revenue.
- **Cost Efficiency**: Acquiring new customers is often more expensive than retaining existing ones.
- **Better Decision Making**: Insights derived from churn prediction models help businesses tailor their services to meet customer needs.

Our churn prediction system leverages machine learning and statistical modeling to help businesses identify potential churners and devise strategies for retention. 
""")

# Footer
st.markdown("<div class='footer'>© 2024 Churn Prediction Inc.</div>", unsafe_allow_html=True)