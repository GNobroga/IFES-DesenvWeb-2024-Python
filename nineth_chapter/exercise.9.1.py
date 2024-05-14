try:
    x = float(input('X: '))
    y = float(input('Y: '))
    print(x / y)
except ZeroDivisionError:
    print('O denominador não pode ser zero')
except:
    print('Falha na formatação dos dados')