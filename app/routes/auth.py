from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.dependencys import get_db
from app.models.user import Usuario
from app.core.security import gerar_hash_senha, verificar_senha, criar_token, get_current_user
from app.schemas.user import UserCreate, UserLogin


auth_router = APIRouter(prefix='/auth', tags=['auth'])

# ROTA DE INSERÇÃO
@auth_router.post("/create_user")
async def create_user(dados: UserCreate , db: Session = Depends(get_db)):
    
    usuario = db.query(Usuario).filter(Usuario.email == dados.email).first() # type: ignore
    
    if usuario:
        raise HTTPException(status_code=400, detail='Email de usuário já cadadastro')
    
    senha_crip = gerar_hash_senha(dados.senha)

    user = Usuario(
        nome=dados.nome,
        email=dados.email,
        senha=senha_crip,
        ativo= True
    )
    
    db.add(user)
    db.commit()
    return {'mensagem': f'Usuario cadastro com sucesso para o email - {user.email}'}


@auth_router.post('/login')
async def login(dados: UserLogin, db: Session = Depends(get_db)):
    
    usuario = db.query(Usuario).filter(Usuario.email == dados.email).first() # type: ignore
    
    if not usuario:
        raise HTTPException(status_code=400, detail='Usuário não encontrado')
    
    if not verificar_senha(dados.senha, str(usuario.senha)):
        raise HTTPException(status_code=401, detail='Senha inválida')
    
    token = criar_token({'sub': usuario.email})
    
    return {
        "access_token": token,
        "token_type": "bearer"
        }

@auth_router.get('/me')
async def dados_usuario_atual(
    usuario: Usuario = Depends(get_current_user)
):
    return {
        "id": usuario.id,
        "email": usuario.email
    }

