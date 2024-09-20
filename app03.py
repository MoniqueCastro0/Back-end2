from flask import Flask

app = Flask(__name__)

@app.route("/")
def raiz():
    return "Rota raiz"

@app.route("/invert/<text>")
def inverter(text):
    texto = text
    texto_invertido = texto[::-1]
    return texto_invertido

if __name__ == '__main__':
    app.run(debug=True)
    