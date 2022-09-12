from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///teste.db', echo=True)
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()


class Pessoa(Base):
    __tablename__ = 'pessoas'

    id = Column(Integer, primary_key=True)
    nome = Column(String)


Base.metadata.create_all(engine)

p1 = Pessoa(nome='Pedro')
p2 = Pessoa(nome='Victor')
p3 = Pessoa(nome='Fernandes')
p4 = Pessoa(nome='Ferreira')

session.add_all([p1, p2, p3, p4])

# Persiste tudo que estão na sessão
session.commit()

# Limpa a sessão
#session.flush()