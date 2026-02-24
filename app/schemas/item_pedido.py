from pydantic import BaseModel


class ItemPedidoCreate(BaseModel):
    produto_id: int
    quantidade: int


class ItemPedidoResponse(BaseModel):
    id: int
    produto_id: int
    quantidade: int
    preco_unitario: float

    class Config:
        from_attributes = True