from . import db # Importe o objeto db do módulo app.models
class Produto(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    produto = db.Column(db.String(255))
    idfornecedor = db.Column(db.Integer, db.ForeignKey('fornecedor.id')) # Chave estrangeira para o fornecedor
# Define o relacionamento com o fornecedor
    fornecedor = db.relationship('Fornecedor', backref='produtos')
    def __repr__(self):
        return f"<Produto {self.produto}>"