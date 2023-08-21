# Customer Churn Prediction Project

This README file provides an overview of the **Customer Churn Prediction** machine learning project. The project focuses on predicting the likelihood of a customer leaving a bank using a variety of features. It includes exploratory data analysis, preprocessing, model training, hyperparameter tuning, and deployment.

## Table of Contents

- [Project Overview](#project-overview)
- [Exploratory Data Analysis](#exploratory-data-analysis)
- [Preprocessing](#preprocessing)
- [Model Training](#model-training)
- [Hyperparameter Tuning](#hyperparameter-tuning)
- [Deployment](#deployment)

## Project Overview

The goal of this project is to predict the likelihood of a customer leaving a bank using a machine learning model. The dataset includes features such as 'CreditScore', 'Geography', 'Gender', 'Age', 'Tenure', 'Balance', 'NumOfProducts', 'HasCrCard', 'IsActiveMember', and 'EstimatedSalary'. The project encompasses data analysis, preprocessing, model training, hyperparameter tuning, and deployment.

## Exploratory Data Analysis

During exploratory data analysis, key insights were derived from the dataset:

- Customers between the ages of 35 and 45 are more likely to stay compared to older customers.
- Females tend to churn more.
- Customers in Germany have a higher churn rate.

## Preprocessing

Data preprocessing involved several steps:

1. Splitting numerical and categorical features.
2. Applying OneHotEncoder to categorical features.
3. Applying StandardScaler to numerical features.
4. Creating a pipeline that includes preprocessing and oversampling using the Smote Tomek model from imblearn.

## Model Training

Multiple machine learning models were trained and evaluated:

- Logistic Regression
- XGBoost
- Random Forest Classifier

XGBoost exhibited the highest accuracy on both the training and test datasets, making it the preferred choice for this project.

## Hyperparameter Tuning

Hyperparameter tuning was performed on the XGBoost model to optimize its performance. This process involved systematically adjusting model parameters to achieve better predictive accuracy.

## Deployment

The final trained XGBoost model, along with the preprocessing steps, was encapsulated in a pipeline. This pipeline was saved using the joblib library. The model was then deployed on a Streamlit web application to enable user-friendly predictions.

## Usage

To replicate this project:

1. Clone this repository.
2. Install the required libraries specified in the `requirements.txt` file.
3. Review the Jupyter Notebook or Python script for code details and explanations.
4. Run the preprocessing steps and model training sections to reproduce the model.
5. Adjust the Streamlit application code to suit your deployment environment.

## File Structure

- `data/`: Directory containing the dataset and related files.
- `notebooks/`: Jupyter Notebook files documenting the exploratory data analysis, preprocessing, and model training.
- `scripts/`: Python scripts containing the final model and deployment code.
- `app/`: Directory containing the Streamlit application files.

## Credits

- Author: Ayomide Dipeolu
- Contact: ayomidedipeolu@gmail.com

## License

This project is licensed under the [MIT License](LICENSE).
