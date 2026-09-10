# -*- coding: utf-8 -*-
"""
Módulo de Controllers Principal - default.py
Este arquivo define as rotas principais da aplicação Flask.
Faz parte da camada de Controllers no padrão MVC.

Funcionalidades:
- Rota de usuário (/user e /user/<name>)
- Página inicial (/) com redirecionamento
- Formulário com validação, sessão e flash messages
- Manipuladores de erro 404 e 500
"""

from app import app
from flask import (
    render_template,  # Renderiza templates HTML com variáveis
    url_for,          # Gera URLs para rotas nomeadas
    request,          # Acessa dados da requisição HTTP (não usado diretamente aqui)
    redirect,         # Redireciona para outra rota
    session,          # Armazena dados entre requisições (lado do servidor)
    flash             # Exibe mensagens temporárias ao usuário
)
from datetime import datetime, timezone  # Para timestamp UTC atual
from app.models.forms import FormularioTeste  # Formulário WTForms definido em models/forms.py


# =============================================================================
# ROTAS DE USUÁRIO
# =============================================================================

@app.route('/user/<name>')
@app.route('/user', defaults={'name': None})
def user(name):
    """
    Exibe a página de boas-vindas do usuário.
    
    Duas rotas mapeiam para esta função:
    - /user           -> name = None (pessoa qualquer)
    - /user/<name>    -> name = valor da URL
    
    Args:
        name (str ou None): Nome do usuário vindo da URL
        
    Returns:
        Response: Template 'user.html' renderizado com:
            - name: nome do usuário (ou None)
            - path: URL absoluta desta rota (gerada por url_for)
            - current_time: datetime atual em UTC para demonstração do Flask-Moment
    """
    # Gera URL absoluta para esta mesma rota (útil para demonstração/debug)
    path = url_for('user', name=name, _external=True)
    
    return render_template('user.html',
                           name=name,
                           path=path,
                           current_time=datetime.now(timezone.utc))


# =============================================================================
# MANIPULADORES DE ERRO
# =============================================================================

@app.errorhandler(404)
def page_not_found(e):
    """
    Manipulador de erro 404 - Página não encontrada.
    
    Args:
        e: Objeto de exceção (não utilizado, mas necessário pela assinatura)
        
    Returns:
        tuple: (template renderizado, código de status HTTP 404)
    """
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_server_error(e):
    """
    Manipulador de erro 500 - Erro interno do servidor.
    
    Args:
        e: Objeto de exceção
        
    Returns:
        tuple: (template renderizado, código de status HTTP 500)
    """
    return render_template('500.html'), 500


# =============================================================================
# ROTA PRINCIPAL (HOME)
# =============================================================================

@app.route('/')
def index():
    """
    Página inicial - redireciona para a página do usuário 'Julio'.
    
    Returns:
        Response: Redirecionamento HTTP 302 para /user/Julio
    """
    return redirect(url_for('user', name='Julio'))


# =============================================================================
# ROTA DE FORMULÁRIO - Demonstração de Sessão, Validação e Flash Messages
# =============================================================================

@app.route('/formulario', methods=['GET', 'POST'])
def formulario():
    """
    Página de formulário com validação WTForms, armazenamento em sessão
    e feedback via flash messages.
    
    Fluxo (padrão PRG - Post/Redirect/Get):
    1. GET: Exibe formulário vazio ou com nome da sessão
    2. POST: Valida dados -> Se válido, salva na sessão -> Redireciona para GET
    3. GET (após redirect): Exibe formulário com nome da sessão
    
    Returns:
        Response: Template 'formulario.html' renderizado com:
            - form: instância de FormularioTeste (WTForms)
            - name: nome armazenado na sessão (ou None)
    """
    # Instancia o formulário (WTForms carrega dados do request automaticamente no POST)
    form = FormularioTeste()
    
    # validate_on_submit() retorna True apenas se:
    # - Requisição é POST
    # - CSRF token é válido
    # - Todos os validadores passam (DataRequired no campo name)
    if form.validate_on_submit():
        # Recupera nome anterior da sessão (se existir)
        old_name = session.get('name')
        
        # Verifica se o nome foi alterado (não é None E é diferente do atual)
        if old_name is not None and old_name != form.name.data:
            # Flash message: exibida uma única vez no próximo request
            flash('Parece que você mudou o nome.')
        
        # Armazena novo nome na sessão (persiste entre requests)
        session['name'] = form.name.data
        
        # PRG Pattern: Redirect após POST para evitar reenvio ao recarregar página
        return redirect(url_for('formulario'))
    
    # GET ou POST com validação falha: renderiza template com formulário
    # session.get('name') retorna None se chave não existir (sem erro)
    return render_template('formulario.html',
                           form=form,
                           name=session.get('name'))

