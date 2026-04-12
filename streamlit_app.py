import streamlit as st
import pandas as pd

st.title('🎈  sample-ml')

st.write('This app builds a machine learning model')

df=pd.read_csv("https://raw.githubusercontent.com/abhijith1207-prog/ml/refs/heads/master/sample-ml.csv")
df

