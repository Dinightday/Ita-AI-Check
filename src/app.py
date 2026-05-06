import streamlit as st
from grafo import pergunta

st.set_page_config(
    page_icon="🏦", 
    page_title="Banco com LangGraph"
                   )

st.title("Banco de empréstimos")

texto = st.text_input(label="Seu motivo do emprestimo:")
button = st.button("Enviar")

with st.spinner():
    if button:
        pergunta(texto)