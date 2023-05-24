import streamlit as st
import pandas as pd

st.title('Streamlit web app about Data Science')
name = st.text_input('Enter your name', '')
st.write(f'Hello {name}!')

st.sidebar.info('This app is about Data Science')
