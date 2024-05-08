

with open(file="./studies/message.txt", mode="r", encoding="utf-8") as file:
    print(file.readlines())
    
    inicio = input("Deseja voltar para o início? ").lower()
    
    if inicio == 'sim':
        file.seek(0, 0)
        print(file.readlines())
    
    print(file.readlines())