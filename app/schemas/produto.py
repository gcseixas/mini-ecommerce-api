from pydantic import BaseModel

class CreateProduct(BaseModel):
    nome: str
    descricao: str
    preco: float
    estoque: int
    ativo: bool
    

class ProdutoResponse(BaseModel):
    id: int
    nome: str
    preco: float

    class Config:
        from_attributes = True
    