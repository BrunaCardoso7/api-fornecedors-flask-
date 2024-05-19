from flask import Blueprint
# Cria um Blueprint chamado 'routes'
routes_bp = Blueprint('routes', __name__)
# Importa as rotas definidas em outros arquivos
from app.routes import home