from langchain_core.tools import tool

@tool
def emprestimo():
    """ACIONE esta ferramenta imediatamente se o motivo do empréstimo for 
    legítimo e profissional."""
    print("Empréstimo aceito")

@tool
def nao_emprestimo():
    """ACIONE esta ferramenta imediatamente se o motivo do empréstimo for 
    ilegal, suspeito (como lavagem de dinheiro) ou fútil."""
    print("Empréstimo rejeitado")
