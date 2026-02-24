from fastapi import APIRouter, Depends, HTTPException
from app.dependencys import get_db
from sqlalchemy.orm import Session
from app.schemas.produto import CreateProduct, ProdutoResponse
from app.models.produto import Produto
from app.models.user import Usuario
from app.core.security import get_current_user

product_router = APIRouter(prefix='/product', tags=['product'], dependencies=[Depends(get_current_user)])

#TODO Fazer com que o usuário seja armazenado na tabela

@product_router.post('/create-product')
async def create_product(
    dados: CreateProduct, 
    db: Session = Depends(get_db),
    usuario: Usuario = Depends(get_current_user)
    ):
    
    if usuario.admin is False: # type: ignore
        raise HTTPException(status_code=400, detail='Você não possui permissão para adicionar produto')
    
    else:    
        
        product = Produto(
            nome=dados.nome,
            descricao=dados.descricao,
            preco=dados.preco,
            estoque=dados.estoque,
            user_id=usuario.id
        )
        
    db.add(product)
    db.commit()
    
    return{
        'msg': f'{product.nome} criado com sucesso pelo {usuario.nome}'
    }



@product_router.get('/list-products', response_model=list[ProdutoResponse])
async def list_products(
     db: Session = Depends(get_db),
):
    produtos = db.query(Produto).all()
    return produtos


@product_router.get('/list-product/{id}', response_model=ProdutoResponse)
async def list_product(
     id: int,
     db: Session = Depends(get_db)
):
    produto = db.query(Produto).filter(Produto.id == id).first()
    
    if not produto:
        raise HTTPException(status_code=400, detail='Produto não encontrado')
    
    return produto


#TODO Criar edição

#TODO Criar deletar