import streamlit as st
import pandas as pd

st.title('🤖Machine Learning App')

st.info('This app builds a machine learning model')
with st.expander('Data'):
  st.write('**Raw data**')
df = pd.read_csv('/kaggle/input/data-set-messy/healthcare_cleaned_outliers_handled (1).csv')              
df
