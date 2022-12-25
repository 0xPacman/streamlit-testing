import streamlit as st
import datetime
import time

st.title("Current Time")


while True:
    st.write(datetime.datetime.now())
    time.sleep(1)

st.markdown("""
    <style>
        h1 {
            text-align: center;
            font-size: 50px;
        }
    </style>
    """, unsafe_allow_html=True)
