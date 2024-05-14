
class Calculadora:
    
    def __init__(self, valor_inicial: float):
        Calculadora.verificar_numero(valor_inicial)
        self.valor = valor_inicial
    
    def somar(self, outro_valor: float):
        Calculadora.verificar_numero(outro_valor)
        self.valor += outro_valor
        return self 
    
    def subtrair(self, outro_valor: float):
        Calculadora.verificar_numero(outro_valor)
        self.valor -= outro_valor
    
    def multiplicacao(self, outro_valor: float):
        Calculadora.verificar_numero(outro_valor)
        self.valor *= outro_valor
    
    def divisao(self, outro_valor: float):
        Calculadora.verificar_numero(outro_valor)
        if outro_valor == 0:
            raise Exception('O valor não pode ser nulo na divisão')
        self.valor /= outro_valor
        
    def ver_valor(self):
        print(f'Valor atual: {self.valor}')
        
    @staticmethod
    def verificar_numero(valor: float):
        if type(valor) != int and type(valor) != float:
            raise Exception('Apenas número é aceito nos parâmetros dessa classe')

calculadora = Calculadora(1000)

calculadora.divisao(10)

calculadora.ver_valor()