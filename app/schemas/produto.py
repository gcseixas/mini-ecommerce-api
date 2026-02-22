from pydantic import BaseModel

class CreateProduct(BaseModel):
    nome: str
    descricao: str
    preco: float
    estoque: int
    ativo: bool
    