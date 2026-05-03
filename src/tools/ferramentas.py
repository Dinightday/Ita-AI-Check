from langchain_core.tools import tool
from schema import BaseConfig

@tool
def emprestimo():
    """Usa-se quando o empréstimo é aceito."""
    print(f"Empréstimo de {BaseConfig.valor_solicitado}")

@tool
def nao_emprestimo():
    """Usa-se quando o empréstimo é por motivo bobo."""
    print("Empréstimo rejeitado")