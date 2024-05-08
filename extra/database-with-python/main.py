from sql import (
    DatabaseFactory, 
    DatabaseType
)
from entities import Product
from repositories import ProductRepository

class InvalidArgument(Exception):
    
    def __init__(self, message: str):
        self.message = message

def create_product() -> Product:
    try:
        product_string = input('Insira o (nome, descricao, estoque e preco do produto): ')
        values = product_string.split(',')
        if len(values) != 4:
            raise InvalidArgument("Os campos do produto não foram passados corretamente")
    
        values[2] = int(values[2])
        values[3] = float(values[3])
        return Product(name=values[0], description=values[1], stock=values[2], price=values[3])
    except InvalidArgument as error:
        print(error.message)
    except:
        print('Um erro ocorreu durante a tentativa de criar')
    
    

def update_product():
    try:
        product_string = input('Insira o (id, nome, descricao, estoque, preco): ')
        values = product_string.split(',')
        if len(values) != 5:
            raise InvalidArgument("Os campos do produto não foram passados corretamente")
        
        values[0] = int(values[0])
        values[3] = int(values[3])
        values[4] = float(values[4])
        return Product(*tuple(values))
    except InvalidArgument as error:
        print(error.message)
    except:
        print('Um erro ocorreu durante a tentativa de atualizar')
        
    

def instructions():
    print('1 - Inserir')
    print('2 - Listar')
    print('3 - Alterar')
    print('4 - Excluir')
    print('5 - Detalhes')
    print('6 - Sair')

def get_choice():
    instructions()
    choice = int(input('Escolha: '))
    return choice

def show_menu():
    
    product_repository = ProductRepository(DatabaseFactory.get_connection(DatabaseType.SQLITE))
   
    while True:
        
        choice = get_choice()
        
        match choice:
            case 1:
                product_repository.create(create_product())
            case 2:
                [print(product) for product in product_repository.findAll()]
            case 3:
                product_repository.update(update_product())
            case 4:
                id = int(input('Insira o id: '))
                if product_repository.deleteByid(id):
                    print('Producto deletado com sucesso')
                else:
                    print('Produto não encontrado')
            case 6:
                print('Shutdown 👍👍👍')
                break 
            case _:
                print('Opção inválida 👌👌👌👌👌👌')


if __name__ == '__main__':
    show_menu()