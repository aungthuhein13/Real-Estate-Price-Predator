import streamlit as st
import numpy as np
import joblib

# Load model and scaler
model = joblib.load('price_model.pkl')
scaler = joblib.load('scaler.pkl')

st.title("LA Real Estate Price Predictor")

st.markdown("Enter the property details to estimate its market value.")

# Input widgets
beds = st.number_input("Bedrooms", min_value=0, max_value=10, step=1)
baths = st.number_input("Bathrooms", min_value=0.0, max_value=10.0, step=0.5)
sqft = st.number_input("Square Footage", min_value=100, max_value=10000, step=100)
latitude = st.number_input("Latitude", value=34.05, format="%.6f")
longitude = st.number_input("Longitude", value=-118.24, format="%.6f")

# Predict button
if st.button("Predict Price"):
    # Prepare features
    input_data = np.array([[beds, baths, sqft, latitude, longitude]])
    input_scaled = scaler.transform(input_data)

    # Predict
    predicted_price = model.predict(input_scaled)[0]

    st.success(f"Estimated Price: **${predicted_price:,.0f}**")
