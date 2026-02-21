from pydantic import BaseModel, EmailStr, Field
from typing import Annotated

class UserCreate(BaseModel):
    nome: Annotated[str, Field(min_length=3, max_length=100)]
    email: EmailStr
    senha: Annotated[str, Field(min_length=6, max_length=128)]
    
    
class UserLogin(BaseModel):
    email: str
    senha: str

