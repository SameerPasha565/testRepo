# Import required libraries
import streamlit as st   # Streamlit is used to build the interactive web app
import pandas as pd      # Pandas is used for data manipulation
import os                # OS module helps check if files exist


# Display the page title
st.title("Exploratory Data Analysis")


# ---------------------------------------------------------
# Check if the processed dataset exists
# ---------------------------------------------------------

# If the cleaned dataset is available, load it
if os.path.exists("processed_data.csv"):

    # Read the preprocessed dataset
    df = pd.read_csv("processed_data.csv")

    # Display a preview of the dataset
    st.subheader("Preprocessed Data Preview")
    st.dataframe(df.head())


    # ---------------------------------------------------------
    # Select numeric columns for analysis
    # ---------------------------------------------------------

    # Identify numeric columns in the dataset
    # Only numerical columns are suitable for charts and correlation analysis
    numeric_cols = df.select_dtypes(include=["int64", "float64"]).columns.tolist()


    # Check if numeric columns exist
    if numeric_cols:

        # ---------------------------------------------------------
        # Single column visualisations
        # ---------------------------------------------------------

        # Create a dropdown menu for selecting a numeric column
        column = st.selectbox("Select a column", numeric_cols)

        # Display a bar chart for the selected column
        st.subheader("Bar Chart")
        st.bar_chart(df[column])

        # Display a line chart for the selected column
        st.subheader("Line Chart")
        st.line_chart(df[column])


        # ---------------------------------------------------------
        # Scatter plot (relationship between two variables)
        # ---------------------------------------------------------

        # Create dropdown menus for selecting X and Y axes
        x_axis = st.selectbox("Select X-axis", numeric_cols, index=0)
        y_axis = st.selectbox("Select Y-axis", numeric_cols, index=min(1, len(numeric_cols)-1))

        # Ensure the same column is not selected for both axes
        if x_axis != y_axis:

            # Display scatter plot showing relationship between two variables
            st.subheader("Scatter Plot")
            st.scatter_chart(df[[x_axis, y_axis]])


        # ---------------------------------------------------------
        # Correlation Matrix
        # ---------------------------------------------------------

        # Display correlation matrix for all numeric columns
        # Correlation shows relationships between variables (-1 to +1)
        st.subheader("Correlation Matrix")
        st.dataframe(df[numeric_cols].corr())


    # If no numeric columns are found
    else:
        st.error("No numeric columns found in the dataset.")


# If the processed dataset does not exist
else:

    # Ask the user to upload and preprocess the dataset first
    st.warning("Please upload and preprocess the dataset first on the Data Description page.")
