import os
import cohere
from dotenv import load_dotenv
import streamlit as st

# Load environment variables from the .env file
load_dotenv()

# Save the below line as ".env" under the same folder of the python program
# COHERE_API_KEY="your_API_Key"

# 1. Securely Store Your API Key: Get the API key from the environment variable
api_key = os.getenv('COHERE_API_KEY')

# 2. Connect to the API
co = cohere.Client(api_key)

# 3. Define Chatbot Tone with Preamble
preamble_template = "You are a talented stand-up comedian, recognized for your sharp humor and engaging personality. Your clever narratives and knack for relating to various audiences make your comedy both insightful and approachable."
MODEL_ENGINE = "command-r-plus-08-2024"

# 4. Deploy with Streamlit
st.title("Chatbot to Tell Funny Joke")  # Add a title

# Initialize a session state variable to track if the app should quit
if 'quit' not in st.session_state:
    st.session_state.quit = False

# Quit button
if st.button("Quit"):
    st.session_state.quit = True
    st.write("Thank you for using this App! You can close this tab.")
    st.stop()  # Stops further script execution

# Only show the chat input if the app is not quitting
if not st.session_state.quit:

    with st.form("user_form", clear_on_submit=True):
        user_input = st.text_input("Please tell me a joke about ...")
        submit_button = st.form_submit_button(label="Send")

    if submit_button:
        with st.spinner("Please wait..."):
            completion = co.chat(
                model=MODEL_ENGINE,
                preamble=preamble_template,
                message=user_input
            )
            st.write(completion.text)

