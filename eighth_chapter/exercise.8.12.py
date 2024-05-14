

class Veiculo:
    
    def acelerar(self): 
        print("Veículo acelerando")
    
    def frear(self):
        print("Veículo Freando...")
        
    def exibir_velocidade(self):
        print("Veículo à 100km/h") 
        

class Carro(Veiculo):
    
    def __init__(self, marca: str):
        self.marca = marca 
    
    
veiculo: Veiculo = Carro("Ford")

veiculo.exibir_velocidade()