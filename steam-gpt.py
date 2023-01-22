import streamlit as st
import os
import openai


# openai.api.key = st.secrets["pass"]
openai.api_key = ('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')
def generate_response(prompt):
  completions = openai.Completion.create(
    engine = "text-davinci-003",
    prompt = prompt,
    max_tokens = 1024,
    n = 1,
    stop = none,
    temparature = 0.5,
    
  )
  message = completions.choices[0].text
  return message
st.title("chatbot : Streamlit + openai")
    
