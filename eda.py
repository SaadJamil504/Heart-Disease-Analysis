import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def plot_correlation_heatmap(df):
    st.markdown("### **Correlation Heatmap**")
    # Select only numerical columns for correlation
    numerical_columns = df.select_dtypes(include=["float64", "int64"]).columns
    corr = df[numerical_columns].corr()

    # Create the heatmap
    fig, ax = plt.subplots(figsize=(8, 6))
    sns.heatmap(
        corr, annot=True, fmt=".2f", cmap="viridis", cbar=True,
        annot_kws={"size": 10}, linewidths=0.5, ax=ax
    )
    ax.set_title("Feature Correlation Heatmap", fontsize=14, pad=10)
    plt.xticks(rotation=45, ha="right", fontsize=10)
    plt.yticks(fontsize=10)
    st.pyplot(fig)

def plot_target_relationships(df, target_col="target"):
    st.markdown("### **Target Relationships with Selected Features (Countplots)**")
    
    # List of specified columns to analyze
    selected_columns = ['age', 'sex', 'cp', 'fbs', 'restecg', 'exang', 'oldpeak', 'slope', 'ca', 'thal']
    
    # Check if all selected columns exist in the DataFrame
    selected_columns = [col for col in selected_columns if col in df.columns]
    
    # Plot relationship between each selected column and the target variable
    for col in selected_columns:
        plt.figure(figsize=(10, 6))
        
        # Create countplot for each column
        sns.countplot(data=df, x=col, hue=target_col, palette="pastel")
        plt.title(f"{col} vs {target_col}", fontsize=16)
        plt.xlabel(col, fontsize=12)
        plt.ylabel("Count", fontsize=12)
        
        # Display plot in Streamlit
        st.pyplot(plt)

def eda():
    st.title("Exploratory Data Analysis (EDA)")

    # Load the dataset
    try:
        df = pd.read_csv("heart.csv")
        st.markdown("### **Dataset Overview**")
        st.dataframe(df.head())

        # Correlation Heatmap
        plot_correlation_heatmap(df)

        # Target Relationships
        if "target" in df.columns:
            plot_target_relationships(df, target_col="target")
        else:
            st.warning("The dataset does not contain a 'target' column.")
    except FileNotFoundError:
        st.error("The file 'heart.csv' was not found. Make sure it exists in the same directory as this script.")

if __name__ == "__main__":
    eda()
