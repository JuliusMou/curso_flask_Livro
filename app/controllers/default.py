from app import app
from flask import render_template, url_for, request, redirect, session, flash
from datetime import datetime, timezone
from app.models.forms import FormularioTeste


@app.route('/user/<name>')
@app.route('/user', defaults={'name': None})
def user(name):
    path = url_for('user', name=name, _external=True)
    return render_template('user.html',
                           name=name,
                           path=path,
                           current_time = datetime.now(timezone.utc)
                           )

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500

@app.route('/')
def index():
    return redirect(url_for('user', name='Julio'))

@app.route('/formulario', methods=['GET','POST'])
def formulario():
    ''' name = None
    form= FormularioTeste()
    if form.validate_on_submit():
        name = form.name.data
        form.name.data = ''
    return render_template('formulario.html',
                           form=form,
                           name=name
                           ) '''
    '''
    form = FormularioTeste()
    if form.validate_on_submit():
        session['name'] = form.name.data
        return redirect(url_for('formulario'))
    return render_template('formulario.html',
                           form = form,
                           name = session.get('name')
                           ) '''
    form = FormularioTeste()
    if form.validate_on_submit():
        old_name = session.get('name')
        if old_name is not None and old_name != form.name.data:
            flash('Parece que você mudou o nome.')
        session['name'] = form.name.data
        return redirect(url_for('formulario'))
    return render_template('formulario.html',
                           form = form,
                           name = session.get('name'))

