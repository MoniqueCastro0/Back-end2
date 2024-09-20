from flask import Flask
from flask import render_template

# 
app = Flask(__name__)

@app.route("/")
def home():
    
    return render_template('layout.html')

@app.route("/sobre")
def sobre():
    return render_template('sobre.html')

@app.route("/contato")
def contato():
    return render_template('conctact.html')

@app.route("/team")
def team():
    return render_template('team.html')




if __name__ == '__main__':
    app.run(debug=True)
