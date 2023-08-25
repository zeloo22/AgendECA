from flask import *
import time
app = Flask(__name__)
@app.route("/")
def hello():
  return render_template("index.html")

@app.route("/", methods = ["POST"])
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
    
    
@app.route("/buda", methods = ["POST", "GET"])
def adicionar():
  nome = request.form.get("nome")
  telefone = request.form.get("numero")
  txt = open("arquivo.txt", "a")
  info = "."
  if request.method == "POST":
    txt.write(f"nome: {nome}, telefone: {telefone}\n")
    txt.close()
    info = "Cadastro realizado com sucesso"
    return redirect(url_for("home"))
  return render_template("Buda.html", info=info)
app.run()