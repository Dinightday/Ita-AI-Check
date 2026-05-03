from langchain_core.prompts import ChatPromptTemplate

class Prompts:
    def __init__(self):
        self.prompt1 = ChatPromptTemplate.from_messages([
            ("system", """De acordo com o que o usuário quer, 
             use uma das ferramentas:
                Chame 'emprestimo' se o usuário merece
                Chame 'nao_emprestimo' se não merece."""),
            ("human", "{query}")
        ])