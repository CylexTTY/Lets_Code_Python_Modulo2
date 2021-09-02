import random


def bubbleSort(lista):
    for i in range(len(lista) - 1):
        for j in range(1, len(lista) - i):
            if lista[j - 1] > lista[j]:
                lista[j - 1], lista[j] = lista[j], lista[j - 1]
    return lista


lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
random.shuffle(lista)
print('Shuffle list:', lista)
print('Ordered list:', bubbleSort(lista))
