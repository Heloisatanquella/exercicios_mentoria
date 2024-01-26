#listas para armazenar as informações
lista_alunos = []
cont_alunos = 0
alunos_aprovados = []
alunos_reprovados = []

while True:
    aluno = {}

    #caso já tenha um aluno cadastrado, vai dar a opção de encerrar, senão, vai ser obrigado a inserir um pelo menos
    if cont_alunos > 0:
        aluno['nome'] = input('Digite o nome do aluno (ou digite "sair" para encerrar): ')
        if aluno['nome'].lower() == 'sair':
            break
    else:
        aluno['nome'] = input('Digite o nome do aluno: ')

    while True:
        idade = input('Digite a idade do aluno: ')

        #vai verificar se é um valor numérico, se for inteiro, o loop é encerrado, senão, o loop se repete
        if idade.isdigit():
            aluno['idade'] = int(idade)
            break
        else:
            print('Apenas valor inteiros serão aceitos')

    aluno['estado_civil'] = input('Digite o estado civil do aluno: ')
    aluno['genero'] = input('Digite o gênero do aluno: ')
    aluno['curso'] = input('Digite o curso do aluno: ')

    #armazenar as notas que ainda serão inseridas
    aluno['notas'] = []

    while True:
        #caso já tenha uma nota cadastrada, vai dar a opção de encerrar, senão, vai ser obrigado a inserir uma pelo menos
        if len(aluno['notas']) > 0:
            nota = input('Dê uma nota para o aluno (ou digite "sair" para seguir com o proximo aluno): ')

            if nota.lower() == 'sair':
                break
        else:
            nota = input('Dê uma nota para o aluno: ')
        #vai verificar se é um valor numérico, se for, o loop é encerrado, senão, o loop se repete
        if nota.isdigit():
            nota = float(nota)
            if nota > 10:
                print('A nota tem um valor máximo de 10')
            else:
                aluno['notas'].append(nota)

        else:
            print('A nota deve ser um número')

    media = sum(aluno['notas']) / len(aluno['notas'])

    cont_alunos += 1

    if media >= 7:
        alunos_aprovados.append(aluno)
    else:
        alunos_reprovados.append(aluno)


print('\n Aprovados: \n')

for aluno in alunos_aprovados:
    print('Aluno: ', aluno['nome'])
    print('Notas: ', aluno['notas'])
    print('\n')

print('\n Reprovados: \n')

for aluno in alunos_reprovados:
    print('Aluno: ', aluno['nome'])
    print('Notas: ', aluno['notas'])
    print('\n')


