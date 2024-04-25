#QnA Chatbot
from langchain.llms import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

import streamlit as st

## Function to load openai model and get responses

def get_openai_response(question):
    llm = OpenAI(openai_api_key = os.getenv('OPEN_API_KEY'),model_name = "gpt-3.5-turbo-instruct", temperature=0.5)
    response = llm(question)
    return response

## Initialize the streamlit
    
st.set_page_config(page_title="QnA Demo")
st.header("Langchain Application")

input = st.text_input("Input: ", key = "input")

response = get_openai_response(input)

submit = st.button("Ask the question")

## if button is pressed

if submit:
    st.subheader("The Response is")
    st.write(response)