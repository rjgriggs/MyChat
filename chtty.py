# Import the required libraries
import openai
import streamlit as st

# Set the GPT-3 API key
# In this case, st.secrets["pass"] is accessing the value of the "pass" secret.

openai.api_key = st.secrets["pass"]
# Create Text Area Widget to enable user to enter texts
article_text = st.text_area("Enter your scientific texts to summarize")
# Create Radio Buttons
output_size = st.radio( label = "What kind of output do you want?", 
                        options= ["To-The-Point”, “Concise”, “Detailed"]
                     )
# First, we'll use an if statement to determine the desired output size 
# and set the out_token variable accordingly:

if output_size == "To-The-Point":
 out_token = 50
elif output_size == "Concise":
 out_token = 128
else:
 out_token = 516

# Next, we'll add a check to make sure that the input text is long enough 
# to summarize, and display a warning if it is not:

if len(article_text)>100:
 # Generate the summary
 # .......
 else:
  st.warning("Not enough words to summarize!")

if st.button("Generate Summary",type=’primary’):
 
  # Use GPT-3 to generate a summary of the article
 response = openai.Completion.create(
                    engine = "text-davinci-002",
                    prompt = "Please summarize this scientific article for me in a few sentences: "+ article_text,
                    max_tokens = out_token,
                    temperature = 0.5)
 
  # Print the generated summary
 res = response["choices"][0]["text"]
 st.success(res)

  # Give user the option to download result
st.download_button('Download result', res)
