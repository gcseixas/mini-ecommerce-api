from pydantic import BaseModel
from typing import Optional

class CarrinhoItemCreate(BaseModel):
    produto_id: int
    quantidade: int
    
    class Config:
        from_attributes = True
        
        
class Updatekart(BaseModel):
    produto_id: Optional[int] = None
    quantidade: Optional[int] = None    
    


    
