from flask import Flask, request, make_response

app = Flask(__name__)

@app.route('/')
def set_cookie():
    response = make_response('Cookie foi definido')
    response.set_cookie('username', 'Monique', max_age=60*60*24) #username = nome da chave / Monique = valor da chave
    return response

#resgatando valor do cookie
@app.route('/get_cookie') #get = resgata
def get_cookie():
    usuario = request.cookies.get('username')
    return f'usuário armazenado no cookie é: {usuario}'

# 1-------------------------------------------------------------------------------------------------------
@app.route('/definir_cookie')
def definir_cookie():
    response = make_response('Atividade 1')
    response.set_cookie('mensagem', 'Deu certo!', max_age=60*60*24)
    return response

@app.route('/obter_cookie')
def ler_cookie():
    mensagem = request.cookies.get('mensagem')
    return f'Mensagem do cookie2: {mensagem}'
#-------------------------------------------------------------------------------------------------------



#2------------------------------------------------------------------------------------------------------- INCOMPLETA
@app.route('/visitas')
def visitas():
    response = make_response('Atividade 2')
    response.set_cookie('visitas', '1', max_age=60*60*24)
    return response

@app.route('/obter_visitas')
def ler_visitas():
    visitas = int(request.cookies.get('visitas')) +1
    """ contador += 1 """
    return f'Cantidade de visitas: {visitas}'
#2-------------------------------------------------------------------------------------------------------

#3-------------------------------------------------------------------------------------------------------
@app.route('/definir_expiracao_cookie')
def visitas():
    response = make_response('Atividade 3')
    response.set_cookie('session_id', 'A', max_age=30)
    return response

@app.route('/check_expiracao_cookie')
def ler_cookie():
    mensagem = request.cookies.get('mensagem')
    return f'Mensagem do cookie2: {mensagem}'
if response ==


if __name__ == "__main__":
    app.run(debug=True)