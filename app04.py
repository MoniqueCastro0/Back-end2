from flask import Flask

app = Flask(__name__)

@app.route("/")
def raiz():
    return "Rota raiz"

@app.route("/paridade/<int:n>")
def paridade(n):
    num = n
    if num % 2 == 0:
        return f"Esse número é PAR"
    else:
        return f"Esse número é IMPAR"
    
if __name__ == '__main__':
    app.run(debug=True)