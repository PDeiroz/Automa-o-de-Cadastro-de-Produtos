# Automaçao de Cadastro de Produtos

Este projeto visa automatizar o processo de cadastro de produtos em um sistema web a partir de dados contidos em uma planilha Excel. 
A automação é realizada usando Python, com a biblioteca PyAutoGUI para interação com a interface gráfica e Openpyxl para manipulação da planilha Excel.

# 1. Python - Automação do Cadastro

1.1 Bibliotecas Utilizadas
pyautogui: Automatização da interação com uma interface gráfica.
openpyxl: Manipulação de planilhas Excel.
pyperclip: Copiar e colar dados na área de transferência.

1.2 Fluxo de Execução
Abrir a Planilha: Carregar uma planilha Excel contendo os dados dos produtos.
Iterar sobre Linhas: Correr cada linha da planilha (500 linhas no total).
Extrair Dados: Obtenha dados de cada coluna para as variáveis ​​correspondentes.
Preencher Campos: Utilização do PyAutoGUI para inserir dados nos campos do sistema web.
Repetir Processo: Repetir o processo para todas as linhas da planilha.

# 2. HTML - Interface de Cadastro de Produtos

2.1 Campos do Formulário
Produto: Campo de texto para inserir o nome do produto.
Fornecedor: Campo de texto para inserir o nome do fornecedor.
Categoria: Campo de texto para inserir a categoria do produto.
Valor Unitário: Campo de texto para inserir o valor unitário do produto.
Notificar Venda: Menu suspenso para selecionar entre "SIM" ou "NÃO".

2.2 Funcionalidades
Registrador Produto: Botão para ativar a função de registro do produto.
Mensagem de sucesso: Exibe uma mensagem após o registro bem-sucedido.
Botão OK: Permite fechar uma mensagem de sucesso.

2.3 Funcionalidades JavaScript
Registrador Produto: Função para simular o registro, ocultando o formulário e exibindo a mensagem de sucesso.
Fechar Mensagem: Função para redefinir o formulário e ocultar a mensagem de sucesso.

# 3. Execução do Projeto
Instale as bibliotecas Python ( pyautogui, openpyxl, pyperclip).
Execute o script Python para iniciar a automação.
Abra o arquivo HTML em um navegador para acessar uma interface de cadastro.

# 4. Observações
Coordenadas PyAutoGUI: As coordenadas no código Python devem corresponder à posição correta na interface do sistema web.
Formato da Planilha: A planilha Excel deve seguir o formato fornecido no exemplo.
Adaptações Necessárias: Faça os ajustes necessários conforme seu ambiente específico.

Este projeto fornece uma solução eficiente para o cadastro automatizado de produtos, evitando erros manuais e otimizando o tempo de inserção de dados. -se de personalizar o código conforme as especificidades do seu sistema web e ambiente de trabalho.
