from pydantic import BaseModel

class PedidoCreate(BaseModel):
    ids_itens_carrinho: list[int]
    
    
    class Config:
        from_attributes = True
        
class PedidoCompletoResponse(BaseModel):
    id: int
    valor: float
    status: str
    itens: list[PedidoItensResponse]
    
    class Config:
        from_attributes = True
        
        
class PedidoItensResponse(BaseModel):
    nome: str
    preco_unitario: float
    produto: ProdutoResumo
    valor_item: float
    
    class Config:
        from_attributes = True


class ProdutoResumo(BaseModel):
    nome: str

    class Config:
        from_attributes = True