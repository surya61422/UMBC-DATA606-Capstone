import streamlit as st
import pandas as pd
import numpy as np
import joblib

# Load the trained model
model = joblib.load('logestic_regre_loan.pkl')

# Load the scaler
scaler = joblib.load('scaler.pkl')

def predict_loan_acceptance(new_data):
    # Scale the input data
    new_data_scaled = scaler.transform(new_data)
    # Make prediction
    prediction = model.predict(new_data_scaled)
    return prediction[0]

def main():
    st.title("Personal Loan Acceptance Prediction")
    st.sidebar.title("User Input")

    # Define input fields
    age = st.sidebar.number_input("Age", min_value=18, max_value=100, value=25)
    experience = st.sidebar.number_input("Experience", min_value=-30, max_value=50, value=10)
    income = st.sidebar.number_input("Income", min_value=0, max_value=500, value=50)
    family = st.sidebar.selectbox("Family Size", [1, 2, 3, 4])
    cc_avg = st.sidebar.number_input("CCAvg", min_value=0.0, max_value=10.0, value=2.0)
    education = st.sidebar.selectbox("Education Level", [1, 2, 3])
    mortgage = st.sidebar.number_input("Mortgage", min_value=0, max_value=1000, value=50)
    yes_no_options = {0: "No", 1: "Yes"}
    securities_account = st.sidebar.selectbox("Securities Account", options=list(yes_no_options.values()))
    cd_account = st.sidebar.selectbox("CD Account", options=list(yes_no_options.values()))
    online = st.sidebar.selectbox("Online", options=list(yes_no_options.values()))
    credit_card = st.sidebar.selectbox("Credit Card", options=list(yes_no_options.values()))

    # Create a dictionary with user input
    new_data = {
        'Age': [age],
        'Experience': [experience],
        'Income': [income],
        'Family': [family],
        'CCAvg': [cc_avg],
        'Education': [education],
        'Mortgage': [mortgage],
        'Securities Account': [list(yes_no_options.keys())[list(yes_no_options.values()).index(securities_account)]],
        'CD Account': [list(yes_no_options.keys())[list(yes_no_options.values()).index(cd_account)]],
        'Online': [list(yes_no_options.keys())[list(yes_no_options.values()).index(online)]],
        'CreditCard': [list(yes_no_options.keys())[list(yes_no_options.values()).index(credit_card)]]
    }

    # Convert dictionary to DataFrame
    new_df = pd.DataFrame(new_data)

    # Predict button
    if st.sidebar.button("Predict"):
        # Make prediction
        prediction = predict_loan_acceptance(new_df)

        # Show prediction result
        st.write("## Prediction Result")
        if prediction == 1:
            st.write("Congratulations! You're likely to be accepted for a personal loan.")
        else:
            st.write("Sorry! You're unlikely to be accepted for a personal loan.")

if __name__ == "__main__":
    main()
