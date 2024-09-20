from app import db
from app.models import fruta
from app import app

with app.app_context():
    users = fruta.query.all()
    print(users)