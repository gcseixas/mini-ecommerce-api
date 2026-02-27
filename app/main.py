from fastapi import FastAPI, Depends
from dotenv import load_dotenv
import os

load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")

app = FastAPI()


from app.routes import auth_router
from app.routes import product_router
from app.routes import kart_router
from app.routes import order_router

app.include_router(auth_router)
app.include_router(product_router)
app.include_router(kart_router)
app.include_router(order_router)


# para rodar o nosso código, executar no terminal: uvicorn app.main:app --reload

# endpoint:
# dominio.com/pedidos


# Rest APIs
# Get -> leitura/pegar
# Post -> enviar/criar
# Put/Patch -> edição
# Delete -> deletar