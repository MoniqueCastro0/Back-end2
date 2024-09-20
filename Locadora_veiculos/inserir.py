from app import db
# """ from models import User """
from app.models import fruta
from app import app





with app.app_context():
    
    nova_fruta = fruta(
        nome = 'Tomate',
        senha=123,
        tipo="b",
        status="a",
        descricao = 'Um morango fresquinha pra você e sua famly',
        id_usuario = db.Column(db.Integer, primary_key=True)
        )

    db.session.add(nova_fruta)
    db.session.commit()
    print('Fruta foi adicionada')

""" with app.app_context():
    novo_usuario = User(username='Maria', email='maria@out.com')
    db.session.add(novo_usuario)
    db.session.commit() """