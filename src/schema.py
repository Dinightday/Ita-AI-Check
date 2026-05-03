from pydantic import BaseModel, Field
from typing import TypedDict

class BaseConfig(BaseModel):
    valor_solicitado: float = Field("Coletar o valor solicitado do usuário.")
    categoria_gasto: str = Field("Coletar o porque o usuário vai gastar o valor")
    grau_de_urgencia: int = Field("Você vai definir o quão urgente é entre 1 a 5, inteiros")

class Dict(TypedDict):
    resposta: str
    pergunta: str