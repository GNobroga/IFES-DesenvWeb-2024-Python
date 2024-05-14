
class Fracao:
    
    def __init__(self, numerador: int, denominador: int):
        self.numerador = numerador
        self.denominador = denominador
        
    def multiplicar(self, outro: 'Fracao'):
        return Fracao(self.numerador * outro.numerador, self.denominador * outro.denominador)
    def mostrar_dados(self):
        print(f"""
        {self.numerador}
        ---
        {self.denominador}
        """)

fracao = Fracao(2, 5)

fracao.mostrar_dados()

fracao.multiplicar(Fracao(3, 7)).mostrar_dados()