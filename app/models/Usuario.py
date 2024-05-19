from . import db
class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    usuario = db.Column(db.String(15))
    senha = db.Column(db.String(255))
    tipo = db.Column(db.String(255))