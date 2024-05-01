from . import EntityInvalidException
import re 

class Cliente(object):
    
    def __init__(self, nome: str, cpf: str):
        self.nome = nome 
        self.cpf = cpf 
        
    @property 
    def nome(self) -> str:
        return self._nome 

    @nome.setter 
    def nome(self, valor: str):
        if valor == None or valor.strip() == '':
            raise EntityInvalidException('O nome não pode ser vazio')
        if len(valor) < 3:
            raise EntityInvalidException('O nome não pode ter menos que 3 caracteres')
        
        self._nome = valor 
        
    @property 
    def cpf(self) -> str:
        return self._cpf 
    
    @cpf.setter 
    def cpf(self, valor: str):
        if valor == None or valor.strip() == '':
            raise EntityInvalidException('O CPF não pode ser vazio')
    
        if not re.match(r'\d{3}\.?\d{3}\.?\d{3}\.?-?\d{2}', valor):
            raise EntityInvalidException('CPF não possui um formato válido')
        
        self._cpf = valor
        
    def __repr__(self) -> str:
        return f'Nome {self.nome} CPF {self.cpf}'