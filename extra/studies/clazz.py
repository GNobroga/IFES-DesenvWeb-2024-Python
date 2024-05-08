from abc import abstractmethod

class Funcionario(object):

    def __init__(self, salario: float):
        self.salario = salario

    def calcular_salario(self):
        return self.salario * 1.15
    
    
class Pai:
        
    def gemer(self):
        print("AIIIIIIIIIIIIII PAI PARA!")
    
class Mae:
    
    def gemer(self):
        print("AIIII QUE GOSTOSIM")

class Person(Pai, Mae, Funcionario):
    
    def __init__(self):
        super().__init__(1000)
        self._name = ""
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        print("CAFE")
        self._name = value
        
    def __repr__(self):
        return self._name
    
    def __add__(self, other):
        return f"{self.name} {other.name}"
        
p = Person()

p.name = "José"

p2 = Person()

p2.name = "Carlinhos"

print(p + p2)