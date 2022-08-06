import streamlit as st
import pickle
import numpy as np

def load_random_forest_model():
    with open("saved_steps_random_forest.pkl", "rb") as file:
        data = pickle.load(file)
    
    return data

def load_linear_regression_model():
    with open("saved_steps_linear_regression.pkl", "rb") as file:
        data = pickle.load(file)
    
    return data

def load_decision_tree_model(): 
    with open("saved_steps.pkl", "rb") as file:
        data = pickle.load(file)
    
    return data

def show_predict_page_linear_regression():

    data = load_linear_regression_model()
    regressor = data["model"]
    le_country = data["le_country"]
    le_education = data["le_education"]
    st.title("Sofware Developer Salary Prediction")

    st.write("### We need more information to predict the salary")

    countries = (
        "United States of America",
        "India",
        "Germany",
        "United Kingdom of Great Britain and Northern Ireland",
        "Canada",
        "France",
        "Brazil",
        "Spain",
        "Netherlands",
        "Australia",
        "Poland",
        "Italy",
        "Russian Federation",
        "Sweden",
        "Turkey",
        "Switzerland",
        "Israel",
        "Norway",
    )

    education = (
        "Master's degree",
        "Bachelor's degree",
        "Post grad",
        "Less than a Bachelor's",
    )

    country = st.selectbox("Country", countries)
    education = st.selectbox("Education", education)
    experience = st.slider("Years of Experience", 0, 50, 1)
    ok = st.button("Calculate Salary")

    if ok:
        X = np.array([[country, education, experience]])
        X[:, 0] = le_country.transform(X[:,0])
        X[:, 1] = le_education.transform(X[:,1])

        X = X.astype(float)    
        salary = regressor.predict(X)

        st.subheader(f"The estimated salary is $ {salary[0]:.2f}")

def show_predict_page_random_forest():

    data = load_random_forest_model()
    regressor = data["model"]
    le_country = data["le_country"]
    le_education = data["le_education"]
    st.title("Sofware Developer Salary Prediction")

    st.write("### We need more information to predict the salary")

    countries = (
        "United States of America",
        "India",
        "Germany",
        "United Kingdom of Great Britain and Northern Ireland",
        "Canada",
        "France",
        "Brazil",
        "Spain",
        "Netherlands",
        "Australia",
        "Poland",
        "Italy",
        "Russian Federation",
        "Sweden",
        "Turkey",
        "Switzerland",
        "Israel",
        "Norway",
    )

    education = (
        "Master's degree",
        "Bachelor's degree",
        "Post grad",
        "Less than a Bachelor's",
    )

    country = st.selectbox("Country", countries)
    education = st.selectbox("Education", education)
    experience = st.slider("Years of Experience", 0, 50, 1)
    ok = st.button("Calculate Salary")

    if ok:
        X = np.array([[country, education, experience]])
        X[:, 0] = le_country.transform(X[:,0])
        X[:, 1] = le_education.transform(X[:,1])

        X = X.astype(float)    
        salary = regressor.predict(X)

        st.subheader(f"The estimated salary is $ {salary[0]:.2f}")

def show_predict_page_decision_tree():

    data = load_decision_tree_model()
    regressor = data["model"]
    le_country = data["le_country"]
    le_education = data["le_education"]
    st.title("Sofware Developer Salary Prediction")

    st.write("### We need more information to predict the salary")

    countries = (
        "United States of America",
        "India",
        "Germany",
        "United Kingdom of Great Britain and Northern Ireland",
        "Canada",
        "France",
        "Brazil",
        "Spain",
        "Netherlands",
        "Australia",
        "Poland",
        "Italy",
        "Russian Federation",
        "Sweden",
        "Turkey",
        "Switzerland",
        "Israel",
        "Norway",
    )

    education = (
        "Master's degree",
        "Bachelor's degree",
        "Post grad",
        "Less than a Bachelor's",
    )

    country = st.selectbox("Country", countries)
    education = st.selectbox("Education", education)
    experience = st.slider("Years of Experience", 0, 50, 1)
    ok = st.button("Calculate Salary")

    if ok:
        X = np.array([[country, education, experience]])
        X[:, 0] = le_country.transform(X[:,0])
        X[:, 1] = le_education.transform(X[:,1])

        X = X.astype(float)    
        salary = regressor.predict(X)

        st.subheader(f"The estimated salary is $ {salary[0]:.2f}")