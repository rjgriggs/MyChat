import streamlit as st
# from transformers import pipeline

# Load the ChatGPT model
chatbot = pipeline("text-generation", model="microsoft/DialoGPT-medium")

st.title("ChatGPT")

# Create a text input for the user to type their message
message = st.text_input("Enter your message:")

# If the user enters a message and hits enter, generate a response
if message:
    response = chatbot(message, max_length=50)
    st.write("ChatGPT: ", response[0]["generated_text"])
