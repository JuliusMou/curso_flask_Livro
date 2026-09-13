from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bootstrap import Bootstrap
from flask_moment import Moment

# Criamos as instâncias "vazias"
db = SQLAlchemy()
login_manager = LoginManager()
bootstrap = Bootstrap()
moment = Moment()