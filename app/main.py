import streamlit as st
import sys
import os

# Add parent directory to path 
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.utils import (
    load_models_and_scalers,
    validate_inputs,
    prepare_features,
    select_model,
    format_prediction
)

# ---------------------------
# Load models and scalers
# ---------------------------
models, scalers = load_models_and_scalers()

# ---------------------------
# Streamlit UI
# ---------------------------
st.set_page_config(page_title="Insurance Cost Predictor", layout="centered")
st.title("💰 Medical Insurance Cost Predictor")
st.write("Fill in the form to predict the expected insurance cost.")

# Inputs
col1, col2 = st.columns(2)

with col1:
    age = st.slider("Age", 18, 100, 30)
    bmi = st.slider("BMI", 15.0, 50.0, 25.0)
    children = st.number_input("Number of Children", 0, 10, 1)

with col2:
    sex = st.selectbox("Sex", ["male", "female"])
    smoker = st.selectbox("Smoker", ["yes", "no"])
    region = st.selectbox("Region", ["northeast", "northwest", "southeast", "southwest"])

# Optional override for general model
use_general_model = st.checkbox("🔁 Force using general model (all data)", value=False)

# Validate inputs
validation_errors = validate_inputs(age, bmi, children)
if validation_errors:
    for error in validation_errors:
        st.error(f"❌ {error}")
    st.stop()

# Select model and scaler
model, scaler, model_name = select_model(smoker, use_general_model, models, scalers)
st.write(f"✅ Using: {model_name}")

# Prepare features for prediction
features = prepare_features(age, bmi, children, sex, smoker, region, scaler)

# Predict
if st.button("Predict Insurance Charges"):
    prediction = model.predict(features)[0]
    formatted_prediction = format_prediction(prediction)
    st.success(f"💵 Estimated Insurance Cost: {formatted_prediction}")
