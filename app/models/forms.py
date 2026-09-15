from flask_wtf import FlaskForm
from wtforms import (
    SubmitField, StringField, PasswordField, BooleanField,
    SelectField, TextAreaField, DecimalField, DateField
)
from wtforms.validators import DataRequired, Email, Length, EqualTo, Optional, NumberRange
from app.models.tables import TipoCategoria, StatusConta


class LoginForm(FlaskForm):
    user_name = StringField('Usuário', validators=[DataRequired(), Length(min=3, max=64)])
    password = PasswordField('Senha', validators=[DataRequired()])
    remember_me = BooleanField('Lembrar-me')
    submit = SubmitField('Entrar')


class RegisterForm(FlaskForm):
    user_name = StringField('Usuário', validators=[DataRequired(), Length(min=3, max=64)])
    email = StringField('E-mail', validators=[DataRequired(), Email(), Length(max=120)])
    password = PasswordField('Senha', validators=[DataRequired(), Length(min=6)])
    password2 = PasswordField('Confirmar Senha', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Registrar')


class CategoriaForm(FlaskForm):
    nome = StringField('Nome', validators=[DataRequired(), Length(min=2, max=64)])
    tipo = SelectField('Tipo', choices=[
        (TipoCategoria.DESPESA.value, 'Despesa'),
        (TipoCategoria.RECEITA.value, 'Receita')
    ], validators=[DataRequired()])
    submit = SubmitField('Salvar')


class ContaForm(FlaskForm):
    descricao = StringField('Descrição', validators=[DataRequired(), Length(min=2, max=128)])
    valor = DecimalField('Valor', validators=[DataRequired(), NumberRange(min=0.01)], places=2)
    data_vencimento = DateField('Data de Vencimento', format='%Y-%m-%d', validators=[DataRequired()])
    data_pagamento = DateField('Data de Pagamento', format='%Y-%m-%d', validators=[Optional()])
    status = SelectField('Status', choices=[
        (StatusConta.PENDENTE.value, 'Pendente'),
        (StatusConta.PAGO.value, 'Pago')
    ], validators=[DataRequired()])
    categoria = SelectField('Categoria', coerce=int, validators=[DataRequired()])
    observacoes = TextAreaField('Observações', validators=[Optional(), Length(max=500)])
    submit = SubmitField('Salvar')


class ReceitaForm(FlaskForm):
    descricao = StringField('Descrição', validators=[DataRequired(), Length(min=2, max=128)])
    valor = DecimalField('Valor', validators=[DataRequired(), NumberRange(min=0.01)], places=2)
    data_recebimento = DateField('Data de Recebimento', format='%Y-%m-%d', validators=[DataRequired()])
    categoria = SelectField('Categoria', coerce=int, validators=[DataRequired()])
    observacoes = TextAreaField('Observações', validators=[Optional(), Length(max=500)])
    submit = SubmitField('Salvar')