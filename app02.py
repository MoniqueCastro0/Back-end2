from flask import Flask

app = Flask(__name__)

@app.route("/")
def raiz():
    return "Rota raiz"

@app.route("/soma/<int:a>/<int:b>")
def somar(a,b):
    soma = a + b
    return f'A soma desse num é: {soma}'

if __name__ == '__main__':
    app.run(debug=True)
    