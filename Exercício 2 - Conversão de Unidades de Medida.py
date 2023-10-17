# Exercício 02: Conversão de Unidades de Medida

# Solicita as medidas ao usuário em metros

metros = input('Insira uma medida em metros, para obter a conversão da medida para centímetros, milímetros e quilômetros:')

# Conversão da unidade de medida para centímetros #
centimetros = float(metros) * 100
milimetros = float(metros) * 1000
quilometros = float(metros) / 1000

# Imprime o resultado na tela do usuário
print(f'{metros} metros é igual a {centimetros} centímetros.')
print(f'{metros} metros é igual a {milimetros} milímetros.')
print(f'{metros} metros é igual a {quilometros} quilômetros.')