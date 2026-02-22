from fastapi import APIRouter, Depends, HTTPException
from app.dependencys import get_db
from sqlalchemy.orm import Session
from app.schemas.produto import CreateProduct
from app.models.produto import Produto
from app.models.user import Usuario
from app.core.security import get_current_user

product_router = APIRouter(prefix='/product', tags=['product'])

#TODO Fazer com que o usuário seja armazenado na tabela

@product_router.post('/create-product')
async def create_product(
    dados: CreateProduct, 
    db: Session = Depends(get_db),
    usuario: Usuario = Depends(get_current_user)
    ):
    
    product = Produto(
        nome=dados.nome,
        descricao=dados.descricao,
        preco=dados.preco,
        estoque=dados.estoque, 
    )
    
    db.add(product)
    db.commit()
    
    return{
        'msg': f'{product.nome} criado com sucesso pelo {usuario.nome}'
    }

