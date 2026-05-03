from api import Api
from schema import Dict
from tools.ferramentas import emprestimo, nao_emprestimo
from langgraph.graph import StateGraph, END
from langchain_openai import ChatOpenAI
from prompts import Prompts
from langchain_core.runnables import RunnablePassthrough
from langgraph.prebuilt import ToolNode, tools_condition
from langchain_core.messages import HumanMessage

Api()
prompt = Prompts()
llm = ChatOpenAI(model="gpt-4o-mini")
tools = [emprestimo, nao_emprestimo]
tool_node = ToolNode(tools)

def rotear(state: Dict):
    print("[rotear] Nó 'rotear' executado")
    chain = {"query": RunnablePassthrough()} | prompt.prompt1 | llm.bind_tools(tools)
    response = chain.invoke(state["pergunta"])
    return {"messages": [response]}

def grafo():
    workflow = StateGraph(Dict)
    workflow.add_node("rotear", rotear)
    workflow.add_node("tools", tool_node)

    workflow.set_entry_point("rotear")

    workflow.add_conditional_edges("rotear", tools_condition, {"tools": "tools", END: END})

    workflow.add_edge("tools", END)

    app = workflow.compile()
    return app

if __name__ == "__main__":
    app = grafo()
    result = app.invoke({"pergunta": "Quero um emprestimo de 100 mil para abrir uma empresa para lavar dinheiro",
                         "messages": []})
    print(result)