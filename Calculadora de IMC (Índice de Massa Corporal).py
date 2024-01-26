# Calculadora de IMC (Índice de Massa Corporal)

weight = float(input('Digite o seu peso em quilogramas:'))
height = float(input('Digite a sua altura em metros:'))
imc = weight / (height ** 2)
print(f'Seu índice de Massa Corporal é de: {imc:.2f}')

if imc <= 18.5:
    print('Você está abaixo do peso.')
elif 18.5 < imc < 25:
    print('Você se encontra dentro da faixa de peso considerada saudável.')
elif 25 <= imc < 30:
    print('Você está com sobrepeso.')
elif 30 <= imc < 40:
    print('Você está na faixa de obesidade.')
else:
    print('Você está na faixa de obesidade mórbida.')
