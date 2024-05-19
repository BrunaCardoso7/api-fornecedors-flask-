from . import db
class Fornecedor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    Fornecedor = db.Column(db.String(255))
    telefone = db.Column(db.String(20))
    revendedor = db.Column(db.String(255))