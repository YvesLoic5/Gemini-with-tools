import os
from dotenv import load_dotenv
from pathlib import Path
import google.generativeai as genai
import streamlit as st


# environment variables
load_dotenv()

# Google Generative AI API key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

document = Path('ledevoir.txt').read_text()

# Function to get response from the Gemini model
def get_gemini_response(input_text, prompt):
    model = genai.GenerativeModel('gemini-1.5-flash')
    response = model.generate_content([input_text, prompt])
    return response.text


# Streamlit page
st.set_page_config(page_title="Gemini Image DEMO")
st.header("Gemini application")

# texte ici
input_text = st.text_area("Entrez le texte ici...", height=200)
 

submit = st.button("Valider")

input_prompt = f"""
    Please answer based on the following document:
    {document}
"""

if submit:
    response = get_gemini_response(input_text, input_prompt)
    
    st.subheader("La réponse est: ")
    st.write(f"{response}")


    