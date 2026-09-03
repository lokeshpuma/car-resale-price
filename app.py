import streamlit as st
import pandas as pd
import pickle
import os
from datetime import datetime

# Set page configuration
st.set_page_config(page_title="Car Price Predictor", page_icon="🚗", layout="centered")

st.title("🚗 Car Resale Price Predictor")
st.markdown("Enter the details of the car below to predict its resale price using Machine Learning.")

# Load Models
@st.cache_resource
def load_models():
    base_dir = os.path.dirname(__file__)
    lin_model_path = os.path.join(base_dir, 'car_price_lin.pkl')
    lass_model_path = os.path.join(base_dir, 'car_price_lass.pkl')

    if not os.path.exists(lin_model_path) or not os.path.exists(lass_model_path):
        st.error("Model files not found. Expected car_price_lin.pkl and car_price_lass.pkl in the project root.")
        return None, None

    try:
        with open(lin_model_path, 'rb') as f:
            lin_model = pickle.load(f)

        with open(lass_model_path, 'rb') as f:
            lass_model = pickle.load(f)

        return lin_model, lass_model
    except Exception as e:
        st.error(f"Failed to load models: {e}")
        return None, None


lin_model, lass_model = load_models()

# Sidebar for Model Selection
st.sidebar.header("Model Configuration")
model_choice = st.sidebar.selectbox("Choose a model:", ["Linear Regression", "Lasso Regression"])
model = lin_model if model_choice == "Linear Regression" else lass_model

# User Inputs
st.header("Car Details")

col1, col2 = st.columns(2)

with col1:
    current_year = datetime.now().year
    year = st.number_input("Year of Manufacture", min_value=1990, max_value=current_year, value=2015, step=1)
    fuel = st.selectbox("Fuel Type", ["Petrol", "Diesel", "CNG", "LPG", "Electric"])
    transmission = st.selectbox("Transmission", ["Manual", "Automatic"])

with col2:
    km_driven = st.number_input("Kilometers Driven", min_value=0, max_value=1000000, value=50000, step=1000)
    seller_type = st.selectbox("Seller Type", ["Individual", "Dealer", "Trustmark Dealer"])
    owner = st.selectbox("Owner Type", ["First Owner", "Second Owner", "Third Owner", "Fourth & Above Owner", "Test Drive Car"])

# Process Inputs for Model (Matching get_dummies from training)
fuel_Diesel = True if fuel == "Diesel" else False
fuel_Electric = True if fuel == "Electric" else False
fuel_LPG = True if fuel == "LPG" else False
fuel_Petrol = True if fuel == "Petrol" else False

seller_type_Individual = True if seller_type == "Individual" else False
seller_type_Trustmark_Dealer = True if seller_type == "Trustmark Dealer" else False

transmission_Manual = True if transmission == "Manual" else False

owner_Fourth_Above_Owner = True if owner == "Fourth & Above Owner" else False
owner_Second_Owner = True if owner == "Second Owner" else False
owner_Test_Drive_Car = True if owner == "Test Drive Car" else False
owner_Third_Owner = True if owner == "Third Owner" else False

# Create DataFrame for prediction
input_data = pd.DataFrame({
    'year': [year],
    'km_driven': [km_driven],
    'fuel_Diesel': [fuel_Diesel],
    'fuel_Electric': [fuel_Electric],
    'fuel_LPG': [fuel_LPG],
    'fuel_Petrol': [fuel_Petrol],
    'seller_type_Individual': [seller_type_Individual],
    'seller_type_Trustmark_Dealer': [seller_type_Trustmark_Dealer],
    'transmission_Manual': [transmission_Manual],
    'owner_Fourth_Above_Owner': [owner_Fourth_Above_Owner],
    'owner_Second_Owner': [owner_Second_Owner],
    'owner_Test_Drive_Car': [owner_Test_Drive_Car],
    'owner_Third_Owner': [owner_Third_Owner]
})

st.markdown("---")

if st.button("Predict Price"):
    if model is None:
        st.error("No model loaded. Cannot predict.")
    else:
        try:
            prediction = model.predict(input_data)
            # Ensure prediction is positive
            pred_value = max(0, float(prediction[0]))
            st.success(f"### Predicted Selling Price: ₹ {pred_value:,.2f}")
        except Exception as e:
            st.error(f"An error occurred during prediction: {e}")
