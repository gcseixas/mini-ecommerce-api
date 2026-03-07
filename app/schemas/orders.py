from pydantic import BaseModel

class PedidoCreate(BaseModel):
    ids_itens_carrinho: list[int]
    
    
    class Config:
        from_attributes = True
        