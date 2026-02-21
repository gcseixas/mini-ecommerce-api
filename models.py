from sqlalchemy import create_engine, Column, String, Integer, Boolean, Float, ForeignKey, DateTime
from sqlalchemy.sql import func
from sqlalchemy.orm import declarative_base, relationship
from database import Base

# ==============================
# MODEL: Usuario
# ==============================

# TODO Usuario
# - id (PK)
# - nome
# - email (unique)
# - senha_hash
# - ativo
# - data_criacao

class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    nome = Column("nome", String, nullable=False)
    email = Column("email", String, nullable=False)
    senha = Column("senha", String, nullable=False)
    ativo = Column("ativo", Boolean, nullable=False)
    criado = Column(
        DateTime,
        server_default=func.now(),  # banco gera automaticamente
        nullable=False
    )

    def __init__(self, nome, email, senha, ativo=True, admin=False):
        self.nome = nome
        self.email = email
        self.senha = senha
        self.ativo = ativo
                


# ==============================
# MODEL: Produto
# ==============================

# TODO Produto
# - id (PK)
# - nome
# - descricao
# - preco
# - estoque
# - ativo
# - data_criacao


# ==============================
# MODEL: Pedido
# ==============================

# TODO Pedido
# - id (PK)
# - usuario_id (FK -> Usuario.id)
# - status (pendente, pago, enviado, cancelado)
# - valor_total
# - data_criacao


# ==============================
# MODEL: ItemPedido
# ==============================

# TODO ItemPedido
# - id (PK)
# - pedido_id (FK -> Pedido.id)
# - produto_id (FK -> Produto.id)
# - quantidade
# - preco_unitario



###--------------------------------------------------------------------####
# executa a criação dos metadados do seu banco (cria efetivamente o banco de dados)


# migrar o banco de dados

# criar a migração: alembic revision --autogenerate -m "mensagem"
# executar a migração: alembic upgrade head