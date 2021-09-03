def buscaBinaria(lista: list, el: float or int):
    """
    Se espera que a lista já esteja ordenada, então busca se o elemento está ou
    não na lista.
    :param lista: lista de numeros ordenados
    :param el: Elemento da busca
    :return: True se existe / False se não existe
    """
    if lista:
        if len(lista) == 1:
            return lista[0] == el

        meio = len(lista) // 2

        if lista[meio] == el:
            return True
        elif lista[meio] > el:
            return buscaBinaria(lista[:meio], el)
        else:
            return buscaBinaria(lista[meio+1:], el)
    return False

lista = [1, 2, 3, 4, 5]
print(buscaBinaria(lista, 2))
print(buscaBinaria(lista, 6))
print(buscaBinaria([], 0))