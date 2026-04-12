import streamlit as st
import pandas as pd

st.title('🎈 sample-ml')

st.info('This app builds a machine learning model')

with st.expander("Data", expanded=True):
    st.write("**raw data**")
    df = pd.read_csv('sample-ml.csv')
    st.dataframe(df)

