from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from dependencys import get_db
from models import Usuario
from security import gerar_hash_senha, verificar_senha
from schemas import UserCreate, UserLogin


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


# TODO criar lógica de token

@auth_router.post('/login')
async def login(dados: UserLogin, db: Session = Depends(get_db)):
    
    usuario = db.query(Usuario).filter(Usuario.email == dados.email).first() # type: ignore
    
    if not usuario:
        raise HTTPException(status_code=400, detail='Usuário não encontrado')
    
    if not verificar_senha(dados.senha, str(usuario.senha)):
        raise HTTPException(status_code=401, detail='Senha inválida')
    
    return {'msg': 'Login feito com sucesso'}

    

# TODO criar lógica de validação do token

# TODO fazer com que as demais rotas usem o token no header