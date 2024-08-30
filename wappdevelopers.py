import streamlit as st
import numpy as np
import pandas as pd
import joblib

model = joblib.load('xmlpipe1000.joblib')
st.title('Salary Prediction in 2024')
st.write("""### We need some information to predict the salary""")

countries = (
    "United States of America",
    "Other",
    "India",
    "United Kingdom of Great Britain and Northern Ireland",
    "Germany",
    "Canada",
    "Brazil",
    "France",
    "Spain",
    "Australia",
    "Netherlands",
    "Poland",
    "Italy",
    "Sweden",
    "Switzerland",
    "Austria",
)

education = (
    "Post grad" ,
    "Less than a Bachelors",
    "Bachelor’s degree",
    "Master’s degree"
)

age =(
    '25-34 years old' ,
    '35-44 years old' ,
    '45-54 years old' ,
    '18-24 years old' ,
    '55-64 years old' ,
    '65 years or older' ,
    'Under 18 years old ' ,
    'Prefer not to say'
)

remotework =(
    "Hybrid (some remote, some in-person)" ,
    "Remote" ,
    "In-person"
)

mainbranch = (
    'I am a developer by profession' ,
    'I am not primarily a developer, but I write code sometimes as part of my work/studies' ,
    'I am learning to code' ,
    'I code primarily as a hobby' ,
    'I used to be a developer by profession, but no longer am'
)
country_ = st.selectbox("Country", countries)
education_ = st.selectbox("Education Level", education)
expericence_ = st.slider("Years of Experience", 0, 50, 3)
age_ = st.selectbox("your age",age)
remotework_ = st.selectbox("remote work" , remotework)
mainbranch_ = st.selectbox("mani branch" , mainbranch)
#expericencepro = st.slider("Years of Experience", 0, 50, 3)

columns = ['Country', 'EdLevel', 'YearsCodePro','Age','RemoteWork','MainBranch']

ok = st.button("Calculate Salary")
if ok:
    #X_new = np.array([countries,education,expericence,age,remotework])
    X_df = np.array([country_,education_,expericence_,age_,remotework_,mainbranch_])
    X_new_df = pd.DataFrame([X_df], columns = columns)
    salary = model.predict(X_new_df)
    
    st.subheader(f"The estimated salary is ${salary[0]:.2f}")\

