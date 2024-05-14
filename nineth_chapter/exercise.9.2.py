

def apenas_numeros(fnc):
    
    def interno(*args, **kwargs):
        if not 'valores' in kwargs:
            raise Exception('O argumento nomeado valores é obrigatório')
        valores = kwargs['valores']
        if type(valores) != list or len(valores) == 0:
            raise Exception('Valores deve ter elementos e ser uma lista')
        for valor in valores:
            if type(valor) != int and type(valor) != float:
                raise Exception('Apenas números são aceitos')
        return fnc 
    return interno



try:
    @apenas_numeros
    def media_aritmetica(list, /):
        return sum(list) / len(list) 
    
    media_aritmetica(valores=[1, 2, 3])
    
except Exception as error:
    print(error)

