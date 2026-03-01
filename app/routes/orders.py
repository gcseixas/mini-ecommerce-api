
from fastapi import APIRouter, Depends, HTTPException
from app.dependencys import get_db
from sqlalchemy.orm import Session
from app.schemas.kart import CarrinhoItemCreate
from app.models.user import Usuario
from app.models.kart import ItensCarrinho
from app.core.security import get_current_user


#TODO Criar rota para fazer insert no itensPedido

order_router = APIRouter(prefix='/order', tags=['order'], dependencies=[Depends(get_current_user)])

@order_router.post('/create-item-order')
async def create_item_order(
    dados: CarrinhoItemCreate, 
    db: Session = Depends(get_db),
    usuario: Usuario = Depends(get_current_user)
    ):
    
    pass


#TODO Criar rota para fazer edição no status do pedido

#TODO Criar rota para fazer visualização de um pedido e seus itens

#TODO Criar rota para fazer visualização todos os pedidos

