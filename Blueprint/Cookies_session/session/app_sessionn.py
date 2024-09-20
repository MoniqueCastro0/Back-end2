from flask import Flask, session
from datetime import timedelta

app = Flask(__name__)

app.config['SECRET_KEY'] = "frted92804"
app.config['PERMANEN_SESSION_LIFETIME'] = timedelta(minutes=5)

@app.route('/')
def ste_sessiomn():
    session.permanent = True
    session['usuario'] = 'João'
    return 'Sessão iniciada com sucesso'

@app.route('/get_session')
def get_session():
    usuario = session.get('usuario')
    return f'Usuario armazenado na sessão é: {usuario}'


if __name__ == "__main__":
    app.run(debug=True)