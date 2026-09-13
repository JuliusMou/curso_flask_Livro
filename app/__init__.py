# app/__init__.py
from flask import Flask
from config import Config
from app.extensions import db, login_manager
from app.controllers import default
from flask_bootstrap import Bootstrap
from flask_moment import Moment
import os
from flask_sqlalchemy import SQLAlchemy

def create_app(config_class=Config):
    # 1. Cria a instância do Flask
    app = Flask(__name__)
    
    # 2. Carrega as configurações
    app.config.from_object(config_class)

    # 3. Inicializa as extensões com o app
    db.init_app(app)
    login_manager.init_app(app)

    # 4. Registra as rotas (Blueprints)
    from app.controllers.auth import bp_auth
    app.register_blueprint(bp_auth, url_prefix='/auth')

    # 5. 
    moment = Moment(app)

    bootstrap = Bootstrap(app)

    basedir = os.path.abspath(os.path.dirname(__file__))

    return app
