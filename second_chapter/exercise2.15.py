
vowels = ['a', 'e', 'i', 'o', 'u']

word = input('Enter: ')

if word:
    if word[0] in vowels:
        print("A palavra começa com vogal")
    elif word[0].isdigit():
        print("A palavra não começa com número")
    else:
        print("A palavra começa com consoante")
else:
    print("Digite uma palavra")
