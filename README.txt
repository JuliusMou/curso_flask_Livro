APLICAÇÃO FLASK - INSTRUÇÕES DE EXECUÇÃO
=========================================

Este projeto é uma aplicação web desenvolvida com o framework Flask (Python).
Siga os passos abaixo para configurar e executar a aplicação em sua máquina.


1. PRÉ-REQUISITOS
-----------------

- Python 3 instalado (recomendado: Python 3.8 ou superior).
- Gerenciador de pacotes pip (geralmente já incluso na instalação do Python).


2. CRIAÇÃO DO AMBIENTE VIRTUAL (venv)
-------------------------------------

Recomenda-se criar um ambiente virtual para isolar as dependências do projeto.

No diretório raiz do projeto, execute:

    python3 -m venv venv

Este comando criará uma pasta chamada "venv" contendo o interpretador Python
e o pip isolados para este projeto.


3. ATIVAÇÃO DO AMBIENTE VIRTUAL
-------------------------------

O comando de ativação varia conforme o sistema operacional:

Linux / macOS:

    source venv/bin/activate

Windows (Prompt de Comando):

    venv\Scripts\activate

Windows (PowerShell):

    venv\Scripts\Activate.ps1

Após a ativação, o nome "(venv)" aparecerá no início da linha de comando,
indicando que o ambiente virtual está ativo.


4. INSTALAÇÃO DAS DEPENDÊNCIAS
------------------------------

Com o ambiente virtual ativo, instale todas as bibliotecas necessárias
executando:

    pip install -r requirements.txt

As seguintes dependências serão instaladas:

- Flask: framework web.
- Flask-Bootstrap: integração do Bootstrap para estilização das páginas.
- Flask-Moment: formatação de datas e horários no template.
- Flask-SQLAlchemy: ORM para manipulação do banco de dados SQLite.
- Flask-WTF: integração de formulários web com o Flask.
- WTForms: definição e validação de formulários.


5. CONFIGURAÇÃO DA VARIÁVEL DE AMBIENTE
---------------------------------------

O Flask precisa saber onde está a aplicação. Defina a variável FLASK_APP:

Linux / macOS:

    export FLASK_APP=app

Windows (Prompt de Comando):

    set FLASK_APP=app

Windows (PowerShell):

    $env:FLASK_APP="app"


6. EXECUÇÃO DA APLICAÇÃO
------------------------

Ainda com o ambiente virtual ativo, execute:

    flask run

A aplicação será iniciada e ficará disponível em:

    http://127.0.0.1:5000

Para encerrar o servidor, pressione Ctrl+C no terminal.


7. INFORMAÇÕES ADICIONAIS
-------------------------

- O banco de dados usado pela aplicação é o SQLite, armazenado no arquivo
  "app/data.sqlite". Não é necessária nenhuma configuração extra de banco.

- As configurações da aplicação (como a SECRET_KEY e a URI do banco de dados)
  estão definidas no arquivo "config.py".

- O pacote "app" contém os controllers (rotas), models (formulários e tabelas)
  e templates (páginas HTML).

- Ao concluir o uso, você pode desativar o ambiente virtual com o comando:

    deactivate