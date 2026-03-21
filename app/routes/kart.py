from fastapi import APIRouter, Depends, HTTPException
from app.dependencys import get_db
from sqlalchemy.orm import Session
from app.schemas.kart import CarrinhoItemCreate, Updatekart
from app.models.user import Usuario
from app.models.kart import ItensCarrinho
from app.models.produto import Produto
from app.services.base_service import BaseService
from app.core.security import get_current_user

kart_router = APIRouter(prefix='/kart', tags=['kart'], dependencies=[Depends(get_current_user)])


@kart_router.post('/create-item-kart')
async def create_item_kart(
    dados: CarrinhoItemCreate, 
    db: Session = Depends(get_db),
    usuario: Usuario = Depends(get_current_user)
    ):

    produto = db.query(Produto).filter(Produto.id == dados.produto_id).first()
    
    if not produto:
        raise HTTPException(status_code=404, detail='Produto não encontrado')

    if not produto.ativo: # type: ignore
        raise HTTPException(status_code=403, detail='Produto inativo no momento')
        
    item_carrinho = ItensCarrinho(
        usuario_id=usuario.id,
        produto_id=dados.produto_id,
        quantidade=dados.quantidade
    )

    db.add(item_carrinho)
    db.commit()
    
    return{
        'msg': 'Item criado com sucesso'
    }



@kart_router.put('/edit-item-kart/{id_item_kart}')
async def edit_item_kart(
    id_item_kart: int,
    dados: Updatekart,
    db: Session = Depends(get_db),
    usuario: Usuario = Depends(get_current_user)
    ):
    
        
    item = db.query(ItensCarrinho).filter(ItensCarrinho.id == id_item_kart).first()
    
    produto = BaseService.buscar_por_id(db, Produto, dados.produto_id)
    
    if not item:
        raise HTTPException(status_code=404, detail='Item no carrinho inextistente')
    
    if usuario.id != item.usuario_id: # type: ignore
        raise HTTPException(status_code=403, detail='Item no carrinho, não pertence ao usuário')
    
    if not produto or not produto.ativo:
        raise HTTPException(status_code=404, detail='O produto não existe ou está indisponível')
        
    item_atualizar = BaseService.atualizar_campos(item, dados)

    db.commit()
    db.refresh(item_atualizar)    
    
    return {
        'msg': 'item editado com sucesso'
    }

@kart_router.get('/list-item-kart/{id_item_kart}')
async def list_item_carrinho(
    id_item_kart: int,
    db: Session = Depends(get_db),
    usuario: Usuario = Depends(get_current_user)
    ):
    
    item = db.query(ItensCarrinho).filter(ItensCarrinho.id == id_item_kart).first()

    if usuario.id != item.usuario_id: # type: ignore
        raise HTTPException(status_code=403, detail='Item no carrinho, não pertence ao usuário')
    
    
    if not item:
        raise HTTPException(status_code=404, detail='Item no carrinho inextistente')
    
    return {
        'Item': item.produto.nome,
        'Quantidade': item.quantidade,
        'Valor': item.quantidade * item.produto.preco
    }


@kart_router.get('/list-items-kart')
async def list_items_carrinho(
    db: Session = Depends(get_db),
    usuario: Usuario = Depends(get_current_user)
    ):
    
    items = db.query(ItensCarrinho).filter(ItensCarrinho.usuario_id == usuario.id).all()
    
    response = []
    
    valor_total = 0
    
    for item in items:
        response.append({
            "id": item.id,
            "item": item.produto.nome,
            "quantidade": item.quantidade,
            "valor_unitario": item.produto.preco,
            "total": item.quantidade * item.produto.preco
        })
        
        valor_total += item.quantidade * item.produto.preco
    
    return {
        'Valor carrinho': valor_total,
        'Itens':response
        }


@kart_router.delete('/remove-item-kart/{id_item_kart}')
async def remove_item_carrinho(
    id_item_kart: int,
    db: Session = Depends(get_db),
    usuario: Usuario = Depends(get_current_user)
    ):
    
    item = db.query(ItensCarrinho).filter(ItensCarrinho.id == id_item_kart).first()

    if not item:
        raise HTTPException(status_code=404, detail='Item no carrinho inextistente')
    
    if usuario.id != item.usuario_id: # type: ignore
        raise HTTPException(status_code=403, detail='Item no carrinho, não pertence ao usuário')
    
    nome_item = item.produto.nome
    
    
    BaseService.deletar(db, item)
    
    return {
        'msg': f'{nome_item} removido com sucesso do seu carrinho'
    }


@kart_router.delete('/empty-items-kart')
async def empty_items_carrinho(
    db: Session = Depends(get_db),
    usuario: Usuario = Depends(get_current_user)
    ):
    
    items = db.query(ItensCarrinho).filter(ItensCarrinho.usuario_id == usuario.id).all()
    
    if not items:
        raise HTTPException(status_code=404, detail='Carrinho já está vazio')
        
    for item in items:
        BaseService.deletar(db, item)
         
    return {
        'Msg': 'Carrinho limpo com sucesso'
        }

