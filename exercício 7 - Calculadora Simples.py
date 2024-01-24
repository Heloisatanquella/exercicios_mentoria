# Calculadora Simples

number_1 = float(input('Digite o primeiro número:'))
number_2 = float(input('Digite o segundo número:'))
operation = input('Agora insira a operação desejada (+, -, *, /):')

if operation == '+':
    result = number_1 + number_2
elif operation == '-':
    result = number_1 - number_2
elif operation == '*':
    result = number_1 * number_2
elif operation == '/':
    if number_2 != 0:
        result = number_1 / number_2
    else:
        result = 'Divisão por zero não é permitida'
else:
    result = 'Operação inválida'

print(f'O resultado da operação {operation} utilizando os números {number_1} e {number_2} é: {result}.')

