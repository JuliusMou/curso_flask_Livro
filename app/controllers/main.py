from flask import (
    Blueprint, render_template, url_for, redirect
)
from flask_login import login_required, current_user
from app.extensions import db
from app.models.tables import Conta, Receita, Categoria, StatusConta, TipoCategoria
from sqlalchemy import func
from datetime import date

bp = Blueprint('main', __name__)


@bp.route('/')
@login_required
def index():
    # Estatísticas rápidas para o dashboard
    hoje = date.today()
    
    # Total de contas pendentes
    contas_pendentes = Conta.query.filter_by(
        user_id=current_user.id, 
        status=StatusConta.PENDENTE
    ).count()
    
    # Total de contas vencidas (pendentes com data_vencimento < hoje)
    contas_vencidas = Conta.query.filter(
        Conta.user_id == current_user.id,
        Conta.status == StatusConta.PENDENTE,
        Conta.data_vencimento < hoje
    ).count()
    
    # Soma das contas pendentes
    total_contas_pendentes = db.session.query(func.sum(Conta.valor)).filter(
        Conta.user_id == current_user.id,
        Conta.status == StatusConta.PENDENTE
    ).scalar() or 0
    
    # Soma das receitas do mês atual
    inicio_mes = date(hoje.year, hoje.month, 1)
    if hoje.month == 12:
        fim_mes = date(hoje.year + 1, 1, 1)
    else:
        fim_mes = date(hoje.year, hoje.month + 1, 1)
    
    total_receitas_mes = db.session.query(func.sum(Receita.valor)).filter(
        Receita.user_id == current_user.id,
        Receita.data_recebimento >= inicio_mes,
        Receita.data_recebimento < fim_mes
    ).scalar() or 0
    
    # Total de despesas do mês atual
    total_despesas_mes = db.session.query(func.sum(Conta.valor)).filter(
        Conta.user_id == current_user.id,
        Conta.data_vencimento >= inicio_mes,
        Conta.data_vencimento < fim_mes
    ).scalar() or 0
    
    # Últimas 5 contas
    ultimas_contas = Conta.query.filter_by(user_id=current_user.id).order_by(
        Conta.data_vencimento.desc()
    ).limit(5).all()
    
    # Últimas 5 receitas
    ultimas_receitas = Receita.query.filter_by(user_id=current_user.id).order_by(
        Receita.data_recebimento.desc()
    ).limit(5).all()
    
    return render_template('main/index.html',
                           contas_pendentes=contas_pendentes,
                           contas_vencidas=contas_vencidas,
                           total_contas_pendentes=total_contas_pendentes,
                           total_receitas_mes=total_receitas_mes,
                           total_despesas_mes=total_despesas_mes,
                           saldo_mes=total_receitas_mes - total_despesas_mes,
                           ultimas_contas=ultimas_contas,
                           ultimas_receitas=ultimas_receitas)