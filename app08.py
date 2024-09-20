from flask import Flask
from flask import render_template

# 
app = Flask(__name__)

@app.route("/")
def raiz():
    return "Rota raiz"

@app.route('/lista')
def tarefas():
    lista = ['Corre', 'Estudar', 'Assitir']
    return render_template('index.html', lista = lista)

if __name__ == '__main__':
    app.run(debug=True)