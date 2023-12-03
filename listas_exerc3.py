lista = ['Fernando', 'Kaian', 'Jonas', 'Erick', 'Tulio', 'Matheus']
print('Informe o nome que procura')
nome = input()

encontrado = False

for n in range(0, len(lista)):
    print(lista[n])
    if lista[n].lower() == nome.lower():
        encontrado = True
if encontrado == False:
    print('Nome não encontrado!')
else:
    print('Nome Encontrado')
