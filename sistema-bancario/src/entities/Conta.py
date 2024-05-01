from . import Cliente
from . import EntityInvalidException
import uuid 

class Conta:
    
    def __init__(self, cliente_alvo: Cliente, saldo_inicial = 0.0):
        self.numero = uuid.uuid4()
        self.cliente = cliente_alvo
        self.saldo = saldo_inicial
        
    @property 
    def saldo(self) -> str:
        return self._saldo 
    
    @saldo.setter 
    def saldo(self, valor: float):
        if valor < 0:
            raise EntityInvalidException('O valor não pode ser negativo')
        self._saldo = valor 
        
    def sacar(self, valor: float):
        if self.saldo < 0 or self.saldo < valor:
            raise EntityInvalidException('Não há saldo suficiente')
        self.saldo -= valor 
        
    def depositar(self, valor: float):
        if valor < 0:
            raise EntityInvalidException('O valor para depósito não pode ser negativo')
        self.saldo += valor
        

    def transferir(self, valor: float, conta_alvo: 'Conta'):
        self.sacar(valor)
        conta_alvo.depositar(valor)
        
    def __repr__(self):
        return f'Conta - {self.numero} Saldo - {self.saldo} Titular - {self.cliente.nome} CPF - {self.cliente.cpf}'