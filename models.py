from sqlalchemy import create_engine, Column, String, Integer, Boolean, Float, ForeignKey
from sqlalchemy.orm import declarative_base, relationship
from database import Base

class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    nome = Column("nome", String)
    email = Column("email", String, nullable=False)
    senha = Column("senha", String)
    ativo = Column("ativo", Boolean)

    def __init__(self, nome, email, senha, ativo=True, admin=False):
        self.nome = nome
        self.email = email
        self.senha = senha
        self.ativo = ativo
        
        

## Criar pedido

## Itens pedido

## Item estoque


###--------------------------------------------------------------------####
# executa a criação dos metadados do seu banco (cria efetivamente o banco de dados)


# migrar o banco de dados

# criar a migração: alembic revision --autogenerate -m "mensagem"
# executar a migração: alembic upgrade head