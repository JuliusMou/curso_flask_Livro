import enum
from app.extensions import db, login_manager
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin


class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)

    users = db.relationship('User', backref='role')

    def __repr__(self):
        return '<Role %r>' % self.name


class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(64), unique=True, index=True)
    email = db.Column(db.String(120), unique=True, index=True)
    password_hash = db.Column(db.String(256))

    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))

    # Relacionamentos com contas, receitas e categorias
    contas = db.relationship('Conta', backref='user', lazy='dynamic')
    receitas = db.relationship('Receita', backref='user', lazy='dynamic')
    categorias = db.relationship('Categoria', backref='user', lazy='dynamic')

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return '<User %r>' % self.user_name


class TipoCategoria(enum.Enum):
    DESPESA = 'despesa'
    RECEITA = 'receita'


class StatusConta(enum.Enum):
    PENDENTE = 'pendente'
    PAGO = 'pago'


class Categoria(db.Model):
    __tablename__ = 'categorias'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(64), nullable=False)
    tipo = db.Column(db.Enum(TipoCategoria), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    # Relacionamentos
    contas = db.relationship('Conta', backref='categoria', lazy='dynamic')
    receitas = db.relationship('Receita', backref='categoria', lazy='dynamic')

    def __repr__(self):
        return '<Categoria %r (%s)>' % (self.nome, self.tipo.value)


class Conta(db.Model):
    __tablename__ = 'contas'
    id = db.Column(db.Integer, primary_key=True)
    descricao = db.Column(db.String(128), nullable=False)
    valor = db.Column(db.Numeric(10, 2), nullable=False)
    data_vencimento = db.Column(db.Date, nullable=False)
    data_pagamento = db.Column(db.Date, nullable=True)
    status = db.Column(db.Enum(StatusConta), default=StatusConta.PENDENTE, nullable=False)
    observacoes = db.Column(db.Text, nullable=True)

    # Foreign Keys
    categoria_id = db.Column(db.Integer, db.ForeignKey('categorias.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    def __repr__(self):
        return '<Conta %r - R$ %s>' % (self.descricao, self.valor)


class Receita(db.Model):
    __tablename__ = 'receitas'
    id = db.Column(db.Integer, primary_key=True)
    descricao = db.Column(db.String(128), nullable=False)
    valor = db.Column(db.Numeric(10, 2), nullable=False)
    data_recebimento = db.Column(db.Date, nullable=False)
    observacoes = db.Column(db.Text, nullable=True)

    # Foreign Keys
    categoria_id = db.Column(db.Integer, db.ForeignKey('categorias.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    def __repr__(self):
        return '<Receita %r - R$ %s>' % (self.descricao, self.valor)


# --- ADICIONE ESTA PARTE NO FINAL ---
@login_manager.user_loader
def load_user(user_id):
    # Usamos db.session.get() que é o padrão do SQLAlchemy 2.0+
    return db.session.get(User, int(user_id))