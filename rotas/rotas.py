from flask import Blueprint, render_template, request, session, redirect, url_for
from Flask_sqlalchemy import db
from model.Model_db import Pessoa

rotas_blueprint = Blueprint('rotas', __name__, template_folder='templates')


# Rota raiz
@rotas_blueprint.route("/")
def rota_raiz():
    db.create_all()
    pessoas_cadastradas = Pessoa.query.all()

    return render_template("index.html", pessoas=pessoas_cadastradas), 200


# Rota formulário pessoa
@rotas_blueprint.route("/adicionar", methods=["GET", "POST"])
def rota_formulario():
    if request.method == "POST":
        return render_template("add.html"), 200
    else:
        return "Vá até o index ('/') e click em cadastar pessoa", 200


# Rota pegar os dados do formulário
@rotas_blueprint.route("/validar", methods=["GET", "POST"])
def rota_adicionar_pessoa():
    if request.method == "POST":
        session["nome"] = request.form["nome"]
        session["telefone"] = request.form["telefone"]
        session["email"] = request.form["email"]
        return redirect(url_for(".rota_validar_dados"))
    else:
        return "ERRO, Vá até o index ('/') e click em cadastar pessoa novamente", 200


# Rota validar e inserir no banco de dados
@rotas_blueprint.route("/restrito")
def rota_validar_dados():
    p1 = Pessoa(nome=session["nome"], email=session["email"], telefone=session["telefone"])
    db.session.add(p1)
    db.session.commit()
    return redirect(url_for(".rota_raiz"))


# Rota excluir pessoa no banco de dados
@rotas_blueprint.route("/deletar/<int:id>", methods=["GET"])
def deletar_pessoa(id):

    if request.method == "GET":
        pessoa_deletar = Pessoa.query.get(id)
        db.session.delete(pessoa_deletar)
        db.session.commit()
        return redirect(url_for(".rota_raiz"))


# Rota alterar pessoa no banco de dados
@rotas_blueprint.route("/alterar/<int:id>", methods=["POST", "GET"])
def alterar_pessoa(id):
    pessoa = Pessoa.query.get(id)
    if request.method == 'GET':
        return render_template("edit.html", pessoa_edit=pessoa), 200
    else:
        pessoa.nome = request.form["nome"]
        pessoa.email = request.form["email"]
        pessoa.telefone = request.form["telefone"]
        db.session.commit()
        return redirect(url_for(".rota_raiz"))
