#Criando a lista de números
lista_numeros = [1, 2, 3]

#Criando uma lista cumulativa
lista_cumulativa = []

# Variável para armazenar a soma cumulativa
soma_cumulativa = 0

# Realizando a soma
for numero in lista_numeros:
    # Adicionar o número atual à soma cumulativa
    soma_cumulativa += numero
    # Adicionar a soma acumulativa à lista cumulativa
    lista_cumulativa.append(soma_cumulativa)

# Imprimir a lista cumulativa ao usuário
print(lista_cumulativa)

