import random


def merge(lista):
    if len(lista) > 1:
        meio = len(lista) // 2
        #            Lista         Esquerda    |        Direita
        lista = sort(lista, merge(lista[:meio]), merge(lista[meio:]))
    return lista


def sort(lista, lista_esquerda, lista_direita):
    ponteiro_esquerdo = ponteiro_direito = 0

    for i in range(len(lista_esquerda) + len(lista_direita)):
        # Se o ponteiro esquerdo estourar
        if ponteiro_esquerdo >= len(lista_esquerda):
            lista[i] = lista_direita[ponteiro_direito]
            ponteiro_direito += 1
        # Se o ponteiro direito estourar
        elif ponteiro_direito >= len(lista_direita):
            lista[i] = lista_esquerda[ponteiro_esquerdo]
            ponteiro_esquerdo += 1
        # Se o elemento do ponteiro esquerdo for maior ou igual ao do ponteiro direito
        elif lista_esquerda[ponteiro_esquerdo] >= lista_direita[ponteiro_direito]:
            lista[i] = lista_direita[ponteiro_direito]
            ponteiro_direito += 1
        # Se o elemento do ponteiro direito for maior ou igual ao do ponteiro esquerdo
        else:
            lista[i] = lista_esquerda[ponteiro_esquerdo]
            ponteiro_esquerdo += 1
    return lista


lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
random.shuffle(lista)
print('Shuffle list:', lista)
print('Ordered list:', merge(lista))
