
class EntityInvalidException(Exception):
    
    def __init__(self, mensagem: str):
        self.mensagem = mensagem