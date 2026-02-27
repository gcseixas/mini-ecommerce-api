from pydantic import BaseModel
from typing import List

class CarrinhoItemCreate(BaseModel):
    produto_id: int
    quantidade: int
    
    class Config:
        from_attributes = True
    
