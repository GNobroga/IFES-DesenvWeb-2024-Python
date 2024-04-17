"""
    Exercício 3.18
"""
def fibonnaci(n: int):
    atual = -1
    futuro = -1
    anterior = 1
    for _ in range(n + 1):
        atual = anterior + futuro 
        futuro = anterior 
        anterior = atual 
        yield atual

for n in fibonnaci(10):
    print(n)



