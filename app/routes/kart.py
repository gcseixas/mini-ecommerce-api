from fastapi import APIRouter, Depends, HTTPException
from app.dependencys import get_db
from sqlalchemy.orm import Session
from app.schemas.kart import CarrinhoItemCreate, CarrinhoItemResponse, CarrinhoResponse
from app.models.produto import Produto
from app.models.user import Usuario
from app.core.security import get_current_user

kart_router = APIRouter(prefix='/kart', tags=['kart'], dependencies=[Depends(get_current_user)])

@kart_router.post('/create-kart')
async def create_kart(
    dados: CarrinhoItemCreate, 
    db: Session = Depends(get_db),
    usuario: Usuario = Depends(get_current_user)
    ):
    
    # if usuario.admin is False: # type: ignore
    #     raise HTTPException(status_code=400, detail='Você não possui permissão para adicionar produto')
    
    # else:    
        
    #     product = Produto(
    #         nome=dados.nome,
    #         descricao=dados.descricao,
    #         preco=dados.preco,
    #         estoque=dados.estoque,
    #         user_id=usuario.id
    #     )
        
    # db.add(product)
    # db.commit()
    
    return{
        'msg': ''
    }
