from enum import Enum

"""
    Exercício 1.2
"""

class Operation(Enum):
    SUM = 0
    SUB = 1
    MUL = 2
    DIV = 3

def math(x: int, y: int, op: Operation) -> int:
    return {
        Operation.SUM: lambda x, y: x + y,
        Operation.SUB: lambda x, y: x - y,
        Operation.MUL: lambda x, y: x * y,
        Operation.DIV: lambda x, y: x / y
    }[op](x, y)
    
    
print(math(10, 5, Operation.MUL))