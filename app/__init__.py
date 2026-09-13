from flask import Flask
from config import Config
from app.extensions import db, login_manager, bootstrap, moment

def create_app(config_class=Config):
    # 1. Cria a instância do Flask
    app = Flask(__name__)
    
    # 2. Carrega as configurações
    app.config.from_object(config_class)

    # 3. Inicializa as extensões com o app
    db.init_app(app)
    login_manager.init_app(app)
    bootstrap.init_app(app)
    moment.init_app(app)

    # 4. Registra as rotas (Blueprints)
    from app.controllers.default import bp as default_bp
    app.register_blueprint(default_bp)

    # 5. Importa os models para registrar o user_loader
    from app.models import tables

    return app