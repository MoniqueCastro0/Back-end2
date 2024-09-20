from flask import Flask
from flask import render_template, request

# 
app = Flask(__name__)

@app.route("/")
def home():
    nome = "Monique"
    return render_template('miolo.html')

@app.route("/sobre",methods=['GET'])
def sobre():
    palavra = request.args.get('palavra')
    return render_template('sobre.html', palavra=palavra)

#Atv1
@app.route("/info",methods=['GET'])
def info():
    nome = request.args.get('nome')
    idade = request.args.get('idade')
    return render_template('sobre.html', nome=nome, idade=idade)
#Atv1

""" @app.route("/saudacao",methods=['GET'])
def saudacao():
    nome = request.args.get('nome')
    if nome == "":
        return f"Olá visitante
    return render_template('sobre.html', nome=nome) """


#incompleto
#Atv3
@app.route("/produtos",methods=['GET'])
def produtos():
    categoria = request.args.get('categoria')
    produto = [
        {
        "nome": "João",
        "Catecoria": "A", 
        
    },{
        "nome": "Lucas",
        "Categoria": "B", 
        
    },{
        "nome": "Ana",
        "Categoria": "C"
    }]
    return render_template('sobre.html', produtos = produto, categoria = categoria)
#Atv3



#Atv4 - validação de parametro
@app.route("/verificar",methods=['GET'])
def verificar():
    numero = request.args.get('numero')
    
    return render_template('sobre.html', numero = numero)
#Atv4



@app.route("/contato")
def contato():
    return render_template('conctact.html')

@app.route("/team")
def team():
    return render_template('team.html')



#Metodo POST
@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == "POST":
        usuario = request.form['usuario']
        return f'Formulario submetido com sucesso! Olá, {usuario}'
    
    return '''
        <form method=POST action='/submit'>
            <label for"usuario">Nome do usuario: </label><br>
            <input type="text" id="usuario" name="usuario"<br>
            <input type="submit" value="enviar">
        </form>
'''



if __name__ == '__main__':
    app.run(debug=True)
