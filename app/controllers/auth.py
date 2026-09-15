from flask import (
    Blueprint, render_template, url_for, request, redirect, flash
)
from flask_login import login_user, logout_user, login_required, current_user
from app.extensions import db
from app.models.tables import User, Role
from app.models.forms import LoginForm, RegisterForm

bp = Blueprint('auth', __name__, url_prefix='/auth')


@bp.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(user_name=form.user_name.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Usuário ou senha inválidos.', 'danger')
            return redirect(url_for('auth.login'))
        
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or not next_page.startswith('/'):
            next_page = url_for('main.index')
        return redirect(next_page)
    
    return render_template('auth/login.html', form=form)


@bp.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Você saiu do sistema.', 'info')
    return redirect(url_for('auth.login'))


@bp.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    
    form = RegisterForm()
    if form.validate_on_submit():
        # Verificar se usuário já existe
        if User.query.filter_by(user_name=form.user_name.data).first():
            flash('Nome de usuário já existe.', 'danger')
            return redirect(url_for('auth.register'))
        
        if User.query.filter_by(email=form.email.data).first():
            flash('E-mail já cadastrado.', 'danger')
            return redirect(url_for('auth.register'))
        
        # Criar role padrão se não existir
        role = Role.query.filter_by(name='user').first()
        if not role:
            role = Role(name='user')
            db.session.add(role)
            db.session.commit()
        
        user = User(
            user_name=form.user_name.data,
            email=form.email.data,
            role=role
        )
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        
        flash('Registro realizado com sucesso! Faça login.', 'success')
        return redirect(url_for('auth.login'))
    
    return render_template('auth/register.html', form=form)