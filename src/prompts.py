from langchain_core.prompts import ChatPromptTemplate

class Prompts:
    def __init__(self):
        self.prompt1 = ChatPromptTemplate.from_messages([
            ("system", """De acordo com os dados do usuário: {context}. 
             Classifica se ele merece um empréstimo com 'yes'
              ou se não merece com um 'no'."""),
            ("human", "{query}")
        ])