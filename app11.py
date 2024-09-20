from flask import Flask
from flask import render_template

app = Flask(__name__)

""" @app.route("/")
def raiz():
    return "Rota raiz" """

@app.route("/")
def perfil():
    usuarios = [
        {
        "nome": "João",
        "endereco": "Rua das flores, 123, São Paulo, SP",
        "telefone": "(11) 987530-9212", 
        "email": "Joanzinho@gmil",
        "cpf": "123.654.324-98", 
        "tipo_de_conta": "cliente"
        
    },{
        "nome": "Lucas",
        "endereco": "Rua das cores, 203, São Paulo, SP",
        "telefone": "(11) 90030-9212", 
        "email": "Luquinhazinho@gmil",
        "cpf": "023.654.324-98", 
        "tipo_de_conta": "cliente"
    },{
        "nome": "Ana",
        "endereco": "Rua das Dores, 398, São Paulo, SP",
        "telefone": "(41) 9090-9212", 
        "email": "Joanzinho@gmil",
        "cpf": "119.654.324-98", 
        "tipo_de_conta": "cliente"
    }]
    return render_template('usuarios.html', usuarios = usuarios)

if __name__ == '__main__':
    app.run(debug=True)