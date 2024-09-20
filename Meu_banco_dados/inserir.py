from app import db
# """ from models import User """
from app.models import fruta
from app import app
from datetime import date




with app.app_context():
    
    nova_fruta = fruta(
        nome = 'Tomate',
        preco=6.40,
        datacolheita=date(2027,8,25),
        vencimento=date(2028,9,5),
        descricao = 'Um morango fresquinha pra você e sua famly'
        )

    db.session.add(nova_fruta)
    db.session.commit()
    print('Fruta foi adicionada')

""" with app.app_context():
    novo_usuario = User(username='Maria', email='maria@out.com')
    db.session.add(novo_usuario)
    db.session.commit() """