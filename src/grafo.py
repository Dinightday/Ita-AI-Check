from api import Api
from schema import Dict
from tools.ferramentas import emprestimo, nao_emprestimo
from langgraph.graph import StateGraph, END
from langchain_openai import ChatOpenAI
from prompts import Prompts
from langgraph.prebuilt import ToolNode, tools_condition

Api()
prompt = Prompts()
llm = ChatOpenAI(model="gpt-4o-mini")
tools = [emprestimo, nao_emprestimo]
tool_node = ToolNode(tools)

def rotear(state: Dict):
    chain = prompt.prompt1 | llm.bind_tools(tools)
    response = chain.invoke({"pergunta": state["pergunta"]})
    return {"messages": [response]}

def assistente():
    workflow = StateGraph(Dict)
    workflow.add_node("rotear", rotear)
    workflow.add_node("tools", tool_node)

    workflow.set_entry_point("rotear")

    workflow.add_conditional_edges("rotear", tools_condition)

    workflow.add_edge("tools", END)

    app = workflow.compile()
    return app

def pergunta(query):
    grafo = assistente()
    grafo.invoke({"pergunta": query})