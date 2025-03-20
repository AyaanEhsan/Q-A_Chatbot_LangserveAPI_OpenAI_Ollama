# Q-A_Chatbot_LangserveAPI_OpenAI_Ollama

- Streamlit
- OpenAI / Ollama
- Langchain
- Langsmith
- Langserve

appBE.py
- Uses add_routes to create /poem and /story.
- /story is served by OpenAI.
- /poem is served by Lllama 3.2 (Local using Ollama).

appFE.py
- Sends user_input as json payload to appBE.py routes (/story | /poem).

Langserve (Uses FastAPI under the hood)
- API endpoints for OpenAI and Ollama.

Langsmith tracking
- Environmental varibales should be loaded in both FE and BE.