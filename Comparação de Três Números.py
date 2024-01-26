#Comparação de Três Números

print('Insira três números inteiros, na sequência abaixo')

number_1 = int(input('Digite o primeiro número inteiro:'))
number_2 = int(input('Digite o segundo número inteiro:'))
number_3 = int(input('Digite o terceiro número inteiro:'))

maior_numero = number_1

# Verifica se o segundo número é maior
if number_2 > maior_numero:
    maior_numero = number_2

# Verifica se o terceiro número é maior
if number_3 > maior_numero:
    maior_numero = number_3

# Exibe o maior número
print(f"O maior número é: {maior_numero}")
