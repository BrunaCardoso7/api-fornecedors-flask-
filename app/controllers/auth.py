from flask import session
from app.models.Usuario import Usuario

def authenticate(username, password):
    user = Usuario.query.filter_by(usuario=username, senha=password).first()
    if user:
        session['username'] = username
        session['user_type'] = user.tipo
        return True
    else:
        return False

def logout():
    session.pop('username', None)
    session.pop('user_type', None)