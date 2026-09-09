import os.path
from app import basedir

SECRET_KEY='290317@aNT'
SQLALCHEMY_DATABASE_URI = 'sqlite:///'+os.path.join(basedir,'data.sqlite')
SQLALCHEMY_TRACK_MODIFICATIONS = False



