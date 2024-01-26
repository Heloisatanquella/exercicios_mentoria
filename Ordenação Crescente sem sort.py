lista_numeros = [9, 45, 23, 2, 85, 64]
lista_ordenada = []

while len(lista_numeros) > 0:
    m = min(lista_numeros)
    lista_numeros.remove(m)
    lista_ordenada.append(m)

print(lista_ordenada)
