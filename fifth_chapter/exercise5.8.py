
def decode_message(message: str, length: int):
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    if len(message) == 0:
        return ''
    else:
        concat = decode_message(message[1::], length)
        
        letter = message[0].lower()
    
        if letter == 'a':
            concat += 'z'
        elif letter == 'z':
            concat += 'a'
        elif letter in letters:
            concat += letters[letters.index(letter) - 1]
        else:
            concat += letter 
            
              
        if length == len(concat):
            return concat[::-1]
    
        return concat
        

print(decode_message('bdfn12', 6))
