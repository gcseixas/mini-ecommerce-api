from pydantic import BaseModel
from datetime import datetime
from typing import List
from .item_pedido import ItemPedidoResponse, ItemPedidoCreate


class PedidoCreate(BaseModel):
    itens: List[ItemPedidoCreate]


class PedidoResponse(BaseModel):
    id: int
    usuario_id: int
    status: str
    valor_total: float
    data_criacao: datetime
    itens: List[ItemPedidoResponse]

    class Config:
        from_attributes = True