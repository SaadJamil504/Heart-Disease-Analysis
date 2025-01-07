import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def dataset_overview():
    st.title("Dataset Overview")

    # Try loading the dataset
    try:
        df = pd.read_csv("heart.csv")

        # Dataset Information
        st.markdown("### **Dataset Summary**")
        st.write(f"**Rows:** {df.shape[0]}, **Columns:** {df.shape[1]}")
        st.write("**Columns:**", ", ".join(df.columns))
        

        # Preview Dataset
        st.markdown("### **Dataset Preview**")
        st.dataframe(df.head())

        # Summary Statistics
        st.markdown("### **Summary Statistics**")
        st.write(df.describe())

        # Check for Missing Data
        st.markdown("### **Missing Data Check**")
        if df.isnull().sum().sum() > 0:
            missing_data = df.isnull().sum()
            st.write("### Missing Values by Column")
            st.write(missing_data[missing_data > 0])
            
            # Visual: Missing Data Heatmap
            st.markdown("### **Missing Data Heatmap**")
            fig, ax = plt.subplots(figsize=(10, 6))  # Increased figure size
            sns.heatmap(df.isnull(), cbar=False, cmap="viridis", ax=ax)
            ax.set_title("Missing Data Heatmap", fontsize=16)
            st.pyplot(fig)
        else:
            st.write("No missing data found.")
    
    except FileNotFoundError:
        st.error("The file 'heart.csv' was not found. Please make sure it exists in the same directory as this script.")
    except Exception as e:
        st.error(f"An error occurred: {e}")

