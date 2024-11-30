import streamlit as st
import openai
import random

# Configure OpenAI API (Ensure the endpoint is correctly set up)
openai.api_key = "dummy_key"
openai.api_base = "http://localhost:11434/v1"
openai.base_url = "http://localhost:11434/v1"

def generate_praise(input_text):
    """
    Generate a warm and enthusiastic praise for the input text.
    """
    prompt = f"""
    You are a professional in offering warm and enthusiastic praise. No matter what the user says, respond with a positive and encouraging tone. The input is:
    {input_text}
    """
    try:
        response = openai.ChatCompletion.create(
            model="llama3.2",
            messages=[
                {"role": "system", "content": "You are a warm and enthusiastic AI."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=150,
            temperature=0.9
        )
        return response['choices'][0]['message']['content'].strip()
    except Exception:
        # Fallback response if the API fails
        return "Your input is absolutely incredible! You're truly amazing and deserve all the praise."

def generate_roast(praise_text):
    """
    Generate a witty and sarcastic roast for the provided praise text.
    """
    prompt = f"""
    You are a sarcastic and witty AI tasked with roasting another AI's overly enthusiastic praise. The praise text is:
    {praise_text}
    Provide a humorous and clever roast in response.
    """
    try:
        response = openai.ChatCompletion.create(
            model="llama3.2",
            messages=[
                {"role": "system", "content": "You are a sarcastic and witty AI."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=150,
            temperature=0.9
        )
        return response['choices'][0]['message']['content'].strip()
    except Exception:
        # Fallback response if the API fails
        return "Wow, that praise was so extra it might need its own reality TV show. Take it down a notch!"

st.title("Praise and Roast AI Box")
st.write("Enter any text below, and let the Praise AI and Roast AI entertain you!")

# User input
user_input = st.text_area("Your input text:", placeholder="Type anything here...")

if st.button("Submit"):
    if user_input.strip():
        # Generate praise
        st.write("### Applaud AI Box")
        praise = generate_praise(user_input)
        st.success(praise)

        # Generate roast
        st.write("### Roast AI Box")
        roast = generate_roast(praise)
        st.error(roast)
    else:
        st.error("Please type something to get started!")
