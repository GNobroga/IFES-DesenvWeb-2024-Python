
class Animal:
    
    def __init__(self, nome: str, idade: int):
        self.nome = nome 
        self.idade = idade 
        
    def emitir_som(self):
        print('KKKKKKKKKKKKKKKKKKKKKKKKKK')
        

animal = Animal('Popo', 1000)

animal.emitir_som()