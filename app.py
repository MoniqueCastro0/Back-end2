
#importa a classe flask do modulo flask
from flask import Flask


# 
app = Flask(__name__)

@app.route("/")
def home():
    return "Olá, flask"

@app.route("/rota")
def rota():
    return "Olá, Rota"

@app.route("/mesagem/<nome>")
def contato(nome):
    return f"Olá, querido {nome}"

 

if __name__ == '__main__':
    app.run(debug=True)
    
