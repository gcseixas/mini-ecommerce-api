import hashlib
from passlib.context import CryptContext


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