import pandas as pd
import streamlit as st
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



