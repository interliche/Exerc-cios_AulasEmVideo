valor = 1
valores = list()
pares = list()
impares = list()
while True:
    valor = int(input('Digite um número: '))

    if (valor % 2 == 0):
        pares.append(valor)
        valores.append((valor))
        
    else:
        impares.append(valor)
        valores.append(valor)

    resp = str(input('Quer sair? [S/N]'))
    if resp == 'S':
       break

valores.sort()
pares.sort()
impares.sort()

print('=-' * 30)
print(f'A lista completa é {valores}')
print(f'A lista de pares é {pares}')
print(f'A lista de ímpares é {impares}')
