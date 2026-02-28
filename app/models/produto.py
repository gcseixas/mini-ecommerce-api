from sqlalchemy import Column, String, Integer, Boolean, DateTime, Float, Integer, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base
from sqlalchemy.sql import func


class Produto(Base):
    __tablename__ = 'produtos'
    
    id = Column("id", Integer, primary_key=True, autoincrement=True)
    nome = Column("nome", String, nullable=False)
    descricao = Column("descricao", String)
    preco = Column("preco", Float, nullable=False)
    estoque = Column("estoque", Integer)
    ativo = Column("ativo", Boolean, nullable=False)
    user_id = Column(Integer, ForeignKey("usuarios.id"), nullable=False)

    owner = relationship("Usuario", back_populates="produtos")
    
    carrinho = relationship("ItensCarrinho", back_populates='produto')
    
    data_criacao = Column(
        DateTime,
        server_default=func.now(), 
        nullable=False
    )
    
    def __init__(self, nome, descricao, preco, estoque=0, ativo=True, user_id=None):
        self.nome = nome
        self.descricao = descricao
        self.preco = preco
        self.estoque = estoque
        self.ativo = ativo
        self.user_id = user_id