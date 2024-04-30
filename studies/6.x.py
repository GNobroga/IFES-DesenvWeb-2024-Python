# Faça um programa que percorra uma lista de 200 números e retorne os divisíveis por 3 e 5
from random import randint, choice


print([n for n in range(201) if n % 15 == 0] )


l1 = [3, 7, 4, 6, 9]
l2 = [5, 2, 1, 7, 3]

print()
print([(x + y) / 2 for x, y in zip(l1, l2)])


palavras = ["pedra", "papel", "tesoura"]

while not (mensagem := input("Jogo (Pedra, Papel, Tesoura): ").lower()) == "sair":
    
    if mensagem == "sair":
        break
    
    if not mensagem in palavras:
        print("Não existe essa opção")    
        continue 
    
    
    maquina = choice(palavras)
    
    if mensagem == maquina:
        print("Empate")
    elif mensagem == "pedra":
        if maquina == "papel":
            print("Máquina ganhou")
        else:
            print("Você ganhou")
    elif mensagem == "papel":
        if maquina == "pedra":
            print("Você ganhou")
        else:
            print("Máquina ganhou")
    elif mensagem == "tesoura":
        if maquina == "pedra":
            print("Máquina ganhou")
        else:
            print("Você ganhou")
            
    print(f"Máquina {maquina} - Você {mensagem}")
    