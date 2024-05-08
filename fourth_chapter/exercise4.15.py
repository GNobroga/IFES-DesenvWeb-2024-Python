from collections import Counter 

phrase = input('Phrase: ')

for word, count in Counter(phrase.split(' ')).items():
    print(f'A palavra {word} apareceu {count} vezes')
