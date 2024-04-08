import os
import google.generativeai as genai
import streamlit as st
from dotenv import load_dotenv
load_dotenv()  

# setting up api key
genai.configure(api_key = os.getenv("GOOGLE_API_KEY"))

# function to load gemini pro and get responses
model = genai.GenerativeModel("gemini-pro")

def call_gemini(question):
    response = model.generate_content(question)
    return response.text

# setting streamlit UI
st.title("Gemini Pro App")

input = st.text_input("Enter query: ", placeholder = "Ask here")

submit = st.button("Ask Gemini Pro")

if submit:
    output = call_gemini(input)
    st.write(output)
