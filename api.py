from fastapi import FastAPI
from langserve import add_routes
from main import runnable_with_history

app = FastAPI(title="Chatbot DevCareer", description="Chatbot desenvolvido para ajudar profissionais e estudantes de tecnologia com dúvidas do universo tech.")
add_routes(app, runnable_with_history, path="/chat")