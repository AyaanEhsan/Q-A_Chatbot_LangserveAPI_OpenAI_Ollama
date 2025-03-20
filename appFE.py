import streamlit as st
import requests as req
import os
from dotenv import load_dotenv

# Loading secrets from .env
load_dotenv()

# Langsmith tracking
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_PROJECT"] = os.getenv("LANGCHAIN_PROJECT")
os.environ["LANGCHAIN_TRACING_V2"] = "true"

def get_openai_response(input_story):
    response_story = req.post(
        url = "http://localhost:8000/story/invoke",
        json=  {'input': {'story_topic': input_story}}
    )
    return response_story.json()["output"]["content"]

def get_ollama_response(input_poem):
    response_poem = req.post(
        url ="http://localhost:8000/poem/invoke",
        json= { "input": { "poem_topic": input_poem}}
    )
    return response_poem.json()["output"]
    


# Streamlit
st.title("Multi LLM: Stories by OpenAI | Poem by Ollama")

input_story = st.text_input("Write an STORY on: ")
input_poem = st.text_input("Write an POEM on: ")

if input_story:
    st.write(get_openai_response(input_story))
    
if input_poem:
    st.write(get_ollama_response(input_poem))