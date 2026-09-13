from app.extensions import db, login_manager

class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)

    users = db.relationship('User', backref='role')

    def __repr__(self):
        return '<Role %r>' % self.name

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(64), unique=True, index=True)

    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))

    def __repr__(self):
        return '<User %r>' % self.user_name

# --- ADICIONE ESTA PARTE NO FINAL ---
@login_manager.user_loader
def load_user(user_id):
    # Usamos db.session.get() que é o padrão do SQLAlchemy 2.0+
    return db.session.get(User, int(user_id))