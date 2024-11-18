# Portal de Administração com Chatbot e Registro de Atividades

Bem-vindo ao **Portal de Administração de Atividades**!  
Este sistema completo oferece funcionalidades para o gerenciamento de usuários e registros de atividades, integrando um chatbot inteligente para facilitar a consulta a documentos baseados em palavras-chave.

O projeto oferece uma interface amigável para que você possa:
- Gerenciar usuários de forma eficiente.
- Registrar e visualizar atividades como em uma agenda.
- Consultar informações através de um chatbot que retorna dados relevantes de documentos.

Ideal para quem busca otimizar o gerenciamento de dados e proporcionar uma experiência mais fluida e automatizada aos usuários.

---

## Funcionalidades

### Administração de Usuários
- Cadastro, edição, visualização e exclusão de usuários.  
- O sistema permite o controle completo dos usuários, com fácil acesso e gerenciamento.

### Registro de Atividades
- Criação e visualização de registros de atividades (agenda).  
- Marcação de atividades com datas, descrições e status de conclusão.

### Chatbot Integrado
- O chatbot utiliza um conjunto de documentos como base de dados.  
- Ele é capaz de identificar palavras-chave em textos e retornar o conteúdo relacionado de forma inteligente, ajudando o usuário a encontrar informações rapidamente.

---

## Tecnologias Utilizadas

- **Python**: A principal linguagem utilizada para implementar a lógica do sistema e a integração com o chatbot.
- **Bootstrap**: Framework front-end para construção de uma interface bonita e responsiva, garantindo boa experiência de uso.
- **SQLAlchemy**: ORM utilizado para interação com o banco de dados, facilitando a manipulação de dados.
- **Django**: Framework web utilizado para integração entre o front-end e o back-end.
- **Chatbot (Modelo)**: O chatbot processa documentos e busca palavras-chave para retornar respostas rápidas e eficazes.

---

## Como Rodar o Projeto

### Pré-requisitos

Antes de rodar o projeto, verifique se você tem os seguintes pré-requisitos:

- **Python 3.8 ou superior** instalado.
- **Virtualenv** (opcional, mas recomendado para isolar as dependências).
- Banco de dados configurado (MySQL, SQLite ou outro).

### Passos para rodar o projeto:

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/seuusuario/nome-do-repositorio.git

2. **Instale as dependências:**
   ```bash
   cd nome-do-repositorio
   python -m venv venv
   source venv/bin/activate  # Para Windows: venv\Scripts\activate
   pip install -r requirements.txt
   
3. **Estrutura do projeto :**
   /nome-do-repositorio
   │
   ├── /app.py                  # Arquivo principal do Flask (se usado)
   ├── /models.py               # Modelos de dados (SQLAlchemy)
   ├── /templates/              # Templates HTML (Bootstrap)
   ├── /static/                 # Arquivos estáticos (CSS, JS, imagens)
   ├── /chatbot.py              # Lógica do chatbot
   ├── /requirements.txt        # Dependências do Python
   ├── /config.py               # Configuração do banco de dados e outras variáveis
   └── /README.md               # Este arquivo

### Chat
  ![image](https://github.com/sullyanoo/ChatBot/blob/main/img/interface.png)

  ### Produtos
  ![image](https://github.com/sullyanoo/ChatBot/blob/main/img/interface_menu_produtos.png)
