from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from dependencys import get_db
from main import app
from models import Usuario

auth_router = APIRouter(prefix='/auth', tags=['auth'])


# ROTA DE INSERÇÃO
@auth_router.post("/create_user")
def create_user(nome, email, senha, db: Session = Depends(get_db)):
    
    user = Usuario(
        nome=nome,
        email=email,
        senha=senha,
        ativo= True
    )
    
    db.add(user)
    db.commit()
    return {'mensagem': 'Testando'}
