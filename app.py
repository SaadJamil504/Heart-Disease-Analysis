import streamlit as st
from introduction import introduction
from dataset_overview import dataset_overview
from eda import eda
from machine_learning_model import machine_learning_model
from conclusion_and_insights import conclusion_and_insights

# Dictionary to map page names to functions
pages = {
    "Introduction": introduction,
    "Dataset Overview": dataset_overview,
    "EDA": eda,
    "Machine Learning Model": machine_learning_model,
    "Conclusion and Insights": conclusion_and_insights
}

# Sidebar for navigation
st.sidebar.title("Heart Disease Dataset")
selection = st.sidebar.radio("Go to", list(pages.keys()))

# Display the selected page
pages[selection]()
