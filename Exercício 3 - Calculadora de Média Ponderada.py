#Exercício 02: Cálculo de Média Ponderada

#Solicita as notas e os pesos

nota_1 = float(input('Insira a primeira nota:'))
peso_1 = float(input('Insira o peso da primeira nota:'))

nota_2 = float(input('Insira a segunda nota:'))
peso_2 = float(input('Insira o peso da segunda nota:'))

nota_3 = float(input('Insira a terceira nota:'))
peso_3 = float(input('Insira o peso da terceira nota:'))

#Calcular a média ponderada

media_ponderada = (nota_1 * peso_1 + nota_2 * peso_2 + nota_3 * peso_3) / 3

#Exibe a média ponderada na tela do usuário

print(f'A média ponderada das notas é: {media_ponderada:}')
