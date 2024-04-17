from functools import reduce
"""
    Exercício 1.3
"""

def calculate_average(*args):
    return reduce(lambda x, y: x + y, args) / len(args)

print(calculate_average(1, 2, 3))