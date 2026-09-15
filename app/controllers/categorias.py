from flask import (
    Blueprint, render_template, url_for, request, redirect, flash
)
from flask_login import login_required, current_user
from app.extensions import db
from app.models.tables import Categoria, TipoCategoria
from app.models.forms import CategoriaForm

bp = Blueprint('categorias', __name__, url_prefix='/categorias')


@bp.route('/')
@login_required
def listar():
    categorias = Categoria.query.filter_by(user_id=current_user.id).order_by(Categoria.tipo, Categoria.nome).all()
    return render_template('categorias/listar.html', categorias=categorias)


@bp.route('/nova', methods=['GET', 'POST'])
@login_required
def nova():
    form = CategoriaForm()
    if form.validate_on_submit():
        categoria = Categoria(
            nome=form.nome.data,
            tipo=TipoCategoria(form.tipo.data),
            user_id=current_user.id
        )
        db.session.add(categoria)
        db.session.commit()
        flash('Categoria criada com sucesso!', 'success')
        return redirect(url_for('categorias.listar'))
    return render_template('categorias/criar.html', form=form)


@bp.route('/<int:id>/editar', methods=['GET', 'POST'])
@login_required
def editar(id):
    categoria = Categoria.query.filter_by(id=id, user_id=current_user.id).first_or_404()
    form = CategoriaForm(obj=categoria)
    
    if form.validate_on_submit():
        categoria.nome = form.nome.data
        categoria.tipo = TipoCategoria(form.tipo.data)
        db.session.commit()
        flash('Categoria atualizada com sucesso!', 'success')
        return redirect(url_for('categorias.listar'))
    
    # Preencher o select com o valor atual
    form.tipo.data = categoria.tipo.value
    return render_template('categorias/editar.html', form=form, categoria=categoria)


@bp.route('/<int:id>/excluir', methods=['POST'])
@login_required
def excluir(id):
    categoria = Categoria.query.filter_by(id=id, user_id=current_user.id).first_or_404()
    
    # Verificar se há contas ou receitas vinculadas
    if categoria.contas.count() > 0 or categoria.receitas.count() > 0:
        flash('Não é possível excluir: existem contas ou receitas vinculadas a esta categoria.', 'danger')
        return redirect(url_for('categorias.listar'))
    
    db.session.delete(categoria)
    db.session.commit()
    flash('Categoria excluída com sucesso!', 'success')
    return redirect(url_for('categorias.listar'))