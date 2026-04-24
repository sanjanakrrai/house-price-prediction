import streamlit as st
import pandas as pd
import pickle

# Load data & model
data = pd.read_csv('data/processed/cleaned_data.csv')
model = pickle.load(open('model/model.pkl', 'rb'))

# Page config
st.set_page_config(page_title="House Price Predictor", layout="centered")

st.markdown("<h1 style='text-align: center;'>🏠 House Price Predictor</h1>", unsafe_allow_html=True)

# Inputs
location = st.selectbox("Select Location", sorted(data['location'].unique()))
bhk = st.number_input("Enter BHK", min_value=1, step=1)
bath = st.number_input("Enter Bathrooms", min_value=1, step=1)
sqft = st.number_input("Enter Square Feet", min_value=100.0, step=100.0)

# Prediction
if st.button("🚀 Predict Price"):

    if sqft < 100:
        st.warning("⚠️ Enter valid square feet to get prediction")

    elif bhk <= 0:
        st.error("BHK must be at least 1")

    elif bath <= 0:
        st.error("Bathrooms must be at least 1")

    else:
        input_df = pd.DataFrame([[location, sqft, bath, bhk]],
                                columns=['location', 'total_sqft', 'bath', 'bhk'])

        prediction = model.predict(input_df)[0] * 1e5

        st.success(f"💰 Estimated Price: ₹ {round(prediction, 2):,}")