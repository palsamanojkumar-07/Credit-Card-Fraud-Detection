# Create app.py

import streamlit as st
import pandas as pd
import joblib

# ==========================================
# PAGE CONFIGURATION
# ==========================================

st.set_page_config(
    page_title="Credit Card Fraud Detection",
    page_icon="💳",
    layout="wide"
)

# ==========================================
# LOAD MODEL
# ==========================================

model = joblib.load("fraud_detection_model.pkl")
scaler = joblib.load("scaler.pkl")

# ==========================================
# HEADER
# ==========================================

st.title("💳 Credit Card Fraud Detection System")

st.markdown("""
### 👨‍💻 Developed by **PALSA MANOJ KUMAR**

**Machine Learning | Python | Streamlit**

This application predicts whether a credit card transaction is **Fraudulent** or **Legitimate** using a trained Machine Learning model.
""")

st.markdown("---")

# ==========================================
# MODEL INFORMATION
# ==========================================

st.info("""
### 🤖 Model Information

- **Algorithm:** Extra Trees Classifier
- **Features:** 30
- **Target:** Fraud / Legitimate
""")

# ==========================================
# SIDEBAR
# ==========================================

st.sidebar.title("💳 Transaction Details")

st.sidebar.write(
    "Enter the transaction details below."
)

time = st.sidebar.number_input(
    "Time",
    value=0.0
)

amount = st.sidebar.number_input(
    "Amount",
    value=100.0
)

features = []

for i in range(1, 29):

    value = st.sidebar.number_input(
        f"V{i}",
        value=0.0,
        format="%.6f"
    )

    features.append(value)

# ==========================================
# PREDICTION
# ==========================================

if st.sidebar.button("🔍 Predict Transaction"):

    scaled = scaler.transform([[time, amount]])

    time_scaled = scaled[0][0]
    amount_scaled = scaled[0][1]

    data = [time_scaled]

    data.extend(features)

    data.append(amount_scaled)

    input_df = pd.DataFrame(
        [data],
        columns=[
            "Time",
            "V1","V2","V3","V4","V5","V6","V7","V8","V9","V10",
            "V11","V12","V13","V14","V15","V16","V17","V18","V19",
            "V20","V21","V22","V23","V24","V25","V26","V27","V28",
            "Amount"
        ]
    )

    prediction = model.predict(input_df)[0]

    probability = model.predict_proba(input_df)[0][1]

    confidence = max(probability, 1 - probability)

    st.markdown("---")

    col1, col2 = st.columns(2)

    # ===============================
    # Prediction Result
    # ===============================

    with col1:

        st.subheader("📊 Prediction Result")

        if prediction == 1:

            st.error("🚨 Fraudulent Transaction")

        else:

            st.success("✅ Legitimate Transaction")

        st.metric(
            "Fraud Probability",
            f"{probability:.2%}"
        )

        st.progress(float(probability))

        st.metric(
            "Prediction Confidence",
            f"{confidence:.2%}"
        )

        if probability < 0.25:

            st.success("🟢 Risk Level : Low")

        elif probability < 0.50:

            st.warning("🟡 Risk Level : Medium")

        elif probability < 0.75:

            st.warning("🟠 Risk Level : High")

        else:

            st.error("🔴 Risk Level : Very High")

    # ===============================
    # Transaction Summary
    # ===============================

    with col2:

        st.subheader("📝 Transaction Summary")

        st.dataframe(input_df)

# ==========================================
# FOOTER
# ==========================================

st.markdown("---")

st.caption(
    "Developed by PALSA MANOJ KUMAR | © 2026"
)