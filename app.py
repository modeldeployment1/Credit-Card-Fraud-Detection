
import streamlit as st
import pandas as pd
import joblib  # or use 'pickle' if preferred

# Title of the app
st.title("Credit Card Fraud Detection")

# Subtitle or description
st.write("This app predicts whether a transaction is fraudulent or not using a trained Random Forest model.")

# Load your pre-trained model
# Replace 'model.pkl' with your actual model file name
model = joblib.load('model.pkl')

# Create input fields for user to input data for prediction
st.write("Please provide the input features below:")

# Feature input fields (without default values)
Time = st.number_input("Time")
V1 = st.number_input("V1")
V2 = st.number_input("V2")
V3 = st.number_input("V3")
V4 = st.number_input("V4")
V5 = st.number_input("V5")
V6 = st.number_input("V6")
V7 = st.number_input("V7")
V8 = st.number_input("V8")
V9 = st.number_input("V9")
V10 = st.number_input("V10")
V11 = st.number_input("V11")
V12 = st.number_input("V12")
V13 = st.number_input("V13")
V14 = st.number_input("V14")
V15 = st.number_input("V15")
V16 = st.number_input("V16")
V17 = st.number_input("V17")
V18 = st.number_input("V18")
V19 = st.number_input("V19")
V20 = st.number_input("V20")
V21 = st.number_input("V21")
V22 = st.number_input("V22")
V23 = st.number_input("V23")
V24 = st.number_input("V24")
V25 = st.number_input("V25")
V26 = st.number_input("V26")
V27 = st.number_input("V27")
V28 = st.number_input("V28")
Hour = st.number_input("Hour")
Is_Weekend = st.number_input("Is_Weekend")
Log_Amount = st.number_input("Log_Amount")

# When the "Predict" button is pressed
if st.button("Predict"):
    # Create a DataFrame with the input data
    input_data = pd.DataFrame([[Time, V1, V2, V3, V4, V5, V6, V7, V8, V9, V10, 
                                V11, V12, V13, V14, V15, V16, V17, V18, V19, 
                                V20, V21, V22, V23, V24, V25, V26, V27, V28, 
                                Hour, Is_Weekend, Log_Amount]],
                              columns=['Time', 'V1', 'V2', 'V3', 'V4', 'V5', 
                                       'V6', 'V7', 'V8', 'V9', 'V10', 'V11', 
                                       'V12', 'V13', 'V14', 'V15', 'V16', 
                                       'V17', 'V18', 'V19', 'V20', 'V21', 
                                       'V22', 'V23', 'V24', 'V25', 'V26', 
                                       'V27', 'V28', 'Hour', 'Is_Weekend', 
                                       'Log_Amount'])

    st.write("Input Data:")
    st.write(input_data)

# Make a prediction using the loaded model
    try:
        prediction = model.predict(input_data)
        st.write(f"Prediction: {prediction[0]}")
        if prediction[0] == 1:
            st.write("The model predicts that the transaction is **fraudulent**.")
        else:
            st.write("The model predicts that the transaction is **not fraudulent**.")
    except Exception as e:
        st.error(f"Error making prediction: {e}")
