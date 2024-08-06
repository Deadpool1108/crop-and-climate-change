import pandas as pd
import streamlit as st
import plotly.express as px
import matplotlib.pyplot as plt
# Load the Excel data
df = pd.read_excel('global-monthly-temp-anomaly.xlsx', sheet_name='YourSheetName')

# Convert date column to datetime
df['Date'] = pd.to_datetime(df['Date'])

# Streamlit app
st.title('Global Monthly Temperature Anomaly')

# User input for year range
year_range = st.slider('Select Year Range', min_value=df['Date'].dt.year.min(),
                       max_value=df['Date'].dt.year.max(), value=[df['Date'].dt.year.min(), df['Date'].dt.year.max()])

# Filter data based on year range
filtered_df = df[(df['Date'].dt.year >= year_range[0]) & (df['Date'].dt.year <= year_range[1])]

# Create interactive line chart
fig = px.line(filtered_df, x='Date', y='Anomaly', title='Global Monthly Temperature Anomaly')
st.plotly_chart(fig)
