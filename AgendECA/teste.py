from doctest import debug
from flask import *
import time

def mostra():
  txt = open("arquivo.txt", "r")
  linha = txt.readline()
  usuario = []
  for linha in txt:
    usuario.append(linha)
  return usuario

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
  acao = "adicionar"
  dados = mostra()
  nome = request.form.get("nome")
  telefone = request.form.get("numero")
  txt = open("arquivo.txt", "a")
  if request.method == "POST":
    txt.write(f"nome: {nome}, telefone: {telefone}\n")
    txt.close()
    return redirect(url_for("home")) 
  return render_template("acao.html", acao=acao, dados=dados)

@app.route("/mostrar", methods = ["POST", "GET"])
def mostrar():
  dados = mostra()
  return render_template("mostrar.html", dados = dados)


@app.route("/remover", methods = ["POST", "GET"])
def remover():
  acao = "remover"
  dados = mostra()
  txt = open("arquivo.txt", "r")
  linhas = txt.readlines()
  if request.method == "POST":
    nome = request.form.get("nome")
    numero = request.form.get("numero")
    txw = open("arquivo.txt", "w")
    for i in linhas:
      if i.strip('\n') != f"nome: {nome}, telefone: {numero}":
        txw.write(i)
    txt.close()
    txw.close()
    return redirect(url_for("home"))
  return render_template("acao.html", acao = acao, dados = dados)


@app.route("/alterar", methods = ["POST", "GET"])
def alterar():
  dados = mostra()
  nome = request.form.get("nome")
  nomet = request.form.get("nomet")
  numero = request.form.get("numero")
  numerot = request.form.get("numerot")
  cont = 0
  txt = open("arquivo.txt", "r")
  linha = txt.readlines()
  if request.method == "POST":
    for i in linha:
      if i.strip("\n") == f"nome: {nome}, telefone: {numero}":
        linha[cont] = f"nome: {nomet}, telefone: {numerot}\n"
      cont+=1
    txw = open("arquivo.txt", "w")
    for i in linha:
      txw.write(i)
    return redirect(url_for("home")) 
  return render_template("alterar.html", dados = dados)



if  __name__ == "__main__":
  app.run(debug=True)