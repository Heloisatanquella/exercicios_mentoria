cont_alunos = 0
alunos_aprovados = []
alunos_reprovados = []

def cadastrar_aluno():
    aluno = {}

    if cont_alunos > 0:
        aluno['nome'] = input('Digite o nome do aluno (ou digite "sair" para encerrar): ')
        if aluno['nome'].lower() == 'sair':
            return 'sair'     
    else:
        aluno['nome'] = input('Digite o nome do aluno: ')

    while True:
        idade = input('Digite a idade do aluno: ')

        if idade.isdigit():
            aluno['idade'] = int(idade)
            break
        else:
            print('Apenas valor inteiros serão aceitos')
        
    aluno['estado_civil'] = input('Digite o estado civil do aluno: ')
    aluno['genero'] = input('Digite o gênero do aluno: ')
    aluno['curso'] = input('Digite o curso do aluno: ')
    aluno['notas'] = []

    return aluno

def cadastrar_nota(aluno):
    if len(aluno['notas']) > 0:
        nota = input('Dê uma nota para o aluno (ou digite "sair" para seguir com o proximo aluno): ')

        if nota.lower() == 'sair':
            return 'sair'
    else:
        nota = input('Dê uma nota para o aluno: ')

    if nota.isdigit():
        nota = float(nota)
        if nota > 10:
            print('A nota tem um valor máximo de 10')
        else:
            aluno['notas'].append(nota)

    else:
        print('A nota deve ser um número')


def aprovacao_aluno(aluno):
    media = sum(aluno['notas']) / len(aluno['notas'])

    global cont_alunos
    cont_alunos += 1

    if media >= 7:
        alunos_aprovados.append(aluno)
    else:
        alunos_reprovados.append(aluno)


def visualizar_alunos(lista_alunos):
    for aluno in lista_alunos:
        print('Aluno: ', aluno['nome'])
        print('Notas: ', aluno['notas'])
        print('\n')


def main():
    while True:
        aluno = cadastrar_aluno()
        if aluno == 'sair':
            break
        else:
            while True:
                nota = cadastrar_nota(aluno)
                if nota == 'sair':
                    break
            
        aprovacao_aluno(aluno)

    print('\n Aprovados: \n')
    visualizar_alunos(alunos_aprovados)

    print('\n Reprovados: \n')
    visualizar_alunos(alunos_reprovados)

main()