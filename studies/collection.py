from typing import List
from collections import Counter
from random import choice, shuffle

numeros: List[int] = [i for i in range(1, 10)]

# Map
print(list(map(lambda x: x * 2, numeros)))

notas = 1,2,3
pessoas = "Gabriel", "José", "Carlos"

# Zip
print(list(zip(pessoas, notas)))


# Set
v1 = {1, 2, 3, 4, 5}
v2 = {1, 2, 3, 4, 5}


print(v1 | v2)


# Counter

repeated = [1, 2, 3, 1, 1, 1]

print(Counter(repeated))

# Random
shuffle(repeated)
print(repeated)
print(choice(repeated))

# Generators

def generate():
    yield 1
    yield 2 
    
it = iter(generate())

print(
next(it) )

