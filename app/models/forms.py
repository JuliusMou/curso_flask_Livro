from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField
from wtforms.fields.simple import BooleanField
from wtforms.validators import DataRequired, Email, Length


class FormularioTeste(FlaskForm):
    # Adicionamos Length para exigir entre 3 e 50 caracteres
    name = StringField('Qual é o seu nome: ', validators=[DataRequired(), Length(min=3, max=50)])
    
    # Criamos um campo de email obrigatório
    email = StringField('E-mail', validators=[DataRequired(), Email()])
    
    remenber_me = BooleanField('Lembre-me')
    submit = SubmitField('Submit')