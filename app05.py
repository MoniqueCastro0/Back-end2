from flask import Flask

app = Flask(__name__)

@app.route("/")
def raiz():
    return "Rota raiz"

@app.route("/calc/<operation>/<int:n1>/<int:n2>")
def calculo(operation, n1, n2):
    operation = operation.lower()
    
    if operation == "soma":
        return f"Resultado da soma: {n1 + n2}"
    elif operation == "subtração":
        return f"Resultado da subtração: {n1 - n2}"
    
    elif operation == "divisão":
        return f"Resultado da divisão: {n1 / n2}"
    
    elif operation == "multiplicação":
        return f"Resultado da multiplicação: {n1 * n2}"
    else:
        return f'Operação invalida'
    
    
if __name__ == '__main__':
    app.run(debug=True, port=5001)
    
    