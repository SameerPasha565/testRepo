import streamlit as st   # Streamlit for building the web app
import pandas as pd      # Pandas for data handling
import os                # OS module to check if files exist

# Display the title on the Streamlit page
st.title("Upload Dataset")

# Define the file name where the uploaded dataset will be saved
DATA_PATH = "uploaded_data.csv"

# Create a file uploader widget that accepts CSV files
file = st.file_uploader("Upload CSV dataset", type=["csv"])

# If the user uploads a file
if file is not None:

    # Read the uploaded CSV file into a pandas dataframe
    df = pd.read_csv(file)

    # Save the uploaded dataset to the local folder
    # This allows the app to reuse the dataset even after refresh
    df.to_csv(DATA_PATH, index=False)

    # Show a success message on the app
    st.success("Dataset uploaded successfully!")

    # Display a small section header
    st.subheader("Preview")

    # Show the first 5 rows of the dataset in an interactive table
    st.dataframe(df.head())

# If no file is uploaded but a dataset already exists locally
elif os.path.exists(DATA_PATH):

    # Load the previously saved dataset
    df = pd.read_csv(DATA_PATH)

    # Inform the user that the dataset has already been uploaded earlier
    st.info("Dataset already uploaded")

    # Show preview header
    st.subheader("Preview")

    # Display the first 5 rows of the dataset
    st.dataframe(df.head())

# If no dataset exists and nothing has been uploaded
else:

    # Show a warning asking the user to upload a dataset
    st.warning("Please upload a dataset to begin.")
