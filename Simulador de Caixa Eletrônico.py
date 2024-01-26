#Simulador de Caixa Eletrônico

balance = float(input('Insira o saldo atual da sua conta:'))
withdrawal_value = float(input('Insira o valor que deseja sacar:'))

if withdrawal_value > balance:
    print('O seu saldo é insuficiente para este saque.')
else:
    print(f'Saque de R${withdrawal_value:.2f} realizado com sucesso.')

balance -= withdrawal_value
print(f'Seu novo saldo é de: R${balance:.2f}')
