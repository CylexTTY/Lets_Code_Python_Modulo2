import random


def bubbleSort(lista, reverse=False):
    """
    Organiza uma lista de forma crescente ou decrescente usando o algoritmo de
    Bubble Sort.
    :param lista: lista principal
    :param reverse: False (se ordem crescente) / True (se ordem decrescente)
    :return: lista ordenada
    """
    ordered = False
    i = 0
    while not ordered:
        ordered = True
        for j in range(len(lista) - i - 1):
            if not reverse:
                if lista[j] > lista[j + 1]:
                    lista[j], lista[j + 1] = lista[j + 1], lista[j]
                    ordered = False
            elif lista[j] < lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                ordered = False
        i += 1
    return lista


lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
random.shuffle(lista)
print('Shuffle list:    ', lista)
print('Ascending Order: ', bubbleSort(lista))
print('Descending Order:', bubbleSort(lista, reverse=True))
