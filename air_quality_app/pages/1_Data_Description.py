
# Import required libraries
import streamlit as st   # Streamlit is used to create the web application interface
import pandas as pd      # Pandas is used for data manipulation and analysis
import os                # OS module helps check if files exist in the system


# Display the page title in the Streamlit app
st.title("Data Description")


# Check if the uploaded dataset exists
# If the dataset exists, load it using pandas
if os.path.exists("uploaded_data.csv"):
    df = pd.read_csv("uploaded_data.csv")

# If the dataset does not exist, show a warning message
# and stop the execution of the app
else:
    st.warning("Please upload data first on the Upload Data page.")
    st.stop()


# ---------------------------------------------------------
# Dataset Preview
# ---------------------------------------------------------

# Display a subheader for the dataset preview section
st.subheader("Dataset Preview")

# Show the first 5 rows of the dataset in an interactive table
st.dataframe(df.head())


# ---------------------------------------------------------
# Dataset Shape
# ---------------------------------------------------------

# Display the number of rows and columns in the dataset
st.subheader("Dataset Shape")

# df.shape[0] gives the number of rows
st.write("Rows:", df.shape[0])

# df.shape[1] gives the number of columns
st.write("Columns:", df.shape[1])


# ---------------------------------------------------------
# Column Names
# ---------------------------------------------------------

# Display all column names in the dataset
st.subheader("Column Names")

# Convert column names to a list and display them
st.write(list(df.columns))


# ---------------------------------------------------------
# Missing Values
# ---------------------------------------------------------

# Display the number of missing values in each column
st.subheader("Missing Values")

# df.isnull().sum() counts missing values in each column
# reset_index() converts the result into a dataframe
# rename() changes column names for better readability
st.dataframe(
    df.isnull().sum().reset_index().rename(
        columns={"index": "Column", 0: "Missing Values"}
    )
)


# ---------------------------------------------------------
# Data Preprocessing
# ---------------------------------------------------------

# Create a copy of the dataset and remove rows with missing values
processed_df = df.copy().dropna()

# Save the cleaned dataset for use in other pages of the Streamlit app
processed_df.to_csv("processed_data.csv", index=False)


# ---------------------------------------------------------
# Display the processed dataset
# ---------------------------------------------------------

# Show preview of the cleaned dataset
st.subheader("Preprocessed Dataset Preview")
st.dataframe(processed_df.head())

# Show the shape of the cleaned dataset
st.subheader("Preprocessed Dataset Shape")
st.write("Rows:", processed_df.shape[0])
st.write("Columns:", processed_df.shape[1])
