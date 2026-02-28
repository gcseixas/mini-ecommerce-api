from sqlalchemy import Column, String, Integer, Boolean, DateTime
from sqlalchemy.sql import func
from app.database import Base
from sqlalchemy.orm import relationship


class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    nome = Column("nome", String, nullable=False)
    email = Column("email", String, nullable=False)
    senha = Column("senha", String, nullable=False)
    ativo = Column("ativo", Boolean, nullable=False)
    admin = Column("admin", Boolean, nullable=False)
    criado = Column(
        DateTime,
        server_default=func.now(),  # banco gera automaticamente
        nullable=False
    )
    
    pedidos = relationship(
    "Pedido",
    back_populates="usuario",
    cascade="all, delete"
    )
    
    produtos = relationship("Produto", back_populates="owner")
    
    itens_carrinho = relationship(
        "ItensCarrinho",
        back_populates="usuario",
        cascade="all, delete-orphan"
    )

    def __init__(self, nome, email, senha, ativo=True, admin=False):
        self.nome = nome
        self.email = email
        self.senha = senha
        self.ativo = ativo
        self.admin = admin
        
                

###--------------------------------------------------------------------####
# executa a criação dos metadados do seu banco (cria efetivamente o banco de dados)


# migrar o banco de dados

# criar a migração: alembic revision --autogenerate -m "Correcao nome de tabela carrinho"
# executar a migração: alembic upgrade head