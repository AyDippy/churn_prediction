import numpy as np
import pickle
import streamlit as st
import sklearn
from sklearn.preprocessing import LabelEncoder, MinMaxScaler

loaded_model = pickle.load(open('trained_model.pkl', 'rb'))

# Creating a function for prediction
def customer_churn(input_data):
    # Changing the input data to numpy array
    input_data_as_numpy_array = np.asarray(input_data)

    # Reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1, -1)

    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)

    if prediction[0] == 1:
        return 'The customer is likely to churn'
    else:
        return 'The customer is likely to stay'


def main():
    # Giving a title for our interface
    st.title('Customer Churn Prediction Web App')

    # Getting the input from the user
    # Columns: 'CreditScore', 'Age', 'Tenure', 'Balance', 'NumOfProducts', 'HasCrCard',
    # 'IsActiveMember', 'EstimatedSalary', 'gender', 'geography

    # Load the LabelEncoder for gender and geography
    gender_label_encoder = LabelEncoder()
    gender_label_encoder.classes_ = np.array(['female', 'male'])  # Reversing the order for label encoding

    geography_label_encoder = LabelEncoder()
    geography_label_encoder.classes_ = np.array(['France', 'Germany', 'Spain'])  # Setting correct classes for encoding

    CreditScore = st.text_input('Credit Score')
    Age = st.text_input("Customer's Age")
    Tenure = st.text_input('Tenure')
    Balance = st.text_input("Customer's Balance")
    NumOfProducts = st.text_input('Number of Products Used')
    HasCrCard = st.text_input('Has Credit Card')
    IsActiveMember = st.text_input('Active Member')
    EstimatedSalary = st.text_input('Estimated Salary')
    gender = st.selectbox('Gender', ['female', 'male'])  # Use a dropdown for gender
    geography = st.selectbox('Location', ['France', 'Germany', 'Spain'])  # Use a dropdown for geography

    # Convert gender and geography using LabelEncoder
    gender_encoded = gender_label_encoder.transform([gender])[0]
    geography_encoded = geography_label_encoder.transform([geography])[0]

    # Apply MinMaxScaler to the numerical inputs
    numerical_inputs = [CreditScore, Age, Tenure, Balance, NumOfProducts, HasCrCard, IsActiveMember, EstimatedSalary]
    numerical_inputs = [float(val) for val in numerical_inputs]  # Convert to float
    numerical_inputs_as_array = np.asarray(numerical_inputs).reshape(1, -1)

    # Convert gender_encoded and geography_encoded to 2D arrays
    gender_encoded = np.array([[gender_encoded]])
    geography_encoded = np.array([[geography_encoded]])

    # Concatenate all inputs for prediction
    input_data = np.concatenate([numerical_inputs_as_array, gender_encoded, geography_encoded], axis=1)

    # Code for prediction
    Customer_decision = ''
    # Creating a button for prediction
    if st.button('Predict Churn'):
        Customer_decision = customer_churn(input_data)

    st.success(Customer_decision)


if __name__ == '__main__':
    main()
