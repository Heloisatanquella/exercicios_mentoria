people_list = []

count_state = {}

while True:
    person = {}
    if len(people_list) > 0:
        person['nome'] = input('Digite o nome da person (ou digite "sair" para encerrar): ')
        if person['nome'].lower() == 'sair':
            break
    else:
        person['nome'] = input('Digite o nome da pessoa: ')

    person['endereço'] = input('Digite o endereço da pessoa: ')
    person['cidade'] = input('Digite a cidade da pessoa: ')
    person['estado'] = input('Digite o estado da pessoa: ')

    people_list.append(person)

    state = person['estado'].upper()
    count_state[state] = count_state.get(state, 0) + 1

for person in people_list:
    print(person)

print(count_state)
