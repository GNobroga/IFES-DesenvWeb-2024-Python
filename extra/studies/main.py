"""
    replace
    lower
    upper
    split
    slice
    endswith
    startswith
    strip
    find
    count 
    len
"""

import re

def to_remove_no_alfacharacter(function):
    
    def intern(*args):
        newArgs = []
        for arg in args:
            if type(arg) is not str:
                raise Exception("Only str is accept")
            newArgs.append(re.sub(r"\W", "", arg))
        return function(*newArgs)
    return intern

@to_remove_no_alfacharacter
def showText(username: str, password: str, email: str) -> None:
    print(username)
    print(password)
    print(email)

showText("Livinha013$$$$", "Gostosinha123", "gabrielcar2232$$$$$***@gmail.com")


text = "umas me convidou para tomar café, mas que não sou besta."

print(re.sub(r'\b(as|os|o|a|um|uns|uma|umas|à|e)\b',"", text))


if re.match(r'\d{4}(1|2)(si|SI|sI|Si)\d{3}', "20211sI020"):
    print("Matricula ok ")

if not re.match(r'\d{4}(1|2)(si|SI|sI|Si)\d{3}', "201SI020"):
    print("Matricula falsificada")



# def ask():
#     while  word := input("Digite uma frase: "):
#         if len(word.split(" ")) == 5:
#             break
    
#     for word in word.split(" "):
#         print(word)


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


        