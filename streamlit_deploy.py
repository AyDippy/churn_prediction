import numpy as np
import pickle
import streamlit as st
import sklearn

loaded_model = pickle.load(open('trained_model.pkl', 'rb'))

#Creating a function for prediction
def customer_churn(input_data):

    #changing the input data to numpy array
    input_data_as_numpy_array = np.asarray(input_data)

    #reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

    prediction = loaded_model.predict(input_data_reshaped)
    
    if (prediction[0] == 1):
        return 'The customer is likely to churn'
    else:
        return 'The customer is likely to stay'
    
def main():

    #Giving a title for our interface
    st.title('Customer Churn Prediction Web App')

    #getting the input from the user
    #Columns: 'CreditScore', 'Age', 'Tenure', 'Balance', 'NumOfProducts', 'HasCrCard',
    #'IsActiveMember', 'EstimatedSalary', 'gender', 'geography
    CreditScore = st.text_input('Credit Score')
    Age = st.text_input("Customer's Age")
    Tenure = st.text_input('Tenure')
    Balance = st.text_input("Customer's Balance")
    NumOfProducts = st.text_input('Number of Products Used')
    HasCrCard = st.text_input('Has Credit Card')
    IsActiveMember = st.text_input('Active Member')
    EstimatedSalary = st.text_input('Estimated Salary')
    gender = st.text_input('Gender')
    geography = st.text_input('Location')


    #code for prediction
    Customer_decison  = ''
    #Creating a button for prediction
    if st.button('Predict Churn'):
        Customer_decison = customer_churn([CreditScore,Age,Tenure,Balance, NumOfProducts, HasCrCard, IsActiveMember, EstimatedSalary,gender, geography])

    st.success(Customer_decison)


if __name__ == '__main__':
    main()
        