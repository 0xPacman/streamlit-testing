import streamlit as st
import datetime
import time

st.title("Current Time")

while True:
    current_time = datetime.datetime.now()
    st.write(f"The current time is: {current_time.strftime('%H:%M:%S')}")
    st.balloons()
    time.sleep(1)

st.markdown("""
    <style>
        h1 {
            text-align: center;
            font-size: 50px;
        }
    </style>
    """, unsafe_allow_html=True)
