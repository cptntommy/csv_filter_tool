import streamlit as st
import pandas as pd
import os

os.environ['STREAMLIT_SERVER_MAX_UPLOAD_SIZE'] = '1024'

st.title('Data Filtering App')

#debug print to check upload size change works
st.write(f"Max upload size: {os.getenv('STREAMLIT_SERVER_MAX_UPLOAD_SIZE')} MB")

# File upload
uploaded_file = st.file_uploader("Choose a CSV file", type="csv")
if uploaded_file is not None:
    # Read the CSV data into a DataFrame
    df = pd.read_csv(uploaded_file)

    # User inputs for filtering
    column_to_filter = st.selectbox('Select the column to filter on:', df.columns)
    unique_values = df[column_to_filter].unique()
    value_to_filter = st.selectbox(f'Select the value to filter in {column_to_filter}:', unique_values)

    # Filter the DataFrame
    filtered_df = df[df[column_to_filter] == value_to_filter]

    # Display the results
    st.write('Filtered Data:')
    st.dataframe(filtered_df)

    # Convert DataFrame to CSV for download
    def convert_df_to_csv(df):
        return df.to_csv(index=False).encode('utf-8')

    csv = convert_df_to_csv(filtered_df)

    st.download_button(
        label="Download filtered data as CSV",
        data=csv,
        file_name='filtered_data.csv',
        mime='text/csv',
    )
else:
    st.write("Upload a CSV file to get started.")
