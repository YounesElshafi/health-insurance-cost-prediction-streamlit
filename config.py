"""
Configuration file 
"""

import os

# Base directory
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Model paths
MODEL_PATHS = {
    'smoker': os.path.join(BASE_DIR, 'models', 'model_smokers.pkl'),
    'nonsmoker': os.path.join(BASE_DIR, 'models', 'model_nonsmokers.pkl'),
    'all': os.path.join(BASE_DIR, 'models', 'model_all.pkl')
}

SCALER_PATHS = {
    'smoker': os.path.join(BASE_DIR, 'models', 'scaler_smokers.pkl'),
    'nonsmoker': os.path.join(BASE_DIR, 'models', 'scaler_nonsmokers.pkl'),
    'all': os.path.join(BASE_DIR, 'models', 'scaler_all.pkl')
}

# Data paths
DATA_PATH = os.path.join(BASE_DIR, 'data', 'insurance.csv')

# Model parameters
RANDOM_STATE = 42
TEST_SIZE = 0.2

# Feature names
NUMERIC_FEATURES = ['age', 'bmi', 'children']
CATEGORICAL_FEATURES = ['sex', 'smoker', 'region']
TARGET_FEATURE = 'charges'

# Input validation ranges
INPUT_RANGES = {
    'age': (18, 100),
    'bmi': (15.0, 50.0),
    'children': (0, 10)
}

# Region encoding mapping
REGION_ENCODING = {
    "northeast": [0, 0, 0],
    "northwest": [1, 0, 0],
    "southeast": [0, 1, 0],
    "southwest": [0, 0, 1],
}

# Sex encoding
SEX_ENCODING = {
    "male": 0,
    "female": 1
}

# Smoker encoding
SMOKER_ENCODING = {
    "yes": 1,
    "no": 0
}
