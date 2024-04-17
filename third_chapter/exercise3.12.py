"""
    Exercício 3.12
"""

def is_primo(value):
    count = 2
    for i in range(2, value):
        if value % i == 0:
            count = count + 1
            break

    return count == 2

print(sum([n for n in range(1, 100) if is_primo(n)]))
