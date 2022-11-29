lista = [5, 3, 9, 1, 7]

for i in range(len(lista) - 1):
    for j in range(i + 1, len(lista)):
        print(i, j, lista, end='')
        if lista[i] > lista[j]:
            lista[i], lista[j] = lista[j], lista[i]
            print('!', lista[i], lista[j])
            print('   ', lista)
        else:
            print('')
