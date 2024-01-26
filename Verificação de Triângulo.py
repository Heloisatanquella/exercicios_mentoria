#Verificação de Triângulo

side_1 = float(input('Insira o comprimeiro em centímetros do primeiro lado do triângulo:'))
side_2 = float(input('Insira o comprimeiro em centímetros do segundo lado do triângulo:'))
side_3 = float(input('Insira o comprimeiro em centímetros do terceiro lado do triângulo:'))

print('O tipo do triângulo é:')

if side_1 == side_2 == side_3:
    print('Equilátero')
elif side_1 == side_2 or side_1 == side_3 or side_2 == side_3:
    print('Isósceles')
else:
    print('Escaleno')
