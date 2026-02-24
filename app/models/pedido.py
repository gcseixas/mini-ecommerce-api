from sqlalchemy import Column, Integer, ForeignKey, String, DateTime, Float
from sqlalchemy.orm import relationship
from datetime import datetime
from app.database import Base


class Pedido(Base):
    __tablename__ = "pedidos"

    id = Column(Integer, primary_key=True, index=True)

    usuario_id = Column(Integer, ForeignKey("usuarios.id"), nullable=False)

    status = Column(String, default="pendente", nullable=False)

    valor_total = Column(Float, nullable=False)

    data_criacao = Column(DateTime, default=datetime.utcnow)

    # Relacionamento com usuário
    usuario = relationship("Usuario", back_populates="pedidos")

    # Relacionamento com itens
    itens = relationship("ItemPedido", back_populates="pedido", cascade="all, delete")