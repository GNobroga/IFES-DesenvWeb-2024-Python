"""
    Exercício 1.4
"""

def main():
    try:     
        weight: float = float(input("Enter your weight: "))
        height: float = float(input("Enter your height: "))

        imc: float = weight / height ** 2

        print(f"Result {imc:.2f}")
    except:
        print('Invalid values were passed')
        main()

if __name__ == '__main__':
    main()