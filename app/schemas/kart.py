from pydantic import BaseModel
from typing import List

class CarrinhoItemCreate(BaseModel):
    produto_id: int
    quantidade: int
    
    
class CarrinhoItemResponse(BaseModel):
    id: int
    produto_id: int
    quantidade: int

    class Config:
        orm_mode = True
        
        
class CarrinhoResponse(BaseModel):
    id: int
    usuario_id: int
    itens: List[CarrinhoItemResponse]

    class Config:
        orm_mode = True