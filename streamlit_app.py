import streamlit as st
import datetime

st.title("Current Time")

current_time = datetime.datetime.now()
st.write(f"The current time is: {current_time.strftime('%H:%M:%S')}")

st.markdown("""
    <style>
        h1 {
            text-align: center;
            font-size: 50px;
        }
    </style>
    """, unsafe_allow_html=True)

