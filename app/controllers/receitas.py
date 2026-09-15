from flask import (
    Blueprint, render_template, url_for, request, redirect, flash
)
from flask_login import login_required, current_user
from app.extensions import db
from app.models.tables import Receita, Categoria, TipoCategoria
from app.models.forms import ReceitaForm

bp = Blueprint('receitas', __name__, url_prefix='/receitas')


def _popular_categorias_form(form, tipo=TipoCategoria.RECEITA):
    """Popula o select de categorias do formulário."""
    categorias = Categoria.query.filter_by(
        user_id=current_user.id, 
        tipo=tipo
    ).order_by(Categoria.nome).all()
    form.categoria.choices = [(c.id, c.nome) for c in categorias]


@bp.route('/')
@login_required
def listar():
    receitas = Receita.query.filter_by(user_id=current_user.id).order_by(Receita.data_recebimento.desc()).all()
    return render_template('receitas/listar.html', receitas=receitas)


@bp.route('/nova', methods=['GET', 'POST'])
@login_required
def nova():
    form = ReceitaForm()
    _popular_categorias_form(form, TipoCategoria.RECEITA)
    
    if form.validate_on_submit():
        receita = Receita(
            descricao=form.descricao.data,
            valor=form.valor.data,
            data_recebimento=form.data_recebimento.data,
            categoria_id=form.categoria.data,
            user_id=current_user.id,
            observacoes=form.observacoes.data
        )
        db.session.add(receita)
        db.session.commit()
        flash('Receita criada com sucesso!', 'success')
        return redirect(url_for('receitas.listar'))
    
    return render_template('receitas/criar.html', form=form)


@bp.route('/<int:id>/editar', methods=['GET', 'POST'])
@login_required
def editar(id):
    receita = Receita.query.filter_by(id=id, user_id=current_user.id).first_or_404()
    form = ReceitaForm(obj=receita)
    _popular_categorias_form(form, TipoCategoria.RECEITA)
    
    if form.validate_on_submit():
        receita.descricao = form.descricao.data
        receita.valor = form.valor.data
        receita.data_recebimento = form.data_recebimento.data
        receita.categoria_id = form.categoria.data
        receita.observacoes = form.observacoes.data
        db.session.commit()
        flash('Receita atualizada com sucesso!', 'success')
        return redirect(url_for('receitas.listar'))
    
    # Preencher select com valor atual
    form.categoria.data = receita.categoria_id
    return render_template('receitas/editar.html', form=form, receita=receita)


@bp.route('/<int:id>/excluir', methods=['POST'])
@login_required
def excluir(id):
    receita = Receita.query.filter_by(id=id, user_id=current_user.id).first_or_404()
    db.session.delete(receita)
    db.session.commit()
    flash('Receita excluída com sucesso!', 'success')
    return redirect(url_for('receitas.listar'))