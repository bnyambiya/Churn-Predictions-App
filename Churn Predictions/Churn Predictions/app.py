import streamlit as st
import pandas as pd
import pickle
from sklearn.preprocessing import LabelEncoder

# Load the model (ensure you have trained it with the same preprocessing)
model_filename = 'churn_model.pkl'
with open(model_filename, 'rb') as file:
    model = pickle.load(file)

# Load the label encoders (you need to save these during your model training)
label_encoders = {}

# Function to encode categorical variables
def preprocess_input(data):
    # Example: Assuming you created LabelEncoders for each categorical feature 
    # during model training and saved them as pickle files.
    for column in ['gender', 'Partner', 'Dependents', 'PhoneService',
                   'MultipleLines', 'InternetService', 'OnlineSecurity',
                   'OnlineBackup', 'DeviceProtection', 'TechSupport',
                   'StreamingTV', 'StreamingMovies', 'Contract',
                   'PaperlessBilling', 'PaymentMethod']:
        le = LabelEncoder()
        le.fit(['Male', 'Female', 'Yes', 'No', 'No phone service', 
                'DSL', 'Fiber optic', 'No', 'No internet service',
                'Month-to-month', 'One year', 'Two year', 
                'Electronic check', 'Mailed check', 'Bank transfer', 
                'Credit card'])  # Populate this with the correct values.
        label_encoders[column] = le

    for column in label_encoders:
        data[column] = label_encoders[column].transform(data[column])

    return data

# Function to predict churn
def predict_churn(data):
    data = preprocess_input(data)
    prediction = model.predict(data)
    return prediction

# Title of the app
st.title('Customer Churn Prediction')

# Input fields
gender = st.selectbox('Gender', ('Male', 'Female'))
senior_citizen = st.selectbox('Senior Citizen', (0, 1))
partner = st.selectbox('Partner', ('Yes', 'No'))
dependents = st.selectbox('Dependents', ('Yes', 'No'))
tenure = st.number_input('Tenure (months)', min_value=0)
phone_service = st.selectbox('Phone Service', ('Yes', 'No'))
multiple_lines = st.selectbox('Multiple Lines', ('Yes', 'No', 'No phone service'))
internet_service = st.selectbox('Internet Service', ('DSL', 'Fiber optic', 'No'))
online_security = st.selectbox('Online Security', ('Yes', 'No', 'No internet service'))
online_backup = st.selectbox('Online Backup', ('Yes', 'No', 'No internet service'))
device_protection = st.selectbox('Device Protection', ('Yes', 'No', 'No internet service'))
tech_support = st.selectbox('Tech Support', ('Yes', 'No', 'No internet service'))
streaming_tv = st.selectbox('Streaming TV', ('Yes', 'No', 'No internet service'))
streaming_movies = st.selectbox('Streaming Movies', ('Yes', 'No', 'No internet service'))
contract = st.selectbox('Contract', ('Month-to-month', 'One year', 'Two year'))
paperless_billing = st.selectbox('Paperless Billing', ('Yes', 'No'))
payment_method = st.selectbox('Payment Method', ('Electronic check', 'Mailed check', 'Bank transfer', 'Credit card'))
monthly_charges = st.number_input('Monthly Charges', min_value=0.0)
total_charges = st.number_input('Total Charges', min_value=0.0)

# Creating a DataFrame for model input
data = pd.DataFrame({
    'gender': [gender],
    'SeniorCitizen': [senior_citizen],
    'Partner': [partner],
    'Dependents': [dependents],
    'tenure': [tenure],
    'PhoneService': [phone_service],
    'MultipleLines': [multiple_lines],
    'InternetService': [internet_service],
    'OnlineSecurity': [online_security],
    'OnlineBackup': [online_backup],
    'DeviceProtection': [device_protection],
    'TechSupport': [tech_support],
    'StreamingTV': [streaming_tv],
    'StreamingMovies': [streaming_movies],
    'Contract': [contract],
    'PaperlessBilling': [paperless_billing],
    'PaymentMethod': [payment_method],
    'MonthlyCharges': [monthly_charges],
    'TotalCharges': [total_charges]
})

# Predict button
if st.button('Predict Churn'):
    prediction = predict_churn(data)
    if prediction[0] == 1:
        st.success("The model predicts that this customer will churn.")
    else:
        st.success("The model predicts that this customer will not churn.")