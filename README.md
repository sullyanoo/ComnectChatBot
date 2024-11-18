Portal de Administração com Chatbot e Registro de Atividades
Bem-vindo ao Portal de Administração de Atividades, um sistema completo para gerenciamento de usuários e registros de atividades, com integração de um chatbot inteligente. Este projeto oferece uma interface amigável para gerenciar dados, registrar atividades e consultar informações a partir de documentos, com base em palavras-chave. Ideal para quem busca otimizar o gerenciamento de dados e oferecer uma interação mais fluida através de um assistente automatizado.

Funcionalidades
Administração de Usuários: Cadastro, edição, visualização e exclusão de usuários. O sistema permite o controle completo dos usuários, garantindo fácil acesso e gerenciamento.

Registro de Atividades: Criação e visualização de registros de atividades, como uma agenda. O sistema permite a marcação de atividades, com datas, descrições e status de conclusão.

Chatbot Integrado: O chatbot utiliza um conjunto de documentos como base de dados. Ele é capaz de identificar palavras-chave em textos e retornar o conteúdo relacionado de forma inteligente, ajudando o usuário a encontrar informações rapidamente.

Tecnologias Utilizadas
Python: A linguagem principal do projeto, utilizada para implementar a lógica do sistema e integração com o chatbot.

Bootstrap: Framework front-end utilizado para a construção de uma interface bonita e responsiva. Garantindo uma boa experiência do usuário em diferentes dispositivos.

SQLAlchemy: ORM utilizado para interação com o banco de dados, facilitando a manipulação e armazenamento de dados relacionados a usuários e atividades.

Flask (opcional, se utilizado no projeto): Framework web leve para a criação da aplicação, facilitando a integração de front-end e back-end.

Chatbot (Modelo): O chatbot foi desenvolvido para processar documentos em busca de palavras-chave e retornar o conteúdo relevante, oferecendo uma resposta rápida e eficaz.

Como Rodar o Projeto
Pré-requisitos
Python 3.8 ou superior instalado.
Virtualenv (opcional, mas recomendado).
Banco de dados configurado (MySQL, SQLite ou outro conforme escolha do projeto).

Passos para rodar o projeto:
Clone o repositório: git clone https://github.com/seuusuario/nome-do-repositorio.git

Instale as dependências: Dentro do diretório do projeto, crie um ambiente virtual (se preferir) e instale as dependências.
cd nome-do-repositorio
python -m venv venv
source venv/bin/activate  # Para Windows: venv\Scripts\activate
pip install -r requirements.txt

Estrutura do Projeto

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


