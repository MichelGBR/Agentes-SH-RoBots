# 🤖 Sobre o projeto :

A proposta geral do projeto é utilizar Inteligência Artificial e automações desenvolvidas em Python para otimizar processos internos, reduzir tarefas manuais e aumentar a eficiência operacional. Já foram implementadas diversas automações que eliminaram mais de 5 horas de trabalho repetitivo, tornando os fluxos até 6 vezes mais rápidos. Essa iniciativa marca o início de uma jornada contínua de melhorias, com foco em escalabilidade, agilidade e geração de valor para o negócio.

<div align="left" >

# 🧩​ Ferramenta utilizada:


<img align="left" height="90" width="80" src="https://github.com/user-attachments/assets/352a6e03-ecf0-47ed-a8a7-0faead584435">

<br>
<br> 
<br>
<br> 

# 💻 Bibliotecas usadas nos Agentes:

Streamlit – Para a interface web simples e funcional

LangChain – Para a orquestração da cadeia de recuperação e geração

FAISS – Para a indexação e busca de vetores

Hugging Face Embeddings – Para transformar o conteúdo textual em vetores

Ollama – Para rodar o modelo LLM localmente (ex: LLaMA 2)

# 🧠 Processo

1. Leitura do arquivo: O script carrega um arquivo .txt com blocos de informações sobre mim.

2. Criação do vetor semântico: Cada trecho do texto é transformado em vetores com o modelo all-MiniLM-L6-v2.

3. Indexação com FAISS: Os vetores são indexados para rápida recuperação.

4. RAG (Geração Aumentada por Recuperação): Ao digitar uma pergunta, o sistema busca os trechos mais relevantes do texto e passa essas informações ao modelo de linguagem (LLM), que então responde com base apenas nesses dados.

5. Interface: Tudo isso é disponibilizado por uma interface amigável via Streamlit.
