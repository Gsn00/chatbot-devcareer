from chain_classifier import chain_classifier
from langchain_core.runnables import RunnableLambda, RunnableParallel, RunnablePassthrough
from chain_programming_language import chain_programming_language
from chain_development_area import chain_development_area
from chain_interview_preparation import chain_interview_preparation
from chain_study_resources import chain_study_resources
from chain_general_topics import chain_general_topics
from langchain_core.runnables import RunnableWithMessageHistory
from history_manager import get_session_history, trimmer
from operator import itemgetter

def classify_route(input: dict):
    option = input["option"].option
    
    print(f"\n\n{input}\n\n")
    
    print(f"\n>> Pergunta do Usuário: {input["input"]}")
    match option:
        case 1:
            print(f">> Escolha Pydantic = {option} (Linguagem de Programação)\n")
            return chain_programming_language
        case 2:
            print(f">> Escolha Pydantic = {option} (Área de Desenvolvimento)\n")
            return chain_development_area
        case 3:
            print(f">> Escolha Pydantic = {option} (Preparação para Entrevista)\n")
            return chain_interview_preparation
        case 4:
            print(f">> Escolha Pydantic = {option} (Recursos de Estudo)\n")
            return chain_study_resources
        case _:
            print(f">> Escolha Pydantic = {option} (Tópicos Gerais)\n")
            return chain_general_topics
            

chain = RunnablePassthrough.assign(history=itemgetter("history") | trimmer) | RunnableParallel({"input": itemgetter("input"), "history": itemgetter("history"), "option": chain_classifier}) | RunnableLambda(classify_route)

runnable_with_history = RunnableWithMessageHistory(
    chain,
    get_session_history,
    input_messages_key="input",
    history_messages_key="history"
)