import re
phrase = input("Phrase: ").split(' ')

print([re.sub('a', 'o', word) for word in phrase if 'a' in word])