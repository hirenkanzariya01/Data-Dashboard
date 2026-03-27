import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(layout="wide")
st.title("📊 AI Data Analysis Dashboard")

# Sidebar Upload
st.sidebar.header("Upload CSV File")
file = st.sidebar.file_uploader("Upload your dataset")

if file:
    data = pd.read_csv(file)

    # Tabs
    tab1, tab2, tab3, tab4 = st.tabs([
        "📄 Overview",
        "🧾 Missing Values",
        "📈 Visualization",
        "🔥 Correlation"
    ])

    # =========================
    # 📄 TAB 1: OVERVIEW
    # =========================
    with tab1:
        st.subheader("Dataset Overview")

        col1, col2 = st.columns(2)

        with col1:
            st.write("Shape:", data.shape)
            st.write("Columns:", list(data.columns))

        with col2:
            st.write("Data Types:")
            st.write(data.dtypes)

        st.subheader("Preview Data")
        st.dataframe(data.head())

        st.subheader("Statistical Summary")
        st.dataframe(data.describe())

    # =========================
    # 🧾 TAB 2: MISSING VALUES
    # =========================
    with tab2:
        st.subheader("Missing Values Analysis")

        missing = data.isnull().sum()
        missing = missing[missing > 0]

        if len(missing) == 0:
            st.success("No Missing Values 🎉")
        else:
            st.dataframe(missing)

            fig, ax = plt.subplots()
            missing.plot(kind='bar', ax=ax)
            plt.title("Missing Values Count")
            st.pyplot(fig)

    # =========================
    # 📈 TAB 3: VISUALIZATION
    # =========================
    with tab3:
        st.subheader("Smart Visualization")

        numeric_cols = data.select_dtypes(include=np.number).columns
        categorical_cols = data.select_dtypes(include='object').columns

        chart_type = st.selectbox(
            "Select Chart Type",
            ["Histogram", "Boxplot", "Bar Chart"]
        )

        col = st.selectbox("Select Column", data.columns)

        fig, ax = plt.subplots()

        if chart_type == "Histogram":
            data[col].hist(ax=ax)
            plt.title(f"Histogram of {col}")

        elif chart_type == "Boxplot":
            sns.boxplot(x=data[col], ax=ax)
            plt.title(f"Boxplot of {col}")

        elif chart_type == "Bar Chart":
            data[col].value_counts().plot(kind='bar', ax=ax)
            plt.title(f"Bar Chart of {col}")

        st.pyplot(fig)

        # 🔥 Auto Visualization for all numeric columns
        st.subheader("Auto Plots (All Numeric Columns)")

        for col in numeric_cols:
            fig, ax = plt.subplots()
            data[col].hist(ax=ax)
            plt.title(f"{col} Distribution")
            st.pyplot(fig)

    # =========================
    # 🔥 TAB 4: CORRELATION
    # =========================
    with tab4:
        st.subheader("Correlation Heatmap")

        corr = data.corr(numeric_only=True)

        fig, ax = plt.subplots(figsize=(10, 6))
        sns.heatmap(corr, annot=True, cmap="coolwarm", ax=ax)
        st.pyplot(fig)

else:
    st.warning("Please upload a CSV file")