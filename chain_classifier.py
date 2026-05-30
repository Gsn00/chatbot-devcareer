from dotenv import load_dotenv
from langchain_groq import ChatGroq
from pydantic import Field, BaseModel
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import PydanticOutputParser

load_dotenv()

model = ChatGroq(model="llama-3.1-8b-instant", temperature=0.0)

system_prompt = """Você é um especialista em classificação de perguntas voltadas a carreira Dev. Classifique a pergunta do usuário
como 1 para perguntas relacionadas a linguagens de programação, 2 para área de desenvolvimento, 3 para preparação para entrevista,
4 para recursos de estudos e 5 para qualquer pergunta fora do tema.
\n{format_instructions}\n
Pergunta do usuário: {input}
"""

class Classifier(BaseModel):
    option: int = Field(description="Opção escolhida de acordo com a pergunta do usuário.")

parser = PydanticOutputParser(pydantic_object=Classifier)

prompt_template = ChatPromptTemplate([
    ("system", system_prompt)
], partial_variables={"format_instructions": parser.get_format_instructions()})

chain = prompt_template | model | parser