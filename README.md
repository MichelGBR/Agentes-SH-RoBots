
<br>
<br> 

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

### - Playwright:

Ferramenta moderna de automação de navegadores, com suporte a múltiplos browsers e execução paralela. Está sendo estudada e testada como evolução do Selenium para novos projetos. Suas principais vantagens incluem:

• Execução mais rápida e estável em comparação ao Selenium;
• Facilidade para lidar com elementos dinâmicos e testes em paralelo;
• Potencial para substituir o Selenium em futuras automações, mantendo a robustez e ampliando a escalabilidade dos processos.

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
Biblioteca utilizada para automação de interações com a interface gráfica do usuário (GUI).

• Realizar cliques e movimentar o mouse em situações onde o Selenium não conseguiu interagir com elementos da página;

• Simular entrada de dados em campos específicos quando outras abordagens falharam.

• A flexibilidade do PyAutoGUI garantiu que o processo não fosse interrompido por limitações do Selenium, completando a automação de forma eficiente.

