import streamlit as st
from ml_model.fraud_detection import predict_fraud

st.title("Paytm UPI Fraud Surveillance")

amount = st.number_input("Amount")

velocity = st.number_input("Velocity")

location_risk = st.selectbox(
"Location Risk",
[0,1]
)

device_change = st.selectbox(
"Device Change",
[0,1]
)

if st.button("Predict"):

    result = predict_fraud(
        amount,
        velocity,
        location_risk,
        device_change
    )

    if result == 1:
        st.error("Fraud Transaction")
    else:
        st.success("Normal Transaction")