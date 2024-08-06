import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

# Load the Excel data
df = pd.read_excel('global-monthly-temp-anomaly.xlsx', sheet_name='YourSheetName')

# Streamlit app
st.title('Global Monthly Temperature Anomaly')

# Line chart
st.line_chart(df.set_index('Date')['Anomaly'])


