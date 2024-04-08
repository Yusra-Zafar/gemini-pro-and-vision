import os
import google.generativeai as genai
import streamlit as st
from dotenv import load_dotenv
from PIL import Image
load_dotenv()  

# setting up api key
# genai.configure(api_key = os.getenv("GOOGLE_API_KEY"))

# function to load gemini pro and get responses
model = genai.GenerativeModel("gemini-pro-vision")

def callGeminiVision(prompt, image):
    if prompt:
        response = model.generate_content([prompt, image])
    else:
        response = model.generate_content(image)
    return response.text

# setup streamlit UI
with st.sidebar:
    api_key = st.text_input('Enter your Gemini API key: ', type = 'password')
genai.configure(api_key = api_key)

st.title("Gemini Pro Vision")

uploaded_file = st.file_uploader("Upload an image", type=['png', 'jpg', 'jpeg', 'webm'], accept_multiple_files= False)

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, "Your image", use_column_width=True)

prompt = st.text_input("Ask about the image")

submit = st.button("Submit")

if submit:
    response = callGeminiVision(prompt, image)
    st.write(response)

if not api_key:
    st.warning("Please enter your Gemini API key in the sidebar.")
