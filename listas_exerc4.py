lista1 = list(range(1, 6))
lista2 = list(range(1, 6))

for n in range(0, 5):
    print('Informe o numero da posicao ', n+1, 'da primeira lista')
    lista1[n] = int(input())

for n in range(0, 5):
    print('Informe o numero da posicao ', n+1, 'da segunda lista')
    lista2[n] = int(input())

for n in range(0, 5):
    if lista1[n] == lista2[n]:
        print('Coincidencia do valor ', lista1[n], 'na posicao ', n+1)
    else:
        print('Valores ', lista1[n], 'e', lista2[n], 'diferentes na posicão', n+1)
