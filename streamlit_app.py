import streamlit as st
import pandas as pd

st.title('🎈 sample-ml')

st.info('This app builds a machine learning model')

with st.expander("Data"):
    st.write("**raw data**")
    df = pd.read_csv('https://raw.githubusercontent.com/abhijith1207-prog/ml/refs/heads/master/sample-ml.csv')
    st.dataframe(df)

    st.write('**X**')
    X=df.drop('species',axis=1)
    X

    st.write('**Y**')
    Y=df.species
    Y

with st.expander("Data visualization", expanded=True):
    st.scatter_chart(data=df,x='bill_length_mm',y='body_mass_g',color='species')

