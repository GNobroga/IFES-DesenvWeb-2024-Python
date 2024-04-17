import re

"""
    Exercício 2.8
"""


def is_date(text: str) -> bool:
    if not re.match(r'\d{2}/\d{2}/\d{4}', text): return False
    day, month, year = map(int, text.split('/'))
    return  1 <= day <= 31 and 1 <= month <= 12 and 1 <= year <= 9999

date = input("Enter a date (dd/mm/yyyy): ")

if is_date(date):
    print("The date is valid")
else:
    print("Invalid date")


