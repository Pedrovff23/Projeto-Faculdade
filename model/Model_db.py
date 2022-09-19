from Flask_sqlalchemy import db


class Produto(db.Model):
    id = db.Column('id', db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column('nome', db.String(500))
    preco = db.Column('preco', db.Float)

    def __repr__(self):
        return f'Produto(id = {self.id}, nome = {self.nome}, preco = {self.preco})'