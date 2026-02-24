from sqlalchemy import Column, Integer, ForeignKey, Float
from sqlalchemy.orm import relationship
from app.database import Base


class ItemPedido(Base):
    __tablename__ = "itens_pedido"

    id = Column(Integer, primary_key=True, index=True)

    pedido_id = Column(Integer, ForeignKey("pedidos.id"), nullable=False)

    produto_id = Column(Integer, ForeignKey("produtos.id"), nullable=False)

    quantidade = Column(Integer, nullable=False)

    preco_unitario = Column(Float, nullable=False)

    # Relacionamentos
    pedido = relationship("Pedido", back_populates="itens")
    produto = relationship("Produto")