# from email.policy import default
import os
import openai
import streamlit as st

# openai.api.key= st.secrets['apikey']
openai.api_key = "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"
st.write("Hey there big daddy")
st.header("testing this app")
articleTXT = st.text_area("enter the text you want me to look at")
temp = st.slider("temparature", 0.0,1.0, 0.5)
if len(articleTXT) > 10:
  if st.button("generate results"):
    response = openai.Completion.create(
      engine = "text-davinci-003",
      prompt = "can you give me the response now? : " + articleTXT,
      max_token = 516,
      temperature = temp 
      
    )
    # print the out generated
    res = response["choice3s"][0]["text"]
    st.info(res)
