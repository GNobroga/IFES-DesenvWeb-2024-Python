from re import sub

phrase = input('Enter phrase: ') 

print(" ".join(filter(lambda x: x != '', [sub(r'\s*', '', word) for word in phrase.split(' ')])))

