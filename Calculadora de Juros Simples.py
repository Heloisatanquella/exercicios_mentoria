#Exercício 04: cálculo de juro simples

#Solicitar ao usuário as informações

principal = float(input('Insira o valor principal:'))
taxa = float(input('Insira a taxa de juros:'))
tempo = float(input('Insira o tempo em anos:'))

# Convertendo a taxa para decimal
taxa = taxa / 100

#Calcular o montante

montante = principal + (principal * taxa * tempo)

#Exibe o resultado

print(f'O montante após {tempo} ano(s) é de: R$ {montante:}')
