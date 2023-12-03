lista = list(range(1, 11))

for n in range(0, 10):
    print('Informe o numero da posição: ', n+1)
    lista[n] = int(input())

lista2 = sorted(lista)
print('O maior valor é: ', lista2[9])
print('O menor valor é: ', lista2[0])

print('O maior valor é: ', max(lista))
print('O menor valor é: ', min(lista))