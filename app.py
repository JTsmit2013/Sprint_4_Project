import streamlit as st
import pandas as pd

# Load data
df = pd.read_csv('vehicles_us.csv')

# Debugging: Print initial data types and first few rows
st.write("Original DataFrame info:")
st.write(df.info())
st.write(df['price'].head())  # Display the first few rows of the `price` column

# Function to safely coerce columns to numeric
def safe_numeric(df, column):
    st.write(f"Processing column: {column}")
    df[column] = pd.to_numeric(df[column], errors='coerce')
    df[column] = df[column].fillna(0)  # Or some other appropriate value
    st.write(df[column].head())  # Display the first few rows after conversion
    return df

# Clean and convert data
df = safe_numeric(df, 'price')

# Additional check for NaNs after conversion
st.write("DataFrame info after conversion of `price` column:")
st.write(df.info())
st.write(df['price'].head())  # Display the first few rows to verify

# Debugging: Print column types to identify any inconsistencies
st.write("Data types after conversion:")
st.write(df.dtypes)

# Further check for remaining NaNs
st.write("Summary of NaNs in DataFrame:")
st.write(df.isna().sum())

# Render Raw Data
st.header('Raw Vehicle Data')
st.dataframe(df)
