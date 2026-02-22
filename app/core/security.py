import hashlib
from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends, HTTPException
from passlib.context import CryptContext
from jose import jwt, JWTError
from datetime import datetime, timedelta
from sqlalchemy.orm import Session
from app.dependencys import get_db
from app.main import SECRET_KEY, ALGORITHM
from app.models.user import Usuario

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

# Define o algoritmo que será usado
pwd_context = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto"
)

def _pre_hash_senha(senha: str) -> str:
    """
    Aplica SHA-256 antes do bcrypt para evitar limite de 72 bytes.
    """
    return hashlib.sha256(senha.encode("utf-8")).hexdigest()

def gerar_hash_senha(senha: str) -> str:
    senha_processada = _pre_hash_senha(senha)
    return pwd_context.hash(senha_processada)

def verificar_senha(senha_digitada: str, senha_hash: str) -> bool:
    senha_processada = _pre_hash_senha(senha_digitada)
    return pwd_context.verify(senha_processada, senha_hash)

def criar_token(dados: dict):
    dados_copia = dados.copy()
    expira = datetime.utcnow() + timedelta(minutes=30)
    dados_copia.update({"exp": expira})
    return jwt.encode(dados_copia, str(SECRET_KEY), algorithm=str(ALGORITHM))


def get_current_user(
    token: str = Depends(oauth2_scheme),
    db: Session = Depends(get_db)
):

    try:
        payload = jwt.decode(token, str(SECRET_KEY), algorithms=str([ALGORITHM]))
        email: str = payload.get("sub") # type: ignore

        if email is None:
            raise HTTPException(status_code=401, detail="Token inválido")

    except JWTError:
        raise HTTPException(status_code=401, detail="Token inválido")

    usuario = db.query(Usuario).filter(Usuario.email == email).first() # type: ignore

    if usuario is None:
        raise HTTPException(status_code=401, detail="Usuário não encontrado")

    return usuario

