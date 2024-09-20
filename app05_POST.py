from flask import Flask
from flask import render_template, request
from werkzeug.utils import secure_filename
app = Flask(__name__)

@app.route("/")
def home():
    return render_template('miolo.html')


""" #Metodo POST
@app.route('/enviar', methods=['GET', 'POST'])
def enviar():
    if request.method == "POST":
        nome_usuario = request.form['nome']
        email_usuario = request.form['email']
        if nome_usuario == " " and email_usuario == " ":
            return f"Erro! Prencha os 2 campos!!!"
        return f'Formulario submetido com sucesso! Olá, {nome_usuario} seu email é: {email_usuario}'
    
    return '''
        <form method=POST action='/enviar'>
            <label for"nome">Nome do usuario: </label><br>
            <input type="text" id="nome" name="nome"<br>
            
            <label for"email">Email do usuario: </label><br>
            <input type="text" id="email" name="email"<br>
            
            <input type="submit" value="enviar">
        </form>
''' """

#Metodo POST
"""@app.route('/enviar', methods=['GET', 'POST'])
def enviar():
    if request.method == "POST":
        nome_usuario = request.form['nome']
        email_usuario = request.form['email']
        usuarios = [
            {
                "nome": "João",
                "email": "Joanzinho@gmil"
        
        },{
                "nome": "Lucas",
                "email": "Luquinhazinho@gmil",
        },{
                "nome": "Ana", 
                "email": "Aninha@gmil",
        }]
        usuarios.insert(3, nome_usuario)
        usuarios.insert(4, email_usuario)
        return f'Formulario submetido com sucesso! Olá, {usuarios}' 
        return '''
        <form method=POST action='/enviar'>
            <tr>
                <td>Nome: {usuarios}</td>
                <td>Email: {{usuario['email']}}</td>
            </tr>
        </form>
'''
    
    return '''
        <form method=POST action='/enviar'>
            <label for"nome">Nome do usuario: </label><br>
            <input type="text" id="nome" name="nome"<br>
            
            <label for"email">Email do usuario: </label><br>
            <input type="text" id="email" name="email"<br>
            
            <input type="submit" value="enviar">
        </form>
'''"""

""" @app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        nome_usuario = request.form['nome']
        senha = request.form['senha']
        if nome_usuario == " " and senha == " ":
            return f"Erro! Prencha os 2 campos!!!"
        else:
            return f'Login realizado com sucesso!'
        
    
    return '''
        <form method=POST action='/login'>
            <label for"nome">Nome do usuario: </label><br>
            <input type="text" id="nome" name="nome"<br>
            
            <label for"senha">Email do usuario: </label><br>
            <input type="text" id="senha" name="senha"<br>
            
            <input type="submit" value="enviar">
        </form>
''' """

""" @app.route('/upload', methods=['GET', 'POST']) #essa rota recebe metodo get e post
def upload():
    if request.method == 'POST':
        file = request.files['arquivo'] #atributo name
        
        file.save(f'upload/{secure_filename(file.filename)}') #secure_filename - segurança
        return "Formulário salvo com sucesso!"

    return '''
        <form method=POST action='/upload' enctype="multipart/form-data">
            <input type="file" id="arquivo" name="arquivo"<br>
            <input type="file" id="arquivo" name="arquivo"<br>
            
    
            
            <input type="submit" value="enviar">
        </form>
''' """

@app.route('/upload', methods=['GET', 'POST']) #essa rota recebe metodo get e post
def upload():
    if request.method == 'POST':
        file = request.files['arquivo'] #atributo name
        file.filename = "Arquivos.uploads"
        print(file)
        
        file.save(f'arquivos/{secure_filename(file.filename)}') #secure_filename - segurança
        
        """ return "Formulário salvo com sucesso!" """
        return f'nome do arquivo: {file.filename}'
    return '''
        <form method=POST action='/upload' enctype="multipart/form-data">
            <input type="file" id="arquivo" name="arquivo"<br>
            <input type="file" id="arquivo" name="arquivo"<br>
            
            
    
            
            <input type="submit" value="enviar">
        </form>
'''

if __name__ == '__main__':
    app.run(debug=True)