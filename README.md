<img width=100% bottom=50px src="https://github.com/user-attachments/assets/8c625f1b-157f-40d4-ad7d-baebdbc51198"/>
<br>
<br> 

# 🤖 Sobre o projeto :

Este projeto teve como objetivo principal otimizar a visualizaçào do envio de descontos para clientes da seguradora Tokio Marine, priorizando aqueles que realmente utilizam os benefícios. Antes, o processo de extração de dados e análise era manual, demorava mais de duas horas e envolvia duas pessoas. Com o uso de automação, conseguimos reduzir esse tempo para cerca de 35 minutos, utilizando um robô chamado Tok_IA feito por mim.

A Tok_IA acessa automaticamente o site da seguradora, faz login, coleta dados de mais de 150 pessoas, organiza as informações e gera uma planilha Excel atualizada com os valores do dia. Esse processo trouxe agilidade para as operações da Honda, reduzindo significativamente os custos operacionais.
<div align="left" >

# 🧩​ Ferramenta utilizada:


<img align="left" height="90" width="80" src="https://github.com/user-attachments/assets/352a6e03-ecf0-47ed-a8a7-0faead584435">

<br>
<br> 
<br>
<br> 

# 💻 Bibliotecas usadas no robô:

### - Selenium: 
Biblioteca de automação que permite controlar navegadores da web programaticamente. No projeto Tok_IA, o Selenium foi usado para:

• Acessar o site da seguradora automaticamente;

• Fazer login com credenciais fornecidas;

• Navegar por diferentes seções e capturar informações relevantes;

• Realizar interações como cliques e preenchimento de campos.

• A biblioteca foi a espinha dorsal da automação, lidando com a maior parte das interações com o site.

### - Pandas:
Biblioteca de análise e manipulação de dados. Na Tok_IA, o Pandas desempenhou um papel importante em:

• Ler a base de dados inicial em formato Excel para identificar os clientes e informações necessárias;

• Atualizar os dados coletados pelo Selenium diretamente na planilha;

• Salvar os resultados finais em um arquivo Excel, garantindo que as informações fossem bem organizadas e acessíveis.

• Essa integração tornou possível gerar relatórios atualizados com precisão e rapidez.

### - PyAutoGUI: 
Biblioteca utilizada para automação de interações com a interface gráfica do usuário (GUI). No Tok_IA, o PyAutoGUI foi empregado como uma solução complementar para:

• Realizar cliques e movimentar o mouse em situações onde o Selenium não conseguiu interagir com elementos da página;

• Simular entrada de dados em campos específicos quando outras abordagens falharam.

• A flexibilidade do PyAutoGUI garantiu que o processo não fosse interrompido por limitações do Selenium, completando a automação de forma eficiente.

# ​​✅​ Resultado:

A Tok_IA conseguiu realizar o processo de forma perfeita, acessando o site da seguradora, extraindo os dados e gerando uma planilha Excel completamente atualizada. Essa automação trouxe uma grande melhoria no fluxo de trabalho, reduzindo o tempo de execução de mais de duas horas para apenas 35 minutos. Além disso, a precisão nos dados coletados facilita a análise e tomada de decisões, otimizando o uso dos recursos da empresa e permitindo maior foco em outras atividades estratégicas.
