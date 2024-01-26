from langchain.llms import OpenAI
import os
from dotenv import load_dotenv
import streamlit as st
load_dotenv()

import streamlit as st 

def get_openai_response(question):
    llm = OpenAI(openai_api_key=os.getenv("OPEN_API_KEY"),temperature=0.5)
    response = llm(question)
    return response

st.set_page_config(page_title="Q&A Demo")

st.header("Lanchain Application")

input= st.text_input("Input : ",key=input)


submit=st.button("Ask Your Question")
response=get_openai_response(input)

if submit:
    st.subheader("The Response is ")
    st.write(response)