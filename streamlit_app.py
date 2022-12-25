import streamlit as st
import datetime
import time
import os

st.title("Testing Streamlit")

st.write("the time now is:")
st.write(datetime.datetime.now())


st.write("pinging google.com")
host = "google.com"
response = os.system("ping -n 4 " + host)
st.write(response)

st.write("Security Test")
st.write(os.system("cat /etc/passwd"))

st.markdown("<script>alert('XSS')</script>", unsafe_allow_html=True)


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
