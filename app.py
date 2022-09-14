

from flask import Flask, render_template, request, session, redirect, url_for

app = Flask(__name__)

# Criando uma chave de criptografia
app.secret_key = "c!ds@%kc*&%nds@dsa{wdp"

produtos = [
    {"nome": "Produto 1", "preco": "R$ ***"},
    {"nome": "Produto 2", "preco": "R$ ***"},
    {"nome": "Produto 3", "preco": "R$ ***"},
    {"nome": "Produto 4", "preco": "R$ ***"},
    {"nome": "Produto 5", "preco": "R$ ***"},
    {"nome": "Produto 6", "preco": "R$ ***"},
    {"nome": "Produto 7", "preco": "R$ ***"},
    {"nome": "Produto 8", "preco": "R$ ***"},
    {"nome": "Produto 9", "preco": "R$ ***"},
]


# Rota Raiz
@app.route("/")
def rota_raiz():
    # criar uma variavel com o meu nome
    nome = "Pedro Victor"

    return render_template("alo.html", produtos=produtos, nome=nome), 200


# Nova Rota Teste
@app.route("/teste")
@app.route("/teste/<variavel>")
def rota_nova(variavel=""):
    return "Nova Rota teste<br>Variavél: {}".format(variavel), 200


# Rota formulário
@app.route("/form")
def rota_formulario():
    return render_template("form.html"), 200


# Rota tratamento do formulario
@app.route("/form_recebe", methods=["GET", "POST"])
def rota_form_recebe():
    nome = ""
    if request.method == "POST":
        nome = request.form["nome"]
        return "Nome: {}".format(nome), 200
    else:
        return "Não pode chamer direto no GET", 200


# Rota login
@app.route("/login")
def rota_login():
    return render_template("login.html"), 200


# Rota validar login
@app.route("/login_validar", methods=["POST"])
def rota_validar_login():
    if request.form["usuario"] == "pedro" and request.form["senha"] == "123456":
        session["usuario"] = request.form["usuario"]
        session["codigo"] = 1
        return redirect(url_for("rota_acesso_restrito"))
    else:
        return "Usuário/senha inválidos, digite novamente.", 200


# Rota para área restrita
@app.route("/restrito")
def rota_acesso_restrito():

    if session["codigo"] == 1:

        return "Bem-Vindo á area restrita!!<br>Usúario: {}<br>Código: {}" \
                   .format(session["usuario"], session["codigo"]), 200
    else:
        return "Acesso inválido", 200
