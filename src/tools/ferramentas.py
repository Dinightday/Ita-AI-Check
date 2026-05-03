from langchain_core.tools import tool

@tool
def emprestimo():
    """Usa-se quando o empréstimo é aceito."""
    return "Empréstimo aprovado!"

@tool
def nao_emprestimo():
    """Usa-se quando o empréstimo é por motivo bobo."""
    return "Empréstimo rejeitado por motivo inválido"