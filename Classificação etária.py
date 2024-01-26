#Classificação Etária

age = int(input('Insira a sua idade, para saber em qual faixa etária você está:'))

if age <= 12:
    print('Hey! Você é uma criança!')
elif 13 <= age <= 19:
    print('Hey! Você já é um adolescente!')
elif 20 <= age <= 59:
    print('Uou! Você é um adulto!.')
else:
    print('Oh! Você é um idoso!')

