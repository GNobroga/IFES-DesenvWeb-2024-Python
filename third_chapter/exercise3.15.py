def is_quadrado_perfeito(n: int) ->  bool:
    if n < 1: return False 
    for i in range(n + 1):
        if i ** 2 == n:
            return True 
    return False

print(is_quadrado_perfeito(13))