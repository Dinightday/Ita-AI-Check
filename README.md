<div align="center">
  <img src="https://shields.io" />
  <img src="https://shields.io" />
  <img src="https://shields.io" />
</div>

<h1 align="center">🏦 Graph-Risk-Engine</h1>

<p align="center">
  <strong>Orquestração de Grafos Inteligentes para Decisão Crítica de Crédito e Exuberância.</strong>
</p>

<hr>

<h2>🚀 Arquitetura de Grafo vs. Scripts Lineares</h2>
<p>
  Este projeto substitui o processamento linear ineficiente por um <b>Grafo de Estados (StateGraph)</b>. Em vez de inputs e outputs soltos, utilizamos o <b>LangGraph</b> para manter o estado da transação e permitir uma análise multinível sem depender de regras rígidas (<code>if/else</code>).
</p>

<h2>🧠 Motor de Decisão Autônoma</h2>
<p>
  O sistema é composto por nós especializados que processam o fluxo de dados de forma assíncrona:
</p>

<ul>
  <li><b>Nó de Triagem Semântica:</b> Avalia a coerência entre valor, local e categoria através de embeddings/LLM.</li>
  <li><b>Identificação de Exuberância:</b> Detecta anomalias contextuais (ex: valores próximos a 10k em contextos de baixo ticket médio).</li>
  <li><b>Final State Decision:</b> A IA atua como juiz final, emitindo um veredito autônomo baseado no acúmulo de risco no grafo.</li>
</ul>

<h2>🛠️ Stack Técnica</h2>
<p>
  - <b>LangGraph / LangChain</b>: Orquestração de agentes e manutenção de estado.<br>
  - <b>Python (Async)</b>: Processamento de alto desempenho para múltiplos inputs.<br>
  - <b>GenAI Core</b>: Modelos de linguagem atuando como nós de raciocínio lógico.
</p>

<hr>

<p align="center">
  <i>"Construindo sistemas de decisão autônomos e escaláveis."</i>
</p>
