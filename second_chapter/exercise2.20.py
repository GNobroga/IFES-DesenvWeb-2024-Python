import re

"""
    Exercício 2.20
"""

def is_cpf(value: str) -> bool:
    if type(value) is not str or (len(value) != 11 and len(value) != 14): return False 
    value = re.sub(r'\D', '', value)
    digits = list(value)
    if not value.isdigit() or is_unique_sequence(digits): return False
    return calc_digit(digits[:9]) == int(digits[9]) and calc_digit(digits[:10]) == int(digits[10])

def is_unique_sequence(digits: list) -> bool:
    return all([digit == digits[0] for digit in digits])

def calc_digit(digits: list) -> int:
    quantifier = len(digits) + 1
    totalDigits = 0
    for digit in digits:
        totalDigits = totalDigits + int(digit) * quantifier 
        quantifier = quantifier - 1
    remaining = totalDigits % 11
    return 0 if remaining < 2 else 11 - remaining 


print(is_cpf("173.645.097-20"))
