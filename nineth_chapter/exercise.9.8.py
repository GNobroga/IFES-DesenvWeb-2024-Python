import random
import re

palavras = ['pera', 'manga', 'uva']

while True:
    
    try:
        palavra_digitada = input('Palavra digitada: ')
    
        if not re.match(r'[a-zA-Z]+', palavra_digitada):
            raise Exception('Apenas letra do alfabeto é permitido')
        
        palavra_escolhida = random.choice(palavras)
        
        if palavra_digitada == palavra_escolhida:
            print('Parabéns! Você acertou!!')
            break 
        else:
            print(f'Você errou! A palavra era {palavra_escolhida}')
    except Exception as error:
        print(error)