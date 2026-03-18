# Import required libraries
import streamlit as st                     # Streamlit for creating the web application
import pandas as pd                        # Pandas for handling data
import os                                  # OS module to check if files exist
from sklearn.model_selection import train_test_split  # Used to split dataset into training and testing sets
from sklearn.linear_model import LinearRegression     # Linear Regression model


# Display the page title
st.title("Model Building")


# ---------------------------------------------------------
# Check if the processed dataset exists
# ---------------------------------------------------------

# If the cleaned dataset exists, load it
if os.path.exists("processed_data.csv"):

    # Read the processed dataset
    df = pd.read_csv("processed_data.csv")

    # Display a preview of the dataset
    st.subheader("Preprocessed Data")
    st.dataframe(df.head())


    # ---------------------------------------------------------
    # Select numeric columns for model building
    # ---------------------------------------------------------

    # Identify numeric columns (only numerical variables can be used in regression)
    numeric_cols = df.select_dtypes(include=["int64", "float64"]).columns.tolist()


    # Ensure there are enough numeric columns for building a model
    if len(numeric_cols) >= 2:

        # Allow the user to select the target variable (the variable to predict)
        target = st.selectbox("Select target variable", numeric_cols)


        # Allow the user to select feature variables (input variables used for prediction)
        features = st.multiselect(
            "Select feature variables",
            [col for col in numeric_cols if col != target]   # Exclude the target column from features
        )


        # Proceed only if at least one feature is selected
        if features:

            # Define input features (X) and target variable (y)
            X = df[features]
            y = df[target]


            # ---------------------------------------------------------
            # Split the dataset into training and testing sets
            # ---------------------------------------------------------

            # 80% of the data is used for training and 20% for testing
            X_train, X_test, y_train, y_test = train_test_split(
                X, y, test_size=0.2, random_state=42
            )


            # ---------------------------------------------------------
            # Train the Linear Regression model
            # ---------------------------------------------------------

            # Create the regression model
            model = LinearRegression()

            # Train the model using the training data
            model.fit(X_train, y_train)


            # ---------------------------------------------------------
            # Evaluate model performance
            # ---------------------------------------------------------

            # Calculate the R² score using the test dataset
            score = model.score(X_test, y_test)

            # Display model performance
            st.subheader("Model Performance")
            st.write("R² Score:", score)


        # If no features are selected
        else:
            st.info("Please select at least one feature.")


    # If there are not enough numeric columns
    else:
        st.error("Not enough numeric columns for model building.")


# If the processed dataset does not exist
else:

    # Ask the user to upload and preprocess the dataset first
    st.warning("Please upload and preprocess the dataset first on the Data Description page.")
