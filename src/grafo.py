from api import Api
from schema import Dict
from tools.ferramentas import emprestimo, nao_emprestimo
from langgraph.graph import StateGraph, END
from langchain_openai import ChatOpenAI
from prompts import Prompts
from langchain_core.runnables import RunnablePassthrough

Api()
prompt = Prompts()
llm = ChatOpenAI(model="gpt-4o-mini")

query = "Quero um empréstimo de 5 mil reais para comprar pão"

def rotear(state: Dict):
    chain = {"query": RunnablePassthrough()} | prompt.prompt1 | llm
    response = chain.invoke(query)
    return {"resposta": response, "pergunta": query}

# Continuar grafo amanhã

def grafo():
    workflow = StateGraph(Dict)
    workflow.add_node("emprestimo", emprestimo)
    workflow.add_node("")