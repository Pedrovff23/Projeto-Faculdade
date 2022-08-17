from flask import Flask, render_template, request

app = Flask(__name__)

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

