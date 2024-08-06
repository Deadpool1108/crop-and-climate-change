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