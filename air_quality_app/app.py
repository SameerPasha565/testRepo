import streamlit as st

st.set_page_config(
    page_title="Air Quality App",
    page_icon="🌫️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Main page
st.title("🌫️ Air Quality Analytics App")

st.markdown("""
Welcome to the **Air Quality Analytics App**.

This application follows a simple workflow:

1. **Upload Dataset**  
2. **Data Description and Preprocessing**  
3. **Exploratory Data Analysis (EDA)**  
4. **Model Building**
""")

st.info("Use the sidebar to move through the pages in order.")

# -------------------------------
# Sidebar content
# -------------------------------
st.sidebar.title("App Guide")

st.sidebar.markdown("### Workflow Overview")

section = st.sidebar.radio(
    "Choose a stage:",
    (
        "Upload Dataset",
        "Data Description",
        "EDA",
        "Model Building"
    )
)

if section == "Upload Dataset":
    st.sidebar.write("""
    Upload your CSV dataset here first.
    This file will then be used in the next pages.
    """)

elif section == "Data Description":
    st.sidebar.write("""
    View the dataset preview, shape, column names,
    missing values, and preprocessed data.
    """)

elif section == "EDA":
    st.sidebar.write("""
    Explore charts and relationships in the
    cleaned dataset.
    """)

elif section == "Model Building":
    st.sidebar.write("""
    Select features and target variables,
    then train and evaluate a model.
    """)

st.sidebar.markdown("---")
st.sidebar.markdown("### Quick Help")

if st.sidebar.button("How to use this app"):
    st.sidebar.success("""
    Start with Upload Dataset, then continue to
    Data Description, EDA, and Model Building.
    """)

if st.sidebar.button("What data should I upload?"):
    st.sidebar.success("""
    Upload a CSV file with at least a few
    numeric columns for charts and modelling.
    """)

if st.sidebar.button("Why can't I see results yet?"):
    st.sidebar.warning("""
    Make sure you uploaded the dataset first
    and completed the previous page.
    """)

st.markdown("---")
st.caption("Tip: Follow the pages in order using the sidebar.")
