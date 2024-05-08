from math import sqrt
from collections import Counter

# 0 20

print(sum([sqrt(n) for n in range(21) if n % 2 == 0]))  

frase = "Caguei comi e corri"

print(list(map(lambda x: { x: len(x) }, frase.split(' '))))
