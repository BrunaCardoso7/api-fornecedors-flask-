from flask_sqlalchemy import SQLAlchemy

# Cria uma instância do SQLAlchemy
db = SQLAlchemy()
# Importa os modelos definidos em outros arquivos
from app.models.Usuario import Usuario
from app.models.fornecedor import Fornecedor