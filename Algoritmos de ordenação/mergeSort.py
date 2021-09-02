import random


def merge(lista, ini, fim):
    if fim - ini > 1:
        meio = (ini + fim) // 2
        # Esquerda
        merge(lista, ini, meio)
        # Direita
        merge(lista, meio, fim)
        # Ordenar
        lista = sort(lista, ini, meio, fim)
    return lista


def sort(lista, ini, meio, fim):
    lista_esquerda = lista[ini:meio]
    lista_direita = lista[meio:fim]

    ponteiro_esquerdo = 0
    ponteiro_direito = 0

    for i in range(ini, fim):
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
print('Ordered list:', merge(lista, ini=0, fim=len(lista)))
