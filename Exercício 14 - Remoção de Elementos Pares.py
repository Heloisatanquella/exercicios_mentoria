#Criando a lista de números completa
lista_numeros = [19, 4, 39, 22]

#Criando uma lista para armazenar somente os ímpares
lista_impares = []

#Removendo os elementos pares da lista original
for numero in lista_numeros:
    if numero % 2 != 0:
        lista_impares.append(numero)

print(f'A lista de números ímpares é igual a: {lista_impares}')

