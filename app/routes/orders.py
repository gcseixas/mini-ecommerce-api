from fastapi import APIRouter, Depends, HTTPException
from app.dependencys import get_db
from sqlalchemy.orm import Session
from app.models.user import Usuario
from app.models.kart import ItensCarrinho
from app.models.pedido import Pedido
from app.schemas.orders import PedidoCreate
from app.core.security import get_current_user


#TODO Criar rota para fazer insert no itensPedido

order_router = APIRouter(prefix='/order', tags=['order'], dependencies=[Depends(get_current_user)])

@order_router.post('/create-pedido')
async def create_pedido(
    dados: PedidoCreate, 
    db: Session = Depends(get_db),
    usuario: Usuario = Depends(get_current_user)
    ):
    
    itens_carrinho = db.query(ItensCarrinho).filter(ItensCarrinho.id.in_(dados.ids_itens_carrinho)).all()
        
    pedido = Pedido(
        usuario_id = usuario.id,
        status = 'pendente',
        valor_total = 0
    )
    
    db.add(pedido)
    db.flush()

    

    return{
        
        'msg': 'Testando'
    }



#TODO Criar rota para fazer edição no status do pedido

#TODO Criar rota para fazer visualização de um pedido e seus itens

#TODO Criar rota para fazer visualização todos os pedidos

