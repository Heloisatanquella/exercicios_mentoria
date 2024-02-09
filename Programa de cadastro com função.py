lista_pessoas = []
contagem_por_estado = {}

def cadastro_pessoas():
    pessoa = {}
    if len(lista_pessoas) > 0:
        pessoa['nome'] = input('Digite o nome da pessoa (ou digite "sair" para encerrar): ')
        if pessoa['nome'].lower() == 'sair':
            return 
    else:
        pessoa['nome'] = input('Digite o nome da pessoa: ')

    pessoa['endereco'] = input('Digite o endereço da pessoa: ')
    pessoa['cidade'] = input('Digite a cidade da pessoa: ')
    pessoa['estado'] = input('Digite o estado da pessoa: ')

    return pessoa

def atualizar_estado(estado):
    contagem_por_estado[estado] = contagem_por_estado.get(estado, 0) + 1

def main():
    while True:
        pessoa = cadastro_pessoas()

        if pessoa:
            lista_pessoas.append(pessoa)
            estado = pessoa['estado'].upper()
            atualizar_estado(estado)

        else:
            break

    for pessoa in lista_pessoas:
        print(pessoa)
    
    print(contagem_por_estado)
    
main()