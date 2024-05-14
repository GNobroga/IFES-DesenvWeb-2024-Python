
def print_inverse_countdown(n: int) -> None:
    if n < 0: 
        print('Inverse countdown finished!')
        return
    print(n)
    print_inverse_countdown(n - 1)


print_inverse_countdown(5)