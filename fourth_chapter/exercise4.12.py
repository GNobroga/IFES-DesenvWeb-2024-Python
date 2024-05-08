def check_words():
    while  word := input("Digite uma frase: "):
        count = [0, 0]
        for value in word.split(' '):

            if value.endswith('o'):
                count[0] += 1 
            
            if value.endswith('a'):
                count[1] += 1
        
        print("Terminam com o %d" % (count[0]))
        print("Terminam com a %d" % (count[1]))

check_words()