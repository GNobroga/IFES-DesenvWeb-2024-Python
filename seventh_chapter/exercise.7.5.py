import os 

if not os.path.exists('./arquivo-criado.txt'):
    open('./arquivo-criado.txt', 'w').close()
else:
    file_name = input('Enter a filename to remove: ')
    os.remove(f'./{file_name}')