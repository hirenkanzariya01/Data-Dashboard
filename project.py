import streamlit as st 
import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 

st.set_page_config(layout="wide")
st.header('Data Analysis Dashbord')

st.sidebar.title('Side Menu')
file = st.sidebar.file_uploader('Uplode Csv File')
if file:
  data = pd.read_csv(file)
  
tab1, tab2, tab3 = st.tabs(['Data', 'Statical Analysis', 'Charts'])

with tab1:
  if file:
    st.write('## First Five Data ')
    st.dataframe(data.head())
    
    st.write('## Last Five Data ')
    st.dataframe(data.tail())
    
    st.write('## Sample Data ')
    st.dataframe(data.sample(5))
    

with tab2:
  if file:
    selected = st.selectbox('Select Colums', data.select_dtypes(include='number').columns)
  
  col1, col2 ,col3, col4= st.columns(4)
  
  if file:
    with col1:
      st.write(f'### Total {selected}')
      st.write(data[selected].sum())
      
    with col2:
      st.write(f'### Avg {selected}')
      st.write(np.round(data[selected].mean()))
      
    with col3:
      st.write(f'### Mimimum {selected} ')
      st.write(np.round(data[selected].min()))
      
    with col4:
      st.write(f'### Maximum {selected} ')
      st.write(np.round(data[selected].max()))
      

