#Condicionais em templates
from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
def raiz():
    return "Rota raiz"

@app.route('/condicional')
def condicional():
    is_logged_in = True