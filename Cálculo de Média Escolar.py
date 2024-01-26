#Cálculo de Média Escolar

print('Insira as notas de suas três provas para calcularmos sua média')

note_1 = float(input('Digite a primeira nota:'))
note_2 = float(input('Digite a segunda nota:'))
note_3 = float(input('Digite a terceira nota:'))

result = (note_1 + note_2 + note_3) / 3

print(f'A média das três notas inseridas é: {result:.2f}.')

if result > 10.0:
    print('Resultado inválido, verifique as notas inseridas')
elif result >= 7.0:
    print('Parabéns, você foi aprovado!')
else:
    print('Sinto muito, você foi reprovado.')
