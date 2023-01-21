# from email.policy import default
import os
from decouple import config
import openai
import streamlit as st

openai.api_key = ['pass']
st.write("Hey there big daddy")
st.header("testing this app")
articleTXT = st.text_area("enter the text you want me to look at")

if len(articleTXT) > 10:
  if st.button("generate results"):
    response = openai.Completion.create(
      engine = "text-davinci-003",
      prompt = "can you give me the response now? : " + articleTXT,
      max_token = 516
     # temperature = 
      
    )
