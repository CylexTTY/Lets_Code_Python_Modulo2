def buscaLinear(lista: list, elemento: float or int):
    """
    Busca linearmente um elemento em uma lista e retorna o seu(s) índice(s).
    Se não achar, retorna None.
    """
    return tuple(i for i, el in enumerate(lista) if el == elemento) or None


lista = [1, 2, 3, 4, 3, 5]
print(buscaLinear(lista, 3))
print(buscaLinear(lista, 6))
