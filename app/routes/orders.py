from fastapi import APIRouter, Depends, HTTPException
from app.dependencys import get_db
from sqlalchemy.orm import Session
from app.models.user import Usuario
from app.models.kart import ItensCarrinho
from app.models.pedido import Pedido
from app.models.item_pedido import ItemPedido
from app.schemas.orders import PedidoCreate, PedidoCompletoResponse, PedidoResponse
from app.core.security import get_current_user


order_router = APIRouter(prefix='/order', tags=['order'], dependencies=[Depends(get_current_user)])

@order_router.post('/create-pedido')
async def create_pedido(
    dados: PedidoCreate, 
    db: Session = Depends(get_db),
    usuario: Usuario = Depends(get_current_user)
    ):
    
    """
    Nesta rota, estamos criando o pedido, transportando do carrinho para o itens pedido e após isso, limpando o carrinho, de acordo com o id
    """
    
    ids_item_carrinho = {item.id for item in usuario.itens_carrinho}
    
    user_items_exist = set(dados.ids_itens_carrinho).issubset(ids_item_carrinho)
    
    if not user_items_exist:
        raise HTTPException(status_code=404, detail='Um dos itens no carrinho inexistente ou não pertence ao usuário')
            
    itens_carrinho = db.query(ItensCarrinho).filter(ItensCarrinho.id.in_(dados.ids_itens_carrinho)).all()
        
    pedido = Pedido(
        usuario_id = usuario.id,
        status = 'pendente',
        valor_total = 0
    )
    
    db.add(pedido)
    db.flush()
    
    valor_pedido = 0
    
    for item in itens_carrinho:
        item_pedido = ItemPedido(
            pedido_id = pedido.id,
            produto_id = item.produto_id,
            quantidade = item.quantidade,
            preco_unitario = item.produto.preco
        )
        
        valor_pedido += item.quantidade * item.produto.preco
        
        db.add(item_pedido)
        db.flush()
        
    pedido.valor_total = valor_pedido # type: ignore
    
    for item in itens_carrinho:
        db.delete(item)
        
    id_pedido = pedido.id
    
    db.commit()    
    
    return{
        
        'msg': f'Pedido nº{id_pedido} criado com sucesso'
    }


@order_router.put('/concluir-pedido/{id_pedido}')
async def concluir_pedido(
    id_pedido: int, 
    db: Session = Depends(get_db),
    usuario: Usuario = Depends(get_current_user)
    ):
    
    pedido = db.query(Pedido).filter(Pedido.id == id_pedido).first()
    
    if not pedido:
        raise HTTPException(status_code=404, detail='Pedido não encontrado')
    
    if pedido.usuario_id != usuario.id: # type: ignore
        raise HTTPException(status_code=403, detail='Pedido não pertence ao usuário')
    
    if pedido.status == 'concluido' or pedido.status == 'cancelado':  # type: ignore
        raise HTTPException(status_code=400, detail=f'Não é possível concluir um pedido com status de {pedido.status}')
    
    pedido_id = pedido.id
    
    pedido.status = 'concluido'  # type: ignore
    
    db.commit()
    
    return{
        'msg': f'Pedido nº{pedido_id} concluído com sucesso'
    }   


@order_router.put('/cancelar-pedido/{id_pedido}')
async def cancelar_pedido(
    id_pedido: int, 
    db: Session = Depends(get_db),
    usuario: Usuario = Depends(get_current_user)
    ):

    pedido = db.query(Pedido).filter(Pedido.id == id_pedido).first()
    
    if not pedido:
        raise HTTPException(status_code=404, detail='Pedido não encontrado')
    
    if pedido.usuario_id != usuario.id: # type: ignore
        raise HTTPException(status_code=403, detail='Pedido não pertence ao usuário')
    
    if pedido.status == 'concluido' or pedido.status == 'cancelado':  # type: ignore
        raise HTTPException(status_code=403, detail=f'Não é possível cancelar um pedido com status de {pedido.status}')
    
    pedido_id = pedido.id
    
    pedido.status = 'cancelado'  # type: ignore
    
    db.commit()
    
    return{
        'msg': f'Pedido nº{pedido_id} cancelado com sucesso'
    }  


@order_router.get('/visualizar-pedido-itens/{id_pedido}', response_model=PedidoCompletoResponse)
async def visualizar_pedido_itens(
    id_pedido: int, 
    db: Session = Depends(get_db),
    usuario: Usuario = Depends(get_current_user)
    ):
    
    pedido = db.query(Pedido).filter(Pedido.id == id_pedido).first()
    
    if not pedido:
        raise HTTPException(status_code=404, detail='Pedido não encontrado')
    
    if pedido.usuario_id != usuario.id: # type: ignore
        raise HTTPException(status_code=403, detail='Pedido não pertence ao usuário')
    
    return pedido


@order_router.get('/visualizar-pedidos', response_model=list[PedidoResponse])
async def visualizar_pedidos(
    db: Session = Depends(get_db),
    usuario: Usuario = Depends(get_current_user)
    ):
    
    pedidos = db.query(Pedido).filter(Pedido.usuario_id == usuario.id).all()
    
    if not pedidos:
        raise HTTPException(status_code=404, detail='Usuário não possui pedidos')
    
    return pedidos



