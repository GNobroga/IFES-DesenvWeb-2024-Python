from entities import Cliente, Conta, EntityInvalidException
from typing import List, Union
import re 

def instrucoes():
    print(
        '\n1 - Criar uma conta',
        '\n2 - Depositar',
        '\n3 - Sacar',
        '\n4 - Transferir',
        '\n5 - Listar',
        '\n0 - Sair'
    )
    
def main():
    contas: List[Conta] = []
    while True:
        instrucoes()
        escolha = int(input("Escolha uma opção: "))
        
        match escolha:
            case 1:
                criar_conta(contas)
            case 2:
                depositar(contas) 
            case 3:
                sacar(contas)
            case 4:
                transferir(contas)
            case 5:
                [print(conta) for conta in contas]
            case 0:
                break
            case _:
                print('Opção não encontrada')
                
        
def obter_conta(cpf: str, contas: List[Conta]) -> Union[Conta, None]:
    def normalize(valor: str):
            return re.sub(r'\D', '', valor)
        
    contas = [conta for conta in contas if normalize(conta.cliente.cpf) == normalize(cpf)]
    
    if len(contas):
        return contas[0]
    
def sacar(contas: List[Conta]):
    try:
        cpf = input('CPF: ')
        
        conta = obter_conta(cpf, contas) 
        
        if not conta:
            raise Exception()
        
        conta.sacar(float(input('Valor: ')))
                
    except EntityInvalidException as error:
        print(error.mensagem)
    except Exception as error:
        print(error)
    else:
        print('Saque realizado com sucesso')
     
def criar_conta(contas: List[Conta]):
    try:
        nome = input('Nome: ')
        cpf = input('CPF: ')
        
        novo_cliente = Cliente(nome, cpf)
        nova_conta = Conta(novo_cliente, 1000)
        
        contas.append(nova_conta)
        
    except Exception as error:
        print('Ocorreu um erro: ', error)
    else:
        print('Conta criada com sucesso!')
    
def depositar(contas: List[Conta]):
    try:
        cpf_destino = input('CPF de destino: ')
        conta = obter_conta(cpf_destino, contas)
        
        if not conta:
            raise Exception()

        conta.depositar(float(input('Valor: ')))
        
    except EntityInvalidException as error:
        print(error.mensagem)
    except Exception as error:
        print('Ocorreu um erro inesperado, tente novamente mais tarde')
    else:
        print('Depositado realizado com sucesso!')

def transferir(contas: List[Conta]):
    try:
        cpf_origem = input('CPF de Origem: ')
        cpf_destino = input('CPF de Destino: ')
        valor = float(input('Valor: '))
    
        
        conta_origem = obter_conta(cpf_origem, contas)
        conta_destino = obter_conta(cpf_destino, contas)
        
        if not conta_origem or not conta_destino:
            raise Exception()
        
        conta_origem.transferir(valor, conta_destino)
        
    except EntityInvalidException as error:
        print(error.mensagem)
    except Exception as error:
        print('Ocorreu um erro inesperado, tente novamente.')
    else:
        print('Transferência realizada com sucesso!')
        

if __name__ == '__main__':
    main()