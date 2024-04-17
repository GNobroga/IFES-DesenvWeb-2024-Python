import math 

"""
    Exercício 1.5
"""

def bhaskara(a: int, b: int, c: int) -> int:
   
    def x1(a: int, b: int, c: int) -> int:
        return (-b + math.sqrt(math.pow(b, 2) - 4 * a * c)) / 2 * a
    
    def x2(a: int, b: int, c: int) -> int:
        return (-b - math.sqrt(math.pow(b, 2) - 4 * a * c)) / 2 * a 
    
    return x1(a, b, c), x2(a, b, c)

# x^2 - 3x - 54 = 0
print(bhaskara(1, -3, -54))