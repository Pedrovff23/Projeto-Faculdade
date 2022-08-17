from flask import Flask, render_template

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
def rota_nova(variavel = ""):
    return "Nova Rota teste<br>Variavél: {}".format(variavel), 200
