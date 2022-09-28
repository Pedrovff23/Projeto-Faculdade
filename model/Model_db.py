from Flask_sqlalchemy import db


class Pessoa(db.Model):
    id = db.Column('id', db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column('nome', db.String(500))
    email = db.Column('email', db.String(500))
    telefone = db.Column('telefone', db.String(500))

    def __repr__(self):
        return f'Pessoa(id = {self.id}, nome = {self.nome}, email = {self.email}, telefone = {self.telefone})'
