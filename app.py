from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def ola_mundo():
    # criar uma variavel com o meu nome
    nome = "Pedro Victor"
    produtos = [
        {"nome": "Ração", "preco": 199.99},
        {"nome": "Playstation", "preco": 5000}]
    return render_template("alo.html", produtos=produtos, nome=nome), 200

