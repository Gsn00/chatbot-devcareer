from chain_classifier import chain_classifier
from langchain_core.runnables import RunnableLambda, RunnableParallel
from operator import itemgetter

def classify_route(input: dict):
    option = input["option"].option
    print("Escolha --->", option)


chain = RunnableParallel({"input": itemgetter("input"), "option": chain_classifier}) | RunnableLambda(classify_route)

result = chain.invoke({"input":"Olá!"})

print(result)