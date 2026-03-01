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
        return instancia
    
    
    @staticmethod
    def criar(db, model, dados):
        nova_instancia = model(**dados.model_dump())
        db.add(nova_instancia)
        db.commit()
        db.refresh(nova_instancia)
        return nova_instancia
    

    @staticmethod
    def deletar(db, instancia):
        db.delete(instancia)
        db.commit()