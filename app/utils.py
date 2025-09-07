"""
Utility functions 
"""

import streamlit as st
import joblib
import numpy as np
import logging
from config import (
    MODEL_PATHS, 
    SCALER_PATHS, 
    REGION_ENCODING, 
    SEX_ENCODING, 
    SMOKER_ENCODING,
    INPUT_RANGES
)

logger = logging.getLogger(__name__)

def load_models_and_scalers():
    """
    Load all models and scalers with error handling
    """
    models = {}
    scalers = {}
    
    try:
        for model_type in ['smoker', 'nonsmoker', 'all']:
            models[model_type] = joblib.load(MODEL_PATHS[model_type])
            scalers[model_type] = joblib.load(SCALER_PATHS[model_type])
        
        logger.info("All models and scalers loaded successfully")
        return models, scalers
        
    except FileNotFoundError as e:
        st.error(f"❌ Model files not found: {e}")
        st.error("Please ensure all model files are present in the models/ directory")
        st.stop()
    except Exception as e:
        st.error(f"❌ Error loading models: {e}")
        st.stop()

def validate_inputs(age, bmi, children):
    """
    Validate user inputs against defined ranges
    """
    errors = []
    
    age_min, age_max = INPUT_RANGES['age']
    if not (age_min <= age <= age_max):
        errors.append(f"Age must be between {age_min} and {age_max}")
    
    bmi_min, bmi_max = INPUT_RANGES['bmi']
    if not (bmi_min <= bmi <= bmi_max):
        errors.append(f"BMI must be between {bmi_min} and {bmi_max}")
    
    children_min, children_max = INPUT_RANGES['children']
    if not (children_min <= children <= children_max):
        errors.append(f"Number of children must be between {children_min} and {children_max}")
    
    return errors

def encode_categorical_features(sex, smoker, region):
    """
    Encode categorical features consistently
    """
    sex_val = SEX_ENCODING[sex]
    smoker_val = SMOKER_ENCODING[smoker]
    region_encoded = REGION_ENCODING[region]
    
    return sex_val, smoker_val, region_encoded

def prepare_features(age, bmi, children, sex, smoker, region, scaler):
    """
    Prepare features for prediction
    """
    # Encode categorical variables
    sex_val, smoker_val, region_encoded = encode_categorical_features(sex, smoker, region)
    
    # Scale numeric features
    numeric_features = np.array([[age, bmi, children]])
    scaled_numeric = scaler.transform(numeric_features)
    
    # Combine all features
    features = np.concatenate([
        scaled_numeric[0],
        [sex_val, smoker_val],
        region_encoded
    ]).reshape(1, -1)
    
    return features

def select_model(smoker, use_general_model, models, scalers):
    """
    Select appropriate model based on smoking status and user preference
    """
    if use_general_model:
        model = models['all']
        scaler = scalers['all']
        model_name = "General model (all data)"
    elif smoker == "yes":
        model = models['smoker']
        scaler = scalers['smoker']
        model_name = "Smoker model"
    elif smoker == "no":
        model = models['nonsmoker']
        scaler = scalers['nonsmoker']
        model_name = "Non-smoker model"
    else:
        model = models['all']
        scaler = scalers['all']
        model_name = "General model (fallback)"
    
    return model, scaler, model_name

def format_prediction(prediction):
    """
    Format prediction result for display
    """
    return f"${prediction:,.2f}"
