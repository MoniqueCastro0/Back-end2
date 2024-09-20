from flask import Flask

app = Flask(__name__)

@app.route("/")
def raiz():
    return "Rota raiz"

@app.route("/hello")
def holla():
    return "Olá, mundo!"

@app.route("/bye")
def bye():
    return "Adeus, Mundo!"

if __name__ == "__main__":
    app.run(debug=True)