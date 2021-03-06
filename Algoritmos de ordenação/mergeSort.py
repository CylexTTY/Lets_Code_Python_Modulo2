import random


# def merge(lista):
#     if len(lista) > 1:
#         meio = len(lista) // 2
#         lista = sort(lista, merge(lista[:meio]), merge(lista[meio:]))
#     return lista
#
#
# def sort(lista, lista_esquerda, lista_direita):
#     ponteiro_esquerdo = ponteiro_direito = 0
#
#     for i in range(len(lista_esquerda) + len(lista_direita)):
#         # Se o ponteiro esquerdo estourar
#         if ponteiro_esquerdo >= len(lista_esquerda):
#             lista[i] = lista_direita[ponteiro_direito]
#             ponteiro_direito += 1
#         # Se o ponteiro direito estourar
#         elif ponteiro_direito >= len(lista_direita):
#             lista[i] = lista_esquerda[ponteiro_esquerdo]
#             ponteiro_esquerdo += 1
#         # Se o elemento do ponteiro esquerdo for maior ou igual ao do ponteiro direito
#         elif lista_esquerda[ponteiro_esquerdo] >= lista_direita[ponteiro_direito]:
#             lista[i] = lista_direita[ponteiro_direito]
#             ponteiro_direito += 1
#         # Se o elemento do ponteiro direito for maior ou igual ao do ponteiro esquerdo
#         else:
#             lista[i] = lista_esquerda[ponteiro_esquerdo]
#             ponteiro_esquerdo += 1
#     return lista
# More fast:
def merge(lista):
    return _merge(lista, 0, len(lista))


def _merge(lista, ini, fim):
    if fim - ini > 1:
        meio = (ini + fim) // 2

        # Esquerda
        _merge(lista, ini, meio)

        # Direita
        _merge(lista, meio, fim)

        # Ordenar
        sort(lista, ini, meio, fim)
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
        # Se o ponteiro esquerdo for maior ou igual ao ponteiro direito da lista principal,
        # colocar o elemento do ponteiro direito na pr??xima posi????o e ponteiro direito avan??a.
        elif lista_esquerda[ponteiro_esquerdo] >= lista_direita[ponteiro_direito]:
            lista[i] = lista_direita[ponteiro_direito]
            ponteiro_direito += 1
        # Se o ponteiro direito for maior ou igual ao ponteiro esquerdo da lista principal,
        # colocar o elemento do ponteiro esquerdo na pr??xima posi????o e ponteiro esquerdo avan??a.
        else:
            lista[i] = lista_esquerda[ponteiro_esquerdo]
            ponteiro_esquerdo += 1


lista = [n for n in range(1, 1_000_001)]
random.shuffle(lista)
print('Shuffle list:', lista)
print('Ordered list:', merge(lista))
