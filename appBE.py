from fastapi import FastAPI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langserve import add_routes            # Helps create FastAPI routes

from langchain_openai import ChatOpenAI     # For OpenAI
from langchain_ollama.llms import OllamaLLM # For Ollama

import uvicorn
import os
from dotenv import load_dotenv

# Loading environment variables
load_dotenv()

# Langsmith tracking
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_PROJECT"] = os.getenv("LANGCHAIN_PROJECT")
os.environ["LANGCHAIN_TRACING_V2"] = "true"

# Environment varibles in os.environ dictionary
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

# FastAPI app
appBE = FastAPI(
    title = "Lanchain server BE",
    version = "1.0",
    description = "BE with OpenAI and Opensource LLM capability"
)

# Models
llmOpenaAI = ChatOpenAI()               #Open AI
llmLlama = OllamaLLM(model="llama3.2")  #Ollama Open source

# Prompt templates
promptStory = ChatPromptTemplate(
    [
        ("system","You are a helpful AI teacher."),
        ("user","Tell a story about {story_topic}")
    ]
)

promptPoem = ChatPromptTemplate(
    [
        ("system","You are a helpful AI Poet."),
        ("user","Tell a poem about {poem_topic}")
    ]
)

# API Routes
add_routes(
    appBE,
    ChatOpenAI(),
    path = "/openai"
)

add_routes(
    appBE,
    promptStory | llmOpenaAI,
    path = "/story"
)

add_routes(
    appBE,
    promptPoem | llmLlama,
    path = "/poem"
)


if __name__ == "__main__":
    uvicorn.run(appBE, host = "localhost", port= 8000)