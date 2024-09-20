from flask import Flask
from flask import render_template

# 
app = Flask(__name__)

@app.route("/")
def home():
    nome = "Monique"
    return render_template('index.html', varnome = nome)
    """ user = {'username': 'Miguel'}
    return '''
<html>
    <head>
        <title>Home Page - Microblog</title>
    </head>
    <body>
        <h1>Olá, ''' + user['username'] + '''!</h1>
    </body>
</html>''' """

@app.route('/lista')
def tarefas():
    lista = ['ovos', 'leite', 'laranja', 'oleo', 'fandangos', 'doritos', 'miojo', 'amendoim']
    return render_template('tarefas.html', listacompras = lista)


@app.route('/perfil')
def perfil():
    usuario = {
        "nome": "João",
        "idade": 32, 
        "email": "Joanzinho@gmil"
    }
    return render_template('perfil.html', usuario = usuario)
if __name__ == '__main__':
    app.run(debug=True)
