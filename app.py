from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def ola_mundo():
    # criar uma variavel com o meu nome
    nome = "Pedro Victor"

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

    return render_template("alo.html", produtos=produtos, nome=nome), 200
