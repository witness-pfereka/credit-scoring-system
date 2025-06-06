import streamlit as st
import joblib
import pandas as pd

# Load model
model = joblib.load("credit_model2.pkl")

st.set_page_config(page_title="Credit Scoring System", layout="centered")
st.title("📊 Credit Score Prediction")

# Define input fields
def user_input():
    Age = st.number_input("Age", 18, 100, 30)
    Annual_Income = st.number_input("Annual Income", 1000, 1000000, 50000)
    Num_Bank_Accounts = st.slider("Number of Bank Accounts", 0, 10, 2)
    Num_Credit_Card = st.slider("Number of Credit Cards", 0, 10, 2)
    Interest_Rate = st.slider("Interest Rate", 0, 100, 10)
    Num_of_Loan = st.slider("Number of Loans", 0, 10, 1)
    Delay_from_due_date = st.number_input("Delay from Due Date", 0, 100, 10)
    Num_of_Delayed_Payment = st.number_input("Number of Delayed Payments", 0, 100, 5)
    Changed_Credit_Limit = st.number_input("Changed Credit Limit", 0.0, 1000000.0, 20000.0)
    Credit_Mix = st.selectbox("Credit Mix", ['Good', 'Standard', 'Bad'])
    Outstanding_Debt = st.number_input("Outstanding Debt", 0.0, 1000000.0, 50000.0)
    Credit_Utilization_Ratio = st.slider("Credit Utilization Ratio", 0.0, 1.0, 0.3)
    Credit_History_Age = st.slider("Credit History Age (months)", 0, 600, 60)
    
    data = {
        'Age': Age,
        'Annual_Income': Annual_Income,
        'Num_Bank_Accounts': Num_Bank_Accounts,
        'Num_Credit_Card': Num_Credit_Card,
        'Interest_Rate': Interest_Rate,
        'Num_of_Loan': Num_of_Loan,
        'Delay_from_due_date': Delay_from_due_date,
        'Num_of_Delayed_Payment': Num_of_Delayed_Payment,
        'Changed_Credit_Limit': Changed_Credit_Limit,
        'Credit_Mix': Credit_Mix,
        'Outstanding_Debt': Outstanding_Debt,
        'Credit_Utilization_Ratio': Credit_Utilization_Ratio,
        'Credit_History_Age': Credit_History_Age
    }

    return pd.DataFrame([data])

input_df = user_input()

if st.button("Predict Credit Score"):
    prediction = model.predict(input_df)[0]
    mapping = {0: "Poor", 1: "Standard", 2: "Good"}
    st.success(f"✅ Predicted Credit Score: **{mapping[prediction]}**")
