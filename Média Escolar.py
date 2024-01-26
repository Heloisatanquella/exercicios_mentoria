#sair = False
#while not sair:
#    nota = input('Insira a nota da prova: ')
#    if nota == 'sair':
#        sair = True
#    else:
#        notas.append(float(nota))

notas = []

#looping infinito
while True:
        nota = input('Dê uma nota para o aluno (ou digite "sair" para seguir com o proximo aluno): ')

        if nota.lower() == 'sair':
            break
        try:
            nota_float = float(nota)
            notas.append(nota_float)
        except ValueError:
            print('Por favor, insira um número válido, ou digite "sair" para encerrar')

media = 0
if len(notas) > 0:
    media = sum(notas) / len(notas)

if media > 10:
    print('Resultado inválido, verifique as notas inseridas')
elif media >= 7:
    print(f'Parabéns, você foi aprovado! Sua média é {media}.')
else:
    print(f'Sinto muito, você foi reprovado. Sua média foi de {media}.')

