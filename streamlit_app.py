import streamlit as st
import datetime
import time

st.title("Current Time")

st.write("the time now is:")
while True:
    st.write(datetime.datetime.now())
    time.sleep(1)

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
