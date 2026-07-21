# 💳 Credit Card Fraud Detection

![Python](https://img.shields.io/badge/Python-3.11-blue?style=for-the-badge\&logo=python)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-ML-orange?style=for-the-badge\&logo=scikitlearn)
![Streamlit](https://img.shields.io/badge/Streamlit-Web%20App-red?style=for-the-badge\&logo=streamlit)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

## 📌 Project Overview

Credit Card Fraud Detection is a Machine Learning project that predicts whether a credit card transaction is **Fraudulent** or **Legitimate** using historical transaction data.

The project applies data preprocessing, exploratory data analysis (EDA), class imbalance handling using **SMOTE**, and multiple machine learning algorithms to build a reliable fraud detection system.

The best-performing model is deployed using **Streamlit** for real-time fraud prediction.

---

# 🎯 Business Problem

Credit card fraud is one of the biggest challenges faced by banks and financial institutions. Fraudulent transactions are extremely rare compared to legitimate transactions, making fraud detection a highly imbalanced classification problem.

The objective of this project is to accurately detect fraudulent transactions while minimizing false positives and improving financial security.

---

# 🎯 Project Objectives

* Detect fraudulent credit card transactions.
* Handle severe class imbalance using SMOTE.
* Compare multiple machine learning algorithms.
* Select the best-performing model.
* Deploy the model using Streamlit.
* Build a real-time fraud prediction system.

---

# 📂 Dataset Information

* **Dataset Name:** Credit Card Fraud Detection
* **Total Transactions:** 284,807
* **Features:** 30 Predictor Variables
* **Target Variable:** Class

### Target Variable

| Value | Description            |
| ----- | ---------------------- |
| 0     | Legitimate Transaction |
| 1     | Fraudulent Transaction |

---

# 🛠 Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Scikit-learn
* Imbalanced-learn (SMOTE)
* XGBoost
* Joblib
* Streamlit

---

# 📊 Machine Learning Workflow

## 1️⃣ Business Understanding

* Defined the business problem
* Identified objectives
* Understood fraud detection challenges

---

## 2️⃣ Data Collection

* Imported the dataset
* Loaded data using Pandas

---

## 3️⃣ Data Understanding

Performed:

* Dataset Shape
* Dataset Information
* Data Types
* Statistical Summary

---

## 4️⃣ Data Cleaning

Performed:

* Missing Value Analysis
* Duplicate Record Removal
* Data Validation

---

## 5️⃣ Exploratory Data Analysis (EDA)

Performed:

### Univariate Analysis

* Class Distribution
* Amount Distribution
* Time Distribution

### Bivariate Analysis

* Amount vs Class
* Time vs Class

### Multivariate Analysis

* Correlation Heatmap

### Outlier Analysis

* Boxplots
* IQR Method

### Overall EDA Insights

* No missing values were found.
* Duplicate records were removed.
* Fraudulent transactions represent only a very small percentage of the dataset.
* The dataset is highly imbalanced.
* Transaction Amount contains significant outliers.
* Time and Amount required feature scaling.
* PCA-transformed features contributed significantly to fraud prediction.

---

## 6️⃣ Data Preprocessing

Performed:

* Feature and Target Separation
* StandardScaler
* Train-Test Split
* SMOTE for Class Balancing

---

## 7️⃣ Model Building

The following Machine Learning models were trained and evaluated:

* Logistic Regression
* Decision Tree
* Random Forest
* Gradient Boosting
* XGBoost
* Extra Trees Classifier

---

## 8️⃣ Model Evaluation

Evaluation Metrics:

* Accuracy
* Precision
* Recall
* F1 Score
* ROC-AUC Score
* Confusion Matrix

### 🏆 Best Model

**Extra Trees Classifier**

| Metric    |      Score |
| --------- | ---------: |
| Accuracy  | **99.95%** |
| Precision | **94.74%** |
| Recall    | **75.79%** |
| F1 Score  | **84.21%** |
| ROC-AUC   | **97.73%** |

---

## 9️⃣ Feature Importance

Top important features include:

* V14
* V12
* V17
* V11
* V10
* V16
* V4

---

# 🚀 Streamlit Web Application

The application allows users to:

* Enter transaction details
* Predict Fraud or Legitimate transactions
* View Fraud Probability
* Display Prediction Confidence
* Show Transaction Risk Level

---

# 📂 Project Structure

```text
Credit-Card-Fraud-Detection/
│
├── app.py
├── fraud_detection_model.pkl
├── scaler.pkl
├── Credit_Card_Fraud_Detection.ipynb
├── requirements.txt
├── runtime.txt
├── README.md
├── LICENSE
├── .gitignore
├── images/
└── creditcard.csv
```

---

# ⚙️ Installation

### Clone the Repository

```bash
git clone https://github.com/palsamanojkumar-07/Credit-Card-Fraud-Detection.git
```

### Navigate to the Project Folder

```bash
cd Credit-Card-Fraud-Detection
```

### Install Required Libraries

```bash
pip install -r requirements.txt
```

### Run the Streamlit Application

```bash
streamlit run app.py
```

---

# 🌐 Project Links

* **GitHub Repository:** https://github.com/palsamanojkumar-07/Credit-Card-Fraud-Detection
* **Live Streamlit Application:** https://manoj-credit-card-fraud-detector.streamlit.app


---

# 📈 Business Impact

* Detects fraudulent transactions efficiently.
* Reduces financial losses.
* Improves customer trust.
* Supports real-time fraud monitoring.
* Assists financial institutions in risk management.

---

# 🔮 Future Enhancements

* Deploy with Docker.
* Integrate FastAPI for REST APIs.
* Add SHAP explainability.
* Enable real-time transaction streaming.
* Build an end-to-end MLOps pipeline.

---

# 👨‍💻 Author

**PALSA MANOJ KUMAR**

**Machine Learning | Python | Streamlit**

GitHub: https://github.com/palsamanojkumar-07

---

