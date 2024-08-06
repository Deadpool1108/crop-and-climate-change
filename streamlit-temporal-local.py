import pandas as pd
import streamlit as st

file_path = os.path.join(script_dir, 'food-emissions-supply-chain.xlsx') 

food_production = pd.read_excel(file_path) # Use the full file path
def app():
    st.title('Food Emissions Supply Chain')

    st.dataframe(food_production) # Change df to food_production

    # Make sure 'Column1' and 'Column2' exist in your DataFrame
    if 'Column1' in food_production.columns and 'Column2' in food_production.columns: # Change df to food_production
        st.line_chart(food_production.set_index('Column1')['Column2']) # Change df to food_production

if __name__ == "__main__":
    app()
file_path = 'Projected_impacts_datasheet_11.24.2021.xlsx'  


import os
if not os.path.exists(file_path):
    print(f"Error: File not found at {file_path}")
else:
    df = pd.read_excel(file_path)

    def app():
        st.title('Global Monthly Temperature Anomalies')

        regions = df['Entity'].unique()
        selected_region = st.sidebar.selectbox('Select Region', regions)

        region_data = df[df['Entity'] == selected_region]

        st.line_chart(region_data.set_index('Day')['Global warming: monthly temperature anomaly'])

        st.dataframe(region_data)

    if __name__ == "__main__":
        app()
