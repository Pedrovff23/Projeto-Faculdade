from flask import Blueprint, render_template, request, session, redirect, url_for
from Flask_sqlalchemy import db
from model.Model_db import Produto

rotas_blueprint = Blueprint('Rotas', __name__, template_folder='templates')


# Rota Raiz
@rotas_blueprint.route("/")
def rota_raiz():

    db.create_all()
    pd1 = Produto(nome="Bernado", preco="1.0")
    db.session.add(pd1)
    db.session.commit()

    produtos = Produto.query.all()

    # criar uma variavel com o meu nome
    nome = "Pedro Victor"
    return render_template("alo.html", produtos=produtos, nome=nome), 200


# Nova Rota Teste
@rotas_blueprint.route("/teste")
@rotas_blueprint.route("/teste/<variavel>")
def rota_nova(variavel=""):
    return "Nova Rota teste<br>Variavél: {}".format(variavel), 200


# Rota formulário
@rotas_blueprint.route("/form")
def rota_formulario():
    return render_template("form.html"), 200


# Rota tratamento do formulario
@rotas_blueprint.route("/form_recebe", methods=["GET", "POST"])
def rota_form_recebe():
    nome = ""
    if request.method == "POST":
        nome = request.form["nome"]
        return "Nome: {}".format(nome), 200
    else:
        return "Não pode chamer direto no GET", 200


# Rota login
@rotas_blueprint.route("/login")
def rota_login():
    return render_template("login.html"), 200


# Rota validar login
@rotas_blueprint.route("/login_validar", methods=["POST"])
def rota_validar_login():
    if request.form["usuario"] == "pedro" and request.form["senha"] == "123456":
        session["usuario"] = request.form["usuario"]
        session["codigo"] = 1
        return redirect(url_for("rota_acesso_restrito"))
    else:
        return "Usuário/senha inválidos, digite novamente.", 200


# Rota para área restrita
@rotas_blueprint.route("/restrito")
def rota_acesso_restrito():
    if session["codigo"] == 1:

        return "Bem-Vindo á area restrita!!<br>Usúario: {}<br>Código: {}" \
                   .format(session["usuario"], session["codigo"]), 200
    else:
        return "Acesso inválido", 200