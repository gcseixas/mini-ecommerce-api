from app.database import SessionLocal
from app.models.kart import ItensCarrinho

def create_item_kart(db):

    for i in range(100000):
        item = ItensCarrinho(
            usuario_id=1,
            produto_id=1,
            quantidade=10
        )
        print(f'Item{i} criado com sucesso')
        db.add(item)

        if i % 1000 == 0:
            db.commit()

    db.commit()


# Criando sessão manualmente
db = SessionLocal()
create_item_kart(db)
db.close()