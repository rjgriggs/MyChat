# from email.policy import default
import os
from decouple import config
import openai
import streamlit as st

openai.api_key = ['pass']
st.write("Hey there big daddy")
st.header("testing this app")
articleTXT = st.text_area("enter the text you want me to look at")


