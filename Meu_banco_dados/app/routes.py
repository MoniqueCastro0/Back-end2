from flask import Blueprint, render_template
from .models import fruta

#cria um blueprint para as rotas
bp = Blueprint('main', __name__)

#define a rota pagina inicial
@bp.route('/')
def index():
    return 'Ola mundo'

@bp.route('/frutas_caras')
def frutas_caras():
    frutas = fruta.query.filter(fruta.preco > 3.00).all() #traga todos os registros
    return render_template('frutas_caras.html', frutas=frutas)