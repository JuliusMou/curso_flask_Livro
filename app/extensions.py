# app/extensions.py
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

# Criamos as instâncias "vazias"
db = SQLAlchemy()
login_manager = LoginManager()