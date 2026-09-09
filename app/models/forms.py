from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField
from wtforms.fields.choices import RadioField, SelectField, SelectMultipleField
from wtforms.fields.datetime import DateField, DateTimeField
from wtforms.fields.form import FormField
from wtforms.fields.list import FieldList
from wtforms.fields.numeric import DecimalField, FloatField, IntegerField
from wtforms.fields.simple import BooleanField, FileField, HiddenField, MultipleFileField, PasswordField, TextAreaField
from wtforms.validators import DataRequired, Email


# Criação de formulário para teste utilizando o Livro Flask
# Definição de classe de formulário
class FormularioTeste(FlaskForm):
    name = StringField('Qual é o seu nome: ', validators=[DataRequired()])
    submit = SubmitField('Submit')
    remenber_me = BooleanField('Lembre-me')
    '''
    data = DateField('Data')
    dataHora = DateTimeField('Data e Hora')
    decimal = DecimalField('Valor Decimal')
    file = FileField('Uploader')
    hidden = HiddenField('Campo oculto')
    multiple_file_field = MultipleFileField('Uploaders')
    floatField = FloatField('Float')
    integerField = IntegerField('Inteiro')
    password = PasswordField('Senha')
    radio = RadioField('Música')
    select = SelectField('Lista')
    selectMultiple = SelectMultipleField('Listas')
    text = TextAreaField('Texto')
    email = StringField('E-mail', validators=[Email()])
    '''






