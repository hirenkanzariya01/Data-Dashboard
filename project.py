import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(layout="wide")
st.header("Data Analysis Dashbord")

st.sidebar.title("Side Menu")
file = st.sidebar.file_uploader("Uplode Csv File")
if file:
    data = pd.read_csv(file)
else:
    d = {
        "Name": ["Vivo", "Oppo", "Mi", "I-phone", "One Plus", "Redme"],
        "Seals": [150, 200, 100, 360, 100, np.nan],
        "Price": [35000, np.nan, 15000, 68000, 35000, 21000],
        "unit": [20, 35, 55, 45, 12, 32],
    }
    data = pd.DataFrame(d)

tab1, tab2, tab3 = st.tabs(["Data", "Statical Analysis", "Charts"])

with tab1:
    st.write("## First Five Data ")
    st.dataframe(data.head())

    st.write("## Last Five Data ")
    st.dataframe(data.tail())

    st.write("## Sample Data ")
    st.dataframe(data.sample(5))


with tab2:
    selected = st.selectbox(
        "Select Colums", data.select_dtypes(include="number").columns
    )

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.write(f"### Total {selected}")
        st.write(data[selected].sum())

    with col2:
        st.write(f"### Avg {selected}")
        st.write(np.round(data[selected].mean()))

    with col3:
        st.write(f"### Mimimum {selected} ")
        st.write(np.round(data[selected].min()))

    with col4:
        st.write(f"### Maximum {selected} ")
        st.write(np.round(data[selected].max()))

    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Missing Values")
        st.write(data.isna().sum())
    with col2:
        st.subheader("Missing Value %")
        st.write(data.isna().sum() / len(data) * 100)

    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Fill Missing Value")
        selectedColumn = st.multiselect(
            "Select Columns", data.columns[data.isnull().any()]
        )
        fillby = st.selectbox(
            "Select Value To Fill",
            [
                0,
                1,
                "Minimum Value",
                "Maximum Value",
                "Average Value",
                "Most Accurant Value",
            ],
        )
        for i in selectedColumn:
            if fillby == 0:
                data[i].fillna(0, inplace=True)
            elif fillby == 1:
                data[i].fillna(1, inplace=True)
            elif fillby == "Minimum Value":
                data[i].fillna(np.min(data[i]), inplace=True)
            elif fillby == "Maximum Value":
                data[i].fillna(np.max(data[i]), inplace=True)
            elif fillby == "Average Value":
                data[i].fillna(np.mean(data[i]), inplace=True)
            elif fillby == "Most Accurant Value":
                data[i].fillna(data[i].mode()[0], inplace=True)

        st.dataframe(data)
