import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

# Load the Excel data
df = pd.read_excel('food-emissions-supply-chain.xlsx', sheet_name='Data')

# Streamlit app
st.title('Food Emissions Supply Chain Analysis')

# Selectbox for food category
food_category = st.selectbox('Select Food Category', df['FoodCategory'].unique())

# Filter data based on selected food category
filtered_df = df[df['FoodCategory'] == food_category]

# Create bar chart
plt.figure(figsize=(10, 6))
plt.bar(filtered_df['EmissionType'], filtered_df['Value'])
plt.xlabel('Emission Type')
plt.ylabel('Emission Value')
plt.title(f'Emissions for {food_category}')
plt.xticks(rotation=45)
st.pyplot(plt)

