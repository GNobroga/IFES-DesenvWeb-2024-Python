
def fatorial(n) -> int:
    if n <= 1: return 1 
    mul = 1
    for i in range(n, 1, -1):
        mul = mul * i 
    return mul 

print(fatorial(5))