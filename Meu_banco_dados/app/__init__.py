from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

#cria a função para mostrar a aplicação e a retorna
def create_app():
    app = Flask(__name__)
    
    #configuração banco dados SQLite
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///meubanco.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    #inicializa o metodo db para app
    db.init_app(app)
    
    #Importando e registramos o Blueprint
    from .routes import bp
    app.register_blueprint(bp)
    #Fim: Importando e registramos o Blueprint
    
    #retorno da montagem do app
    return app