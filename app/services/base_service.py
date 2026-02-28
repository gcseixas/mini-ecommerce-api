class BaseService:

    @staticmethod
    def atualizar_campos(model, dados):
        valores = dados.model_dump(exclude_unset=True)
        for campo, valor in valores.items():
            setattr(model, campo, valor)
        return model
    
    @staticmethod
    def buscar_por_id(db, model, id):
        instancia = db.query(model).filter(model.id == id).first()
        if not instancia:
            raise ValueError(f"{model.__name__} não encontrado")
        return instancia