
"""
    Exercício 1.1
"""

def display_name(name: str, age: int) -> None:
    print("%s %d" % (name, age))

name = "Gabriel Cardoso"
age = 24

display_name(
    name=name,
    age=age
)