from flask import (
    Blueprint,        # IMPORTANTE: Adicionado o Blueprint
    render_template, 
    url_for,          
    request,          
    redirect,         
    session,          
    flash             
)
from datetime import datetime, timezone
from app.models.forms import FormularioTeste

# Criamos o Blueprint para este arquivo
bp = Blueprint('default', __name__)


@bp.route('/user/<name>')
@bp.route('/user', defaults={'name': None})
def user(name):
    # ATENÇÃO: Adicionado 'default.' antes do nome da função
    path = url_for('default.user', name=name, _external=True)
    return render_template('user.html',
                           name=name,
                           path=path,
                           current_time=datetime.now(timezone.utc))

# Tratamento de erro global usando app_errorhandler no blueprint
@bp.app_errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@bp.app_errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500


@bp.route('/')
def index():
    # ATENÇÃO: Adicionado 'default.' antes do nome da função
    return redirect(url_for('default.user', name='Julio'))


@bp.route('/formulario', methods=['GET', 'POST'])
def formulario():
    form = FormularioTeste()
    
    if form.validate_on_submit():
        old_name = session.get('name')
        if old_name is not None and old_name != form.name.data:
            flash('Parece que você mudou o nome.')
        
        session['name'] = form.name.data
        
        # ATENÇÃO: Adicionado 'default.' antes do nome da função
        return redirect(url_for('default.formulario'))
    
    return render_template('formulario.html',
                           form=form,
                           name=session.get('name'))

@bp.route('/perfil')
def perfil():
    # Tenta pegar o nome que está salvo na sessão (memória do navegador)
    nome = session.get('name')
    
    # Se existe um nome na sessão, mostramos uma mensagem de boas vindas
    if nome:
        return f"<h1>Bem-vindo ao seu perfil, {nome}!</h1>"
    
    # Se não existe (usuário não preencheu o formulário), mandamos ele de volta
    else:
        flash("Acesso negado: Por favor, identifique-se preenchendo o formulário primeiro.")
        return redirect(url_for('default.formulario'))