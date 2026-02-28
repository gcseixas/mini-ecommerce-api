
def atualizar_campos_model(item, dados):
    """A função recebe:
        - Model onde será atualizado
        - Esquema da atualização    
    """
    campos_atualizacao = dados.dict(exclude_unset=True)
    
    for campo, valor in campos_atualizacao.items():
        setattr(item, campo, valor)
    
    return item
    