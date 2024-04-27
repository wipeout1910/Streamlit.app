import streamlit as st
import pandas as pd
import joblib

# Load the trained model
model = joblib.load('Dimas.joblib')

# Function to make predictions
def predict_gender(age, income, family_size, education):
    # Transform input into DataFrame
    input_data = pd.DataFrame({'Age': [age],
                               'Income': [income],
                               'Family Size': [family_size],
                               'Education': [education]})
    # Make prediction
    prediction = model.predict(input_data)
    # Convert prediction to human-readable label
    if prediction[0] == 'M':
        return 'Male'
    else:
        return 'Female'

# Streamlit UI
def main():
    # Page title
    st.title('Gender Prediction App')

    # Input fields
    age = st.slider('Age', min_value=18, max_value=100, value=30, step=1)
    income = st.number_input('Income', value=50000)
    family_size = st.number_input('Family Size', value=2)
    education = st.selectbox('Education', ['High School', 'Bachelor', 'Master', 'PhD'])

    # Predict button
    if st.button('Predict Gender'):
        # Make prediction
        prediction = predict_gender(age, income, family_size, education)
        st.write(f'The predicted gender is: {prediction}')

# Run the app
if __name__ == '__main__':
    main()
