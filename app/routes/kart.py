from fastapi import APIRouter, Depends, HTTPException
from app.dependencys import get_db
from sqlalchemy.orm import Session
from app.schemas.kart import CarrinhoItemCreate
from app.models.user import Usuario
from app.models.kart import Carrinho
from app.core.security import get_current_user

kart_router = APIRouter(prefix='/kart', tags=['kart'], dependencies=[Depends(get_current_user)])


#TODO Criar rota para fazer insert no carrinho
@kart_router.post('/create-item-kart')
async def create_item_kart(
    dados: CarrinhoItemCreate, 
    db: Session = Depends(get_db),
    usuario: Usuario = Depends(get_current_user)
    ):
#TODO verificar se o produto existe



#TODO verificar se o produto está ativo

#TODO Fazer cálculo de estoque

    item_carrinho = Carrinho(
        usuario_id=usuario.id,
        produto_id=dados.produto_id,
        quantidade=dados.quantidade
    )

    db.add(item_carrinho)
    db.commit()
    
    
    return{
        'msg': 'Item criado com sucesso'
    }


#TODO Criar rota para fazer edição de um item no carrinho

#TODO Criar rota para fazer visualização de um item no carrinho

#TODO Criar rota para fazer visualização dos itens de um usuário

#TODO Criar rota para remoção de item no carrinho

#TODO Criar rota para limpar o carrinho


