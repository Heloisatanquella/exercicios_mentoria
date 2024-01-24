# Lista para armazenar as informações de várias pessoas
lista_pessoas = []

# Dicionário para contar quantas pessoas foram cadastradas por estado
contagem_por_estado = {}

# Loop para cadastrar informações
while True:
    # Dicionário para armazenar as informações de uma pessoa
    pessoa = {}
    # entrará neste if, se já tiver alguém cadastrado
    if len(lista_pessoas) > 0:
        pessoa['nome'] = input('Digite o nome da pessoa (ou digite "sair" para encerrar): ')
        if pessoa['nome'].lower() == 'sair':
            break
    else:
        pessoa['nome'] = input('Digite o nome da pessoa: ')

    pessoa['endereco'] = input('Digite o endereço da pessoa: ')
    pessoa['cidade'] = input('Digite a cidade da pessoa: ')
    pessoa['estado'] = input('Digite o estado da pessoa: ')

    # Adicionar o dicionário da pessoa à lista
    lista_pessoas.append(pessoa)

    # Atualizar a contagem de pessoas por estado
    estado = pessoa['estado'].upper()
    # para adicionar a nova contagem ao original
    contagem_por_estado[estado] = contagem_por_estado.get(estado, 0) + 1

for pessoa in lista_pessoas:
    print(pessoa)

print(contagem_por_estado)
