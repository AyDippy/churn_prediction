import numpy as np
import pickle
import streamlit as st
import sklearn
from sklearn.preprocessing import MinMaxScaler
import joblib
import pandas as pd

loaded_model = pickle.load(open('pls.pkl', 'rb'))
jobless = joblib.load('tire.joblib')

#Creating a function for prediction
def customer_churn(input_data):

    #changing the input data to numpy array
    input_data_as_numpy_array = np.array(input_data)
    # print(input_data_as_numpy_array)

    #reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1, -1)
    column = ['CreditScore', 'Geography', 'Gender', 'Age', 'Tenure', 'Balance','NumOfProducts','HasCrCard', 'IsActiveMember', 'EstimatedSalary']

    trainee = pd.DataFrame(input_data_reshaped, columns = column)
    print(trainee)
    

    prediction = jobless.predict(trainee)

    if prediction[0] == 1:
        return 'The customer is likely to churn'
    elif prediction[0] == 0:
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
    HasCrCard = st.selectbox('Has Credit Card',['Yes', 'No'])
    IsActiveMember = st.selectbox('Active Member', ['Yes','No'])
    EstimatedSalary = st.text_input('Estimated Salary')
    gender = st.selectbox('Gender', ['Male', 'Female'])
    geography = st.selectbox('Location', ['Germany', 'Spain', 'France'])
    try:
    #Coverting strings to integers, as well as floats in some cases
        credit_score_int = int(CreditScore)
        age = int(Age)
        tenure = int(Tenure)
        num_of_products = int(NumOfProducts)
        estimated_salary = float(EstimatedSalary)
        balance = float(Balance)
    except:
        pass
    is_active_member =  []
    has_credit_card = []
    if IsActiveMember == 'Yes':
        is_active_member.append(1)
    else:
        is_active_member.append(0)
    if HasCrCard == 'Yes':
        has_credit_card.append(1)
    else:
        has_credit_card.append(0)


    #code for prediction
    Customer_decison  = ''
    #Creating a button for prediction
    if st.button('Predict Churn'):
        Customer_decison = customer_churn([credit_score_int,geography, gender, age, tenure, balance, num_of_products, has_credit_card[0], is_active_member[0], estimated_salary])

    st.success(Customer_decison)

if __name__ == '__main__':
    main()
        