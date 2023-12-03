from statistics import mean

lista = list(range(1, 11))
for n in range(0, 10):
    print('Informe o numero na posição: ', n+1)
    lista[n] = int(input())
    while lista[n] <= 0:
        print('Entrada inválida, por favor repita!')
        lista[n] = int(input())

soma = 0
for n in range(0, 10):
    soma += lista[n]

print('Media calculada', soma)
print('Média calculada por função ', mean(lista))
