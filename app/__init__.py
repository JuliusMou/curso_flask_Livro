from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask import Flask
import os
from flask_sqlalchemy import SQLAlchemy

basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
bootstrap = Bootstrap(app)
moment = Moment(app)
app.config.from_object('config')
db = SQLAlchemy(app)


from app.controllers import default
