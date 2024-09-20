from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def home():
    usuario = {
        "nome": "João",
        "idade": 32,
        "cidade": "Rua Alegre,123"
    }
    return render_template('index2.html', usuario = usuario)
if __name__ == '__main__':
    app.run(debug=True)