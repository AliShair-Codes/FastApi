import streamlit as st
import requests

# Define the FastAPI backend URL
API_URL = "http://127.0.0.1:8000/predict"  # Make sure to adjust the URL if it's different

# Streamlit app layout
st.title('Health Premium Prediction')

# Input fields for the user
age = st.number_input('Age', min_value=1, max_value=120, value=25)
weight = st.number_input('Weight (in kg)', min_value=1.0, value=70.0)
height = st.number_input('Height (in meters)', min_value=0.1, max_value=2.5, value=1.75)
income_lpa = st.number_input('Income (in LPA)', min_value=1.0, value=5.0)
smoker = st.selectbox('Are you a smoker?', ['Yes', 'No'])
city = st.text_input('City')
occupation = st.selectbox('Occupation', ['retired', 'freelancer', 'student', 'government_job', 'business_owner', 'unemployed', 'private_job'])

# Convert 'Yes'/'No' to boolean for smoker
smoker_bool = True if smoker == 'Yes' else False

# Button to trigger prediction
if st.button('Predict'):
    # Prepare the data to be sent to the API
    data = {
        "age": age,
        "weight": weight,
        "height": height,
        "income_lpa": income_lpa,
        "smoker": smoker_bool,
        "city": city,
        "occupation": occupation
    }

    # Send a POST request to the FastAPI backend
    try:
        response = requests.post(API_URL, json=data)
        
        if response.status_code == 200:
            prediction = response.json()
            st.success(f"Predicted Category: {prediction['predicted_category']}")
        else:
            st.error("Error: Unable to get prediction from the backend.")
    except requests.exceptions.RequestException as e:
        st.error(f"Error connecting to the API: {e}")
