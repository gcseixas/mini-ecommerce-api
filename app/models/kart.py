from sqlalchemy import Column, Integer, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from app.database import Base

class Carrinho(Base):
    __tablename__ = "carrinhos"

    id = Column(Integer, primary_key=True, index=True)

    usuario_id = Column(Integer, ForeignKey("usuarios.id"), nullable=False)
    
    produto_id = Column(Integer, ForeignKey("produtos.id"), nullable=False)
    
    quantidade = Column("quantidade", Integer)

    criado_em = Column(DateTime, default=datetime.utcnow)
    

    # Relacionamentos
    usuario = relationship("Usuario", back_populates="carrinho")
    
    produto = relationship("Produto", back_populates='carrinho')
    
    
 
    

