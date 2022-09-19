from flask import Flask
from rotas import rotas_blueprint
from Flask_sqlalchemy import db


app = Flask(__name__)

# Criando uma chave de criptografia para o cookie
app.secret_key = "c!ds@%kc*&%nds@dsa{wd"

# Apontar para um banco de dados
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Produto.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

# Rotas Blueprint
app.register_blueprint(rotas_blueprint)


