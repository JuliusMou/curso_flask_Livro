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
    
    # Configurar login_manager
    login_manager.login_view = 'auth.login'
    login_manager.login_message = 'Por favor, faça login para acessar esta página.'
    login_manager.login_message_category = 'info'
    
    # 4. Registra as rotas (Blueprints)
    from app.controllers.auth import bp as auth_bp
    app.register_blueprint(auth_bp)
    
    from app.controllers.main import bp as main_bp
    app.register_blueprint(main_bp)
    
    from app.controllers.categorias import bp as categorias_bp
    app.register_blueprint(categorias_bp)
    
    from app.controllers.contas import bp as contas_bp
    app.register_blueprint(contas_bp)
    
    from app.controllers.receitas import bp as receitas_bp
    app.register_blueprint(receitas_bp)
    
    # 5. Importa os models para registrar o user_loader
    from app.models import tables
    
    # 6. Criar tabelas se não existirem
    with app.app_context():
        db.create_all()
    
    return app