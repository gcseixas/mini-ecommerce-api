from sqlalchemy import Column, Integer, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from app.database import Base

class ItensCarrinho(Base):
    __tablename__ = "itensCarrinho"

    id = Column(Integer, primary_key=True, index=True)

    usuario_id = Column(Integer, ForeignKey("usuarios.id"), nullable=False)
    
    produto_id = Column(Integer, ForeignKey("produtos.id"), nullable=False)
    
    quantidade = Column("quantidade", Integer)

    criado_em = Column(DateTime, default=datetime.utcnow)
    

    # Relacionamentos
    usuario = relationship("Usuario", back_populates="itens_carrinho")
    
    produto = relationship("Produto", back_populates='carrinho')
    
    
 
    

