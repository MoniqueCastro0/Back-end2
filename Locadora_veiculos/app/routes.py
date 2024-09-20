from flask import Blueprint, render_template, Request
""" from .models import fruta """

#cria um blueprint para as rotas
bp = Blueprint('main', __name__)

#define a rota pagina inicial
@bp.route('/')
def index():
    return 'Ola mundo'

@bp.routes('/enviar', methods=['GET', 'POST'])
def enviar():
    if request.method == 'POST':
        nova
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
""" @bp.route('/frutas_caras')
def frutas_caras():
    frutas = fruta.query.all() #traga todos os registros
    return render_template('frutas_caras.html', frutas=frutas) """    