from random import randint
numbers = [n for n in range(1, 11)]

for index, number in enumerate(numbers):
    if index % 2 == 0:
        new_index = randint(0, 9)
        swap = numbers[new_index]
        numbers[new_index] = number 
        numbers[index] = swap
        
print(numbers)