# app/database.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = "sqlite:///./mini_ecommerce.db"

engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False}  # obrigatório no SQLite
)

SessionLocal = sessionmaker(bind=engine) # type: ignore

Base = declarative_base()
