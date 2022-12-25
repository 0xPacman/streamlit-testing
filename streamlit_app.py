import streamlit as st
import datetime
import time 

st.title("Current Time")

st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Digital-7&display=swap');
        h1 {
            font-family: 'Digital-7', sans-serif;
            text-align: center;
            font-size: 50px;
        }
    </style>
    """, unsafe_allow_html=True)

@st.cache(interval=1)
def get_time():
    return datetime.datetime.now().strftime('%H:%M:%S')

st.write(get_time(), unsafe_allow_html=True)
