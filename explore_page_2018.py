import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def shorten_categories(categories, cutoff):
    categorical_map = {}
    for i in range(len(categories)):
        if categories.values[i] >= cutoff:
            categorical_map[categories.index[i]] = categories.index[i]
        else:
            categorical_map[categories.index[i]] = "Other"
    
    return categorical_map

def clean_experience(x):
    if x == "30 or more years":
        return 31
    elif x == "6-8 years":
        return 7
    elif x == "9-11 years":
        return 10
    elif x == "15-17 years":
        return 16
    elif x == "18-20 years":
        return 19
    elif x == "3-5 years":
        return 4
    elif x == "12-14 years":
        return 13
    elif x == "0-2 years":
        return 1
    elif x == "24-26 years":
        return 25
    elif x == "21-23 years":
        return 22
    elif x == "27-29 years":
        return 28
    return float(x)

def clean_education(x):
    if "Bachelor’s degree" in x:
        return "Bachelor's degree"
    if "Master’s degree" in x:
        return "Master's degree"
    if "Professional degree" in x or "doctoral degree" in x:
        return "Post grad"
    return "Less than a Bachelor's"

@st.cache
def load_data():
    df = pd.read_csv("datasets/salaries/survey_results_public_2018.csv")
    df = df[["Country","FormalEducation", "YearsCoding", "Employment", "ConvertedSalary"]]
    df= df.rename({"ConvertedSalary": "Salary", "FormalEducation": "EdLevel", "YearsCoding": "YearsCodePro"}, axis =1)
    df = df[df["Salary"].notnull()]
    df = df.dropna()
    df = df[df["Employment"] == "Employed full-time"]
    df = df.drop("Employment", axis =1)
    df["Country"] = df["Country"].apply(lambda x: x.replace("United States", "United States of America"))
    country_map = shorten_categories(df.Country.value_counts(), 400)  
    df["Country"] = df["Country"].map(country_map)
    df = df[df["Salary"] <= 250000]
    df = df[df["Salary"] >= 10000]
    df = df[df["Country"] != "Other"]
    df["YearsCodePro"] = df["YearsCodePro"].apply(clean_experience)
    return df

df = load_data()

def show_explore_page():
    st.title("Sofware Developer Salary Prediction")

    st.write("### We need more information to predict the salary")

    data = df["Country"].value_counts()

    fig1, ax1 = plt.subplots()
    ax1.pie(data, labels = data.index, autopct = "%1.1f%%", shadow = True, startangle = 90)
    ax1.axis("equal") #Equal aspect ratio, ensures that pie is drawn as a circle

    st.write("""### Number of Data from Different Countries""")

    st.pyplot(fig1)

    st.write(""" ### Mean Salary Based on Country""")

    data = df.groupby(["Country"])["Salary"].mean().sort_values(ascending= True)

    st.bar_chart(data)

    st.write("""### Mean Salary Based on Experience""")

    data = df.groupby(["YearsCodePro"])["Salary"].mean().sort_values(ascending = True)

    st.line_chart(data)