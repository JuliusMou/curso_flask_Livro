# ⚡ Aplicação Flask

> Aplicação web modular desenvolvida com o microframework **Flask** (Python), estruturada no padrão MVC com banco de dados SQLite e formulários validados.

![Status do Projeto](https://img.shields.io/badge/Status-Funcional-brightgreen)
![Python](https://img.shields.io/badge/Python-3.8+-blue?logo=python)
![Flask](https://img.shields.io/badge/Framework-Flask-lightgrey?logo=flask)
![SQLite](https://img.shields.io/badge/Database-SQLite-003B57?logo=sqlite)

---

## 📌 Sobre o Projeto

Este projeto é uma aplicação web construída em Python utilizando o framework Flask. A arquitetura foi organizada de forma modular no pacote `app`, separando as responsabilidades entre controle de requisições, modelagem de dados e templates de interface.

### 🎯 Recursos da Aplicação
* **Estrutura Modular:** Organização em *controllers* (rotas), *models* (banco e formulários) e *templates* (HTML).
* **Camada Visual:** Renderização de templates Jinja2 combinada com componentes do Bootstrap.
* **Persistência Local:** Banco de dados relacional embarcado sem dependências externas de serviço.
* **Validação de Entradas:** Formulários web protegidos e validados via WTForms.

---

## 🛠️ Tecnologias Utilizadas

* **Linguagem:** Python
* **Backend:** Flask
* **Banco de Dados:** SQLite (`app/data.sqlite`)
* **ORM:** Flask-SQLAlchemy
* **Interface & Formulários:** Flask-Bootstrap, WTForms e Flask-WTF
* **Manipulação de Tempo:** Flask-Moment

---

## 🚀 Funcionalidades

### 🔹 Módulos Implementados
- [x] Estrutura base de rotas e controladores dentro do pacote `app`
- [x] Banco de dados SQLite configurado localmente
- [x] Integração com Bootstrap para estilização de páginas
- [x] Definição e validação de formulários web
- [x] Formatação dinâmica de datas e horários em templates

---

## 💻 Como Executar Localmente

### Pré-requisitos
* Python 3 instalado (recomendado: 3.8 ou superior)
* Gerenciador de pacotes `pip`
* Git

### Passo a passo

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/seu-usuario/nome-do-repositorio.git
   cd nome-do-repositorio
   ```

2. **Crie o ambiente virtual (`venv`):**
   ```bash
   python3 -m venv venv
   ```

3. **Ative o ambiente virtual:**
   * **Linux / macOS:**
     ```bash
     source venv/bin/activate
     ```
   * **Windows (Prompt de Comando):**
     ```cmd
     venv\Scripts\activate
     ```
   * **Windows (PowerShell):**
     ```powershell
     venv\Scripts\Activate.ps1
     ```

4. **Instale as dependências:**
   ```bash
   pip install -r requirements.txt
   ```

5. **Defina a variável de ambiente:**
   * **Linux / macOS:**
     ```bash
     export FLASK_APP=app
     ```
   * **Windows (Prompt de Comando):**
     ```cmd
     set FLASK_APP=app
     ```
   * **Windows (PowerShell):**
     ```powershell
     $env:FLASK_APP="app"
     ```

6. **Inicie a aplicação:**
   ```bash
   flask run
   ```

Acesse o sistema no navegador através do endereço: **http://127.0.0.1:5000**

Para interromper o servidor, pressione `Ctrl + C` no terminal. Ao concluir o uso, desative o ambiente virtual executando `deactivate`.

---

## 📂 Estrutura do Projeto

* `app/` — Contém os controllers (rotas), models (tabelas e formulários) e templates (páginas HTML).
* `app/data.sqlite` — Arquivo do banco de dados SQLite local.
* `config.py` — Parâmetros centrais da aplicação (como `SECRET_KEY` e URI de conexão do banco).
* `requirements.txt` — Lista de bibliotecas necessárias para execução.