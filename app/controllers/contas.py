from flask import (
    Blueprint, render_template, url_for, request, redirect, flash
)
from flask_login import login_required, current_user
from app.extensions import db
from app.models.tables import Conta, Categoria, StatusConta, TipoCategoria
from app.models.forms import ContaForm

bp = Blueprint('contas', __name__, url_prefix='/contas')


def _popular_categorias_form(form, tipo=TipoCategoria.DESPESA):
    """Popula o select de categorias do formulário."""
    categorias = Categoria.query.filter_by(
        user_id=current_user.id, 
        tipo=tipo
    ).order_by(Categoria.nome).all()
    form.categoria.choices = [(c.id, c.nome) for c in categorias]


@bp.route('/')
@login_required
def listar():
    contas = Conta.query.filter_by(user_id=current_user.id).order_by(Conta.data_vencimento.desc()).all()
    return render_template('contas/listar.html', contas=contas)


@bp.route('/nova', methods=['GET', 'POST'])
@login_required
def nova():
    form = ContaForm()
    _popular_categorias_form(form, TipoCategoria.DESPESA)
    
    if form.validate_on_submit():
        conta = Conta(
            descricao=form.descricao.data,
            valor=form.valor.data,
            data_vencimento=form.data_vencimento.data,
            data_pagamento=form.data_pagamento.data,
            status=StatusConta(form.status.data),
            categoria_id=form.categoria.data,
            user_id=current_user.id,
            observacoes=form.observacoes.data
        )
        db.session.add(conta)
        db.session.commit()
        flash('Conta criada com sucesso!', 'success')
        return redirect(url_for('contas.listar'))
    
    return render_template('contas/criar.html', form=form)


@bp.route('/<int:id>/editar', methods=['GET', 'POST'])
@login_required
def editar(id):
    conta = Conta.query.filter_by(id=id, user_id=current_user.id).first_or_404()
    form = ContaForm(obj=conta)
    _popular_categorias_form(form, TipoCategoria.DESPESA)
    
    if form.validate_on_submit():
        conta.descricao = form.descricao.data
        conta.valor = form.valor.data
        conta.data_vencimento = form.data_vencimento.data
        conta.data_pagamento = form.data_pagamento.data
        conta.status = StatusConta(form.status.data)
        conta.categoria_id = form.categoria.data
        conta.observacoes = form.observacoes.data
        db.session.commit()
        flash('Conta atualizada com sucesso!', 'success')
        return redirect(url_for('contas.listar'))
    
    # Preencher selects com valores atuais
    form.categoria.data = conta.categoria_id
    form.status.data = conta.status.value
    return render_template('contas/editar.html', form=form, conta=conta)


@bp.route('/<int:id>/excluir', methods=['POST'])
@login_required
def excluir(id):
    conta = Conta.query.filter_by(id=id, user_id=current_user.id).first_or_404()
    db.session.delete(conta)
    db.session.commit()
    flash('Conta excluída com sucesso!', 'success')
    return redirect(url_for('contas.listar'))


@bp.route('/<int:id>/toggle', methods=['POST'])
@login_required
def toggle_status(id):
    """Alterna o status da conta entre pendente e pago."""
    conta = Conta.query.filter_by(id=id, user_id=current_user.id).first_or_404()
    
    if conta.status == StatusConta.PENDENTE:
        conta.status = StatusConta.PAGO
        from datetime import date
        conta.data_pagamento = date.today()
        flash('Conta marcada como paga!', 'success')
    else:
        conta.status = StatusConta.PENDENTE
        conta.data_pagamento = None
        flash('Conta marcada como pendente!', 'info')
    
    db.session.commit()
    return redirect(url_for('contas.listar'))