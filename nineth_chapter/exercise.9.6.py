import random 

acertou = False

while not acertou:
    
    try:
        numero = int(input('Número: '))
        numero_gerado = random.randint(1, 10)
        
        print(f'Número gerado {numero_gerado}')
        
        if numero == numero_gerado:
            acertou = not acertou 
            print('Você acertou!!')
            break 
        else:
            print('Não foi dessa vez')
    except:
        print('Um erro ocorreu, tente denovo!')