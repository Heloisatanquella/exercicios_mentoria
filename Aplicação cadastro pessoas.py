pessoas = []
ultimo_codigo = 0

# Funçao que exibe o menu do sistema
def menu():
    while True:
        print('\n Menu \n')
        print('1 - Inserir pessoa')
        print('2 - Alterar pessoa')
        print('3 - Excluir pessoa')
        print('4 - Visualizar pessoa')
        print('5 - Listas pessoas')
        print('6 - Sair \n')

        opcao = input()

        # Verifica se a opção é um valor válido
        if opcao.isdigit():
            opcao = int(opcao)
            if opcao > 0 and opcao < 7:
                return opcao

        # Caso inválido o menu é exibido novamente
        else:
            print('\n Valor inválido \n')

# Funçao que gera um novo código
def gerar_codigo():
    global ultimo_codigo
    ultimo_codigo += 1
    return ultimo_codigo

# Funçao que cadastra uma pessoa no sistema
def cadastro():
    pessoa = {}

    # Gera um novo código para o novo cadastro
    pessoa['codigo'] = gerar_codigo()
    pessoa['nome'] = input('Digite o nome da pessoa: ')

    # Verifica se o valor da idade é válido
    while True:
        idade = input('Digite a idade da pessoa: ')

        if idade.isdigit():
            pessoa['idade'] = int(idade)
            break
        else:
            print('Apenas valores inteiros serão aceitos')

    # Adiciona a pessoa a lista de pessoas
    pessoas.append(pessoa)
    print(pessoa)

# Função que lista todas as pessoas do sistema
def listar():
    print('\n Pessoas: \n')
    print(pessoas)

# Função que faz a busca da pessoa a partir do seu código
def buscar_pessoa(codigo):
    for pessoa in pessoas:
        if pessoa['codigo'] == codigo:
            return pessoa

# Função que retorna o codigo de busca válidado
def input_codigo():
    while True:
        codigo = input('Digite o código da pessoa: ')

        if codigo.isdigit():
            return int(codigo)
        else:
            print('Digite um código válido')

# Função que faz o print da pessoa escolhida
def visualizar():
    codigo = input_codigo()     
    pessoa = buscar_pessoa(codigo)

    # Válida se o código pertence a uma pessoa do sistema
    if pessoa:
        print(pessoa)
    else:
        print('Pessoa não encontrada')

# Função que deleta uma pessoa do sistema
def excluir():
    codigo = input_codigo()
    pessoa = buscar_pessoa(codigo)

    # Válida se o código pertence a uma pessoa do sistema
    if pessoa:
        # Remove a pessoa do sistema
        pessoas.remove(pessoa)
        print('Pessoa deletada')
    else:
        print('Pessoa não encontrada')

# Função que altera uma pessoa do sistema
def alterar():
    codigo = input_codigo()
    pessoa = buscar_pessoa(codigo)

    if pessoa:
        # Altera a pessoa do sistema, se ela existir
        pessoa['nome'] = input('Atualize o nome da pessoa: ')
        while True:
            idade = input('Atualize a idade da pessoa: ')

            if idade.isdigit():
                pessoa['idade'] = int(idade)
                break
            else:
                print('Apenas valores inteiros serão aceitos')    
        print('Pessoa Atualizada')    
    else:
        print('Pessoa não encontrada')
        

# Funçao que inicia o sistema
def main():
    while True:
        opcao = menu()
        if opcao == 1:
            cadastro()

        elif opcao == 2:
            alterar()

        elif opcao == 3:
            excluir()

        elif opcao == 4:
            visualizar()

        elif opcao == 5:
            listar()

        elif opcao == 6:
            break


main()
