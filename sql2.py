from pprint import pprint

from sqlalchemy import create_engine, Column, String, Integer,ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

engine = create_engine('sqlite:///teste2.db', echo=True)
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()


class Produto(Base):

    __tablename__ = 'produtos'

    id = Column(Integer, primary_key=True)
    nome = Column(String)
    pessoa_id = Column(Integer, ForeignKey('pessoas.id'))
    pessoa = relationship('Pessoa')

    def __repr__(self):
        return f'Produto( nome={self.nome}, pessoa={self.pessoa} )'


class Pessoa(Base):
    __tablename__ = 'pessoas'

    id = Column(Integer, primary_key=True)
    nome = Column(String)
    idade = Column(Integer)
    produtos = relationship(Produto, backref='pessoas')

    def __repr__(self):
        return f'Pessoa( id={self.id}, nome={self.nome}, idade={self.idade})'


Base.metadata.create_all(engine)

p1 = Pessoa(nome='Pedro', idade=23)
pd1 = Produto(nome='PS5', pessoa=p1)
pd2 = Produto(nome='Livro', pessoa=p1)

session.add_all([pd1, pd2, p1])

session.commit()

pprint(session.query(Pessoa).all())