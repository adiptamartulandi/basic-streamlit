#load libraries
import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(layout="wide")

# st.markdown(
#     """
#     <style>
#     .stApp {
#         background-color: #34aeeb;
#     }
#     </style>
#     """,
#     unsafe_allow_html=True
# )

#title
st.title("Titanic Exploratory Data Analysis")

#create section to upload files
st.write("")

#upload files
uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write("Upload complete")

#create separator
st.write("")

#button to display dataframe
if st.button("Display Dataframe"):
    st.dataframe(df)

#create separator
st.write("")

#button to show general information of data
if st.button("Show General Information"):
    st.write("Number of columns and rows")
    st.write(df.shape)
    
    st.write("Column names")
    st.write(df.columns)
    
    st.write("Data types")
    st.write(df.dtypes)
    
    #missing values
    st.write("Missing values")
    st.write(df.isnull().sum())
    
    #data duplicates
    st.write("Duplicate data")
    st.write(df.duplicated().sum())
    
    st.write("First 5 rows")
    st.write(df.head())
    
    st.write("Last 5 rows")
    st.write(df.tail())

#create separator
st.write("")

#button to show summary statistics
if st.button("Show Summary Statistics"):
    st.write("Summary statistics")
    st.write(df.describe())
    
#button to plot histogram
if st.button("Plot Histogram"):
    
    #create separator
    left_column, right_column = st.columns(2)

    # You can use a column just like st.sidebar:
    with left_column:
        st.write("Histogram of Sex")
        st.bar_chart(df['Sex'].value_counts())

    # Or even better, call Streamlit functions inside a "with" block:
    with right_column:
        st.write("Histogram of Age")
        st.bar_chart(df['Age'].value_counts())
        
    #create separator
    st.write("")
    
#change color theme of background
