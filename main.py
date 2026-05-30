from chain_classifier import chain_classifier
from langchain_core.runnables import RunnableLambda, RunnableParallel
from chain_programming_language import chain_programming_language
from chain_development_area import chain_development_area
from chain_interview_preparation import chain_interview_preparation
from operator import itemgetter

def classify_route(input: dict):
    option = input["option"].option
    
    match option:
        case 1:
            print(f"\n>> Escolha Pydantic = {option} (Linguagem de Programação)\n")
            return chain_programming_language
        case 2:
            print(f"\n>> Escolha Pydantic = {option} (Área de Desenvolvimento)\n")
            return chain_development_area
        case 3:
            print(f"\n>> Escolha Pydantic = {option} (Preparação para Entrevista)\n")
            return chain_interview_preparation
        case _:
            print(f"\n>> Escolha Pydantic = {option} (Tópicos Gerais)\n")

chain = RunnableParallel({"input": itemgetter("input"), "option": chain_classifier}) | RunnableLambda(classify_route)

result = chain.invoke({"input":"Quais pontos críticos devo me atentar para conseguir minha primeira vaga?"})

print(result)