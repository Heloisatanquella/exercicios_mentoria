clientes = []
produtos = []

def menu_principal():
    while True:
        print('\n Menu \n')
        print('1 - Cadastrar novo cliente, produto ou pedido')
        print('2 - Buscar clientes ou produtos')
        # print('3 - Criar novos pedidos associados a clientes existentes')
        print('3 - Sair \n')

        opcao = input()

        if opcao.isdigit():
            opcao = int(opcao)
            if opcao > 0 and opcao < 4:
                return opcao
            else:
                print('\n O valor inserido é inválido \n')
        else:
            print('\n O valor inserido é inválido \n')

def submenu_cadastro():
    while True:
        print('\n Submenu \n')
        print('1 - Cadastrar novo cliente')
        print('2 - Cadastrar novo produto')
        print('3 - Cadastrar novo pedido a um novo cliente')
        print('4 - Criar novos pedidos associados a clientes existentes')
        print('5 - Voltar ao menu principal \n')

        opcao = input()

        if opcao.isdigit():
            opcao = int(opcao)
            if opcao == 5:
                break
            elif opcao == 1:
                cadastro() 
            elif opcao == 2:
                produto()
            elif opcao == 3:
                pedido_cadastro_cliente() 
            elif opcao == 4:
                pedido_cliente_existente()
            else:
                print('\n O valor inserido é inválido \n')
        else:
            print('\n O valor inserido é inválido \n')

def submenu_busca():
    while True:
        print('\n Submenu \n')
        print('1 - Buscar cliente')
        print('2 - Buscar produto')
        print('3 - Voltar ao menu principal \n')

        opcao = input()

        if opcao.isdigit():
            opcao = int(opcao)
            if opcao == 3:
                break
            elif opcao == 1:
                busca_cliente()
            elif opcao == 2:
                busca_produto()
            else:
                print('\n O valor inserido é inválido \n')

        else:
            print('\n O valor inserido é inválido \n')

def busca_cliente():
    while True:
        email = input('\nDigite o e-mail do cliente: ')
        cliente = buscar(email, clientes, 'e-mail')
        if cliente:
            print(cliente)
            return cliente
        else:
            print('Não encontrado')

def busca_produto():
    while True:
        nome = input('Digite o nome do produto: ')
        produto = buscar(nome, produtos, 'nome')
        if produto:
            print(produto)
            return produto
        else:
            print('Não encontrado')

def cadastro():
    cliente = {}

    cliente['pedidos'] = []
    cliente['nome'] = input('\nDigite o primeiro nome do cliente: ')
    cliente['sobrenome'] = input('Digite o sobrenome do cliente: ')
    
    while True:
        email = input('Insira o e-mail do cliente: ')
        duplicado = buscar(email, clientes, 'e-mail')

        if duplicado:
            print('\nE-mail já cadastrado. Tente novamente. \n')
        else:
            cliente['e-mail'] = email
            break

    cliente['telefone'] = input('Insira o número para contato do cliente (DDD 9 9999.9999): ')

    clientes.append(cliente)
    print('\n Dados do cliente cadastrado \n')
    print(cliente)

    return cliente

def buscar(valor, lista, chave):
    for item in lista:
        if item[chave] == valor:
            return item

def produto():
    produto = {}

    while True:
        nome = input('Digite o nome do produto: ')
        duplicado = buscar(nome, produtos, 'nome')

        if duplicado:
            print('Produto já existente. Tente novamente.')
        else:
            produto['nome'] = nome
            break

    produto['descrição'] = input('Insira a descrição do produto: ')

    while True:
        preco = input('Insira o preço do produto (00,00): ')

        try:
            produto['preço'] = float(preco)
            break
        except ValueError:
            print('\nO valor inserido não é válido \n')
            
    while True: 
        quantidade = input('Insira a quantidade em estoque: ')

        if quantidade.isdigit():
            produto['quantidade'] = int(quantidade)
            break
        else:
            print('\nApenas valores inteiros serão aceitos \n')

    produtos.append(produto)
    print('\n Dados do produto cadastrado \n')
    print(produto)

def pedidos(cliente):
    pedido = {}
    pedido['produtos'] = []
    pedido['total_do_pedido'] = 0

    while True:
        item = {}
        produto = {}

        while True:
            produto = busca_produto()
            if produto:
                item['nome'] = produto['nome']
                break

        while True:
            quantidade = input('Digite a quantidade: ')

            if quantidade.isdigit():
                quantidade = int(quantidade)
                if quantidade <= produto['quantidade']:
                    produto['quantidade'] = produto['quantidade'] - quantidade
                    item['quantidade'] = quantidade
                    break
                else:
                    print('\nEstoque insuficiente \n')
            else:
                print('\nApenas valores inteiros serão aceitos \n')

        item['total'] = produto['preço'] * item['quantidade']
        pedido['total_do_pedido'] = pedido['total_do_pedido'] + item['total']
        pedido['produtos'].append(item)
        print(item)

        print('Cadastrar mais produtos? \n')
        print('1: Sim \n')
        print('2: Não \n')

        novo = 1
        while True:  
            novo = input()

            if novo.isdigit():
                novo = int(novo)
                if novo == 2:
                    cliente['pedidos'].append(pedido)
                    print(cliente['pedidos'])
                    return pedido
                elif novo == 1:
                    print(item)
                    break
                else:
                    print('\nValor inválido \n')
            
            else:
                print('\nApenas valores inteiros serão aceitos \n')

def pedido_cliente_existente():
    cliente = busca_cliente()
    pedidos(cliente)

def pedido_cadastro_cliente():
    print('\nÉ necessário cadastrar um cliente \n')
    cliente = cadastro()
    pedidos(cliente)

def main():
    while True:
        opcao = menu_principal()
        if opcao == 1:
            submenu_cadastro()
        
        elif opcao == 2:
            submenu_busca()

        elif opcao == 3:
            pedido_cliente_existente()

        elif opcao == 4:
            break

main()

   