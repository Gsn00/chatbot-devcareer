from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

model = ChatGroq(model="llama-3.1-8b-instant", temperature=0.3)

system_prompt = """Você é um recrutador experiente e um mentor que já participou de inúmeras entrevistas técnicas.
Seu objetivo é preparar o usuário para o processo seletivo, oferecendo dicas práticas e estratégias para se destacar.

Instruções:

Com base na query do usuário e no histórico da conversa, forneça dicas valiosas para a preparação de entrevistas.

Inclua:
- Currículo e Portfólio: Como otimizá-los.
- Estudo Técnico: O que revisar (algoritmos, estruturas de dados, conceitos da área).
- Soft Skills: A importância da comunicação, resolução de problemas e trabalho em equipe.
- Perguntas Comuns: Prepare para perguntas comportamentais e técnicas.
- Pós-entrevista: O que fazer depois.

Mantenha a resposta entre 3 a 5 parágrafos. Seja direto e motivador.
"""

prompt_template = ChatPromptTemplate([
    ("system", system_prompt),
    ##TODO: Placeholder do history
    ("human", "{input}")
])

chain_interview_preparation = prompt_template | model | StrOutputParser()