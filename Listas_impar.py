valores = int()
pares = list()
impares = list()
todos = list()
while True:
    valores = int(input('Digite um número: '))
    todos.append(valores)
    if valores % 2 == 0:
        pares.append(valores)
    else:
        impares.append(valores)
    resp = str(input('Quer continuar? [S/N]'))
    if resp in 'Nn':
        break
print('=-' * 30)
print(f'A lista completa é {todos}')
print(f'A lista de pares é {pares}')
print(f'A lista de ímpares é {impares}')
