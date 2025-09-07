# 💼 Medical Insurance Cost Prediction

A machine learning project that predicts the annual **medical insurance cost** for individuals based on personal and health-related features. Built using **Linear Regression**, **Streamlit**, and **scikit-learn**.

---

## 🔍 Overview

This project demonstrates a full pipeline of:

* Exploratory Data Analysis (EDA)
* Data preprocessing and feature encoding
* Model training (separate models for smokers and non-smokers)
* Model evaluation (RMSE  / MAE /  R² )
* Scalable and interactive **web app** using Streamlit

---

## 🚀 Features

* 🔄 Supports three models:

  * General model trained on all data
  * Specialized model for smokers
  * Specialized model for non-smokers
* ✅ Automatic model selection based on smoking status
* 🔁 Manual override to use the general model
* 📊 User-friendly sliders and dropdowns
* 📦 Trained models and saved 

---

## 🖼 Screenshots


### 🖼 Streamlit App Interface
<img src="images/streamlit.png" width="600"/>

### 📊 EDA Visualization
<img src="images/eda.png" width="600"/>


---

## 📂 Project Structure

```
│
├── app/
│   ├── main.py              # Main Streamlit application
│   └── utils.py             # Utility functions for the app
│
├── data/
│   └── insurance.csv        # Dataset file
│
├── images/
│   ├── eda.png             # EDA visualization
│   └── streamlit.png       # App interface screenshot
│
├── models/
│   ├── model_all.pkl       # General model (all data)
│   ├── model_nonsmokers.pkl # Non-smoker specific model
│   ├── model_smokers.pkl   # Smoker specific model
│   ├── scaler_all.pkl      # Scaler for general model
│   ├── scaler_nonsmokers.pkl # Scaler for non-smoker model
│   └── scaler_smokers.pkl  # Scaler for smoker model
│
├── notebooks/
│   ├── 01_EDA.ipynb        # Exploratory Data Analysis
│   └── 02_Model_Building.ipynb # Model training and evaluation
│
├── src/
│   └── preprocessing.py    # Data preprocessing utilities
│
│
├── config.py               # Configuration settings
├── .gitignore              # Git ignore rules
├── LICENSE                 # MIT License
├── requirements.txt        # Production dependencies
└── README.md               # Project documentation
```

---

## 🚀 Quick Start

### Option 1: Using pip (Recommended)

```bash
# Install the package
pip install git+https://github.com/YounesElshafi/health-insurance-cost-prediction-streamlit.git

# Run the app
streamlit run app/main.py
```

### Option 2: Manual Installation

1. **Clone the repository**:
```bash
git clone https://github.com/YounesElshafi/health-insurance-cost-prediction-streamlit.git
cd health-insurance-cost-prediction-streamlit
```

2. **Install dependencies**:
```bash
pip install -r requirements.txt
```

3. **Run the app**:
```bash
streamlit run app/main.py
```


---

## 📈 Model Performance

🔹 Results for model All Data:
   MAE  = 4181.19
   RMSE = 5796.28
   R²   = 0.7836

🔹 Results for model  Smokers:
   MAE  = 4774.73
   RMSE = 6697.87
   R²   = 0.7010

🔹 Results for model Non-Smokers:
   MAE  = 2422.00
   RMSE = 4363.45
   R²   = 0.4577

* ➕ Specialized models give better results when segmenting the data

---

## 📁 Dataset Info

* Source: `data/insurance.csv`
* Features:
  * `age`, `sex`, `bmi`, `children`, `smoker`, `region`

* Target:
  * `charges`

---

## 📁 Dataset Information

The dataset used in this project is the **Medical Cost Personal Dataset** from Kaggle.

### 📊 Dataset Details:
- **Source**: [Kaggle - Medical Cost Personal Dataset](https://www.kaggle.com/datasets/mirichoi0218/insurance)
- **Size**: 1,338 records
- **Features**: 6 input features + 1 target variable

### 🔍 Feature Description:
- **age**: Age of the insured person (18-64)
- **sex**: Gender of the insured person (male/female)
- **bmi**: Body Mass Index (15.96-53.13)
- **children**: Number of children/dependents covered (0-5)
- **smoker**: Smoking status (yes/no)
- **region**: Geographic region (northeast/northwest/southeast/southwest)
- **charges**: Individual medical costs billed by health insurance (target variable)

### 📈 Data Insights:
- The dataset shows significant variation in insurance costs
- Smoking status has the most significant impact on costs
- Age and BMI also show strong correlations with charges
- Regional differences exist but are less pronounced

---

## 🐛 Troubleshooting

### Common Issues:

**1. Model files not found:**
```
❌ Model files not found: [Errno 2] No such file or directory
```
**Solution**: Ensure you have trained the models by running the notebooks in the `notebooks/` directory.

**2. Import errors:**
```
ModuleNotFoundError: No module named 'src'
```
**Solution**: Make sure you're running the app from the project root directory.

**3. Streamlit not found:**
```
streamlit: command not found
```
**Solution**: Install requirements: `pip install -r requirements.txt`

**4. Port already in use:**
```
Port 8501 is already in use
```
**Solution**: Use a different port: `streamlit run app/main.py --server.port 8502`

---

## 📧 Contact

Made by **Younes Elshafi** — feel free to connect!

- **Email**: younes.ai.dev@gmail.com
- **GitHub**: [@YounesElshafi](https://github.com/YounesElshafi)

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

### 📋 License Summary:
- ✅ Commercial use
- ✅ Modification
- ✅ Distribution
- ✅ Private use
- ❌ No liability
- ❌ No warranty

