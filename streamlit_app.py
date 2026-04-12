import streamlit as st
import pandas as pd

st.title('🎈  sample-ml')

st.info('This app builds a machine learning model')
with st.expander("Data"):
  
  st.write("**raw data"**)
  df=pd.read_csv("https://raw.githubusercontent.com/abhijith1207-prog/ml/refs/heads/master/sample-ml.csv")
  st.write(df)

