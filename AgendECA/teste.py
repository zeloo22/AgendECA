from doctest import debug
from flask import *
app = Flask(__name__)
@app.route("/")
def hello():
  return render_template("index.html")

@app.route("/", methods = ["POST", "GET"])
def login():
  if request.method == "POST":
    nome = request.form.get("nome")
    senha = request.form.get("senha")
  if nome == "Buda" and senha == "Buda":
    return redirect(url_for("home"))
  else:
    return f"<h1>bem vindo: {nome} sua senha foi:  {senha}</h1>"
    
    
@app.route("/home", methods =["POST", "GET"])
def home():
    return render_template("home.html")
    
    
@app.route("/adicionar", methods = ["POST", "GET"])
def adicionar():
  nome = request.form.get("nome")
  telefone = request.form.get("numero")
  txt = open("arquivo.txt", "a")
  if request.method == "POST":
    txt.write(f"nome: {nome}, telefone: {telefone}\n")
    txt.close()
    return redirect(url_for("sucesso")) 
  return render_template("adicionar.html")

@app.route("/sucesso", methods = ["POST", "GET"])
def sucesso():
  return render_template("sucesso.html")


if  __name__ == "__main__":
  app.run(debug=True)