# Para esse projeto nós criaremos uma rede social baseada no Instagram onde
# teremos um grafo direcionado, já que posso seguir alguém que não me segue.
# Além disso, teremos conexões que serão melhores amigos e outras que serão
# conexão comuns. Logo, teremos um grafo direcionado e ponderado.
# O objetivo será criar algumas funções relacionadas ao grafo e a rede social:
import csv


class GrafoInsta(object):

    def __init__(self):
        self.rede_instagram = {}

    def add_user(self, username):
        # Verificar se deixa assim ou simplifica
        self.rede_instagram[username] = {}

    def usuario_existe(self, usuario):
        existe = usuario in self.rede_instagram.keys()
        if not existe:
            print('\033[31mUsuario não existe!\033[m')
        return existe

    def connect_user(self, usuario, username_amigo, tipo_amizade):
        """
        Conecta usuarios no grafo
        :param usuario: Username do usuario
        :param username_amigo: Username do amigo
        :param tipo_amizade: 1 se amigo, 2 se melhor amigo
        """
        if self.usuario_existe(usuario) and self.usuario_existe(
                username_amigo):
            self.rede_instagram[usuario][username_amigo] = tipo_amizade

    # 1- Exibir número de seguidores
    def exibir_numero_seguidores(self, username_do_usuario):
        if self.usuario_existe(username_do_usuario):
            qnt_seguidores = 0
            for username, seguindo in self.rede_instagram.items():
                if username != username_do_usuario:
                    for nick in seguindo.keys():
                        if nick == username_do_usuario:
                            qnt_seguidores += 1
            return qnt_seguidores

    # 2- Exibir quantidades de pessoas que o usuário segue
    def exibir_numero_seguindo(self, username_do_usuario):
        if self.usuario_existe(username_do_usuario):
            return len(self.rede_instagram[username_do_usuario])

    # 3- Ordenar a lista de Stories, ou seja, melhores amigos primeiro e depois
    # conexões comuns ordenadas por ordem alfabética ->
    # [melhores amigos em ordem alfabetica , amigos em ordem alfabetica]
    def ordenar_stories(self, username_do_usuario):
        if self.usuario_existe(username_do_usuario):
            melhores_amigos = []
            amigos_comuns = []
            for amigo_tipo in self.rede_instagram[username_do_usuario].items():
                if amigo_tipo[1] == str(2):
                    melhores_amigos.append(amigo_tipo[0])
                else:
                    amigos_comuns.append(amigo_tipo[0])
        return self.ordenar_lista(melhores_amigos) + self.ordenar_lista(amigos_comuns)

    def ordenar_lista(self, lista):

        def merge(lista):
            if len(lista) > 1:
                meio = len(lista) // 2
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
                elif lista_esquerda[ponteiro_esquerdo] >= lista_direita[
                    ponteiro_direito]:
                    lista[i] = lista_direita[ponteiro_direito]
                    ponteiro_direito += 1
                # Se o elemento do ponteiro direito for maior ou igual ao do ponteiro esquerdo
                else:
                    lista[i] = lista_esquerda[ponteiro_esquerdo]
                    ponteiro_esquerdo += 1
            return lista

        return merge(lista)

    # 4- Encontrar top k influencers, ou seja, k pessoas que mais tem seguidores
    # da rede
    def ordenar_top_influencers(self, k):
        # Desafio: encontrar maiores vertices adjacentes esse usuario.
        if len(self.rede_instagram) >= k > 0:
            pessoas_seguidores = {pessoa: self.exibir_numero_seguidores(pessoa)
                                  for pessoa in self.rede_instagram.keys()}
            return self.ordenar_dicionario_reverse(pessoas_seguidores)[:k]
        return f'\033[31mNúmero {k} inválido\n' \
               f'Necessário numero de 1 a {len(self.rede_instagram)}\033[m'

    def ordenar_dicionario_reverse(self, dicionario):
        # Considerando que a lista sera retornada na ordem decrescente
        def bubbleSort(dicionario):
            ordered = False
            i = 0
            dicionario = list(tuple(dicionario.items()))
            while not ordered:
                ordered = True
                for j in range(len(dicionario) - i - 1):
                    # Comparando o menor valor e colocando na frente (final da lista)
                    if dicionario[j][1] < dicionario[j + 1][1]:
                        dicionario[j], dicionario[j + 1] = dicionario[j + 1], dicionario[j]
                        ordered = False
                i += 1
            return list(dict(dicionario).keys())

        return bubbleSort(dicionario)

    # 5- Encontrar o caminho entre uma pessoa e outra na rede
    def encontrar_caminho(self, usu_origem, usu_destino):
        if self.usuario_existe(usu_origem) and self.usuario_existe(usu_destino):
            fila = [usu_origem]
            visitados = []
            predecessor = {usu_origem: None}
            # Enquanto a fila não estiver vazia:
            while fila:
                primeiro_elemento = fila.pop(0)
                visitados.append(primeiro_elemento)
                for nos_adjacentes in self.rede_instagram[primeiro_elemento].keys():
                    # Se achar, montar caminho
                    if nos_adjacentes == usu_destino:
                        pred = primeiro_elemento
                        caminho_invertido = [usu_destino]
                        while pred is not None:
                            caminho_invertido.append(pred)
                            pred = predecessor[pred]
                        return ' -> '.join(caminho_invertido[::-1])
                    if nos_adjacentes not in visitados and nos_adjacentes not in fila:
                        predecessor[nos_adjacentes] = primeiro_elemento
                        fila.append(nos_adjacentes)
            return f'\033[31mUsuario {usu_origem} não tem ligação com {usu_destino}'


def obter_nickname(arquivo):
    with open(arquivo, encoding='utf-8', mode='r') as users:
        leitura = csv.reader(users)
        usuarios = [nickname[1] for nickname in leitura]
    return usuarios


def adicionar_usuarios(arquivo):
    users = obter_nickname(arquivo)
    grafo = GrafoInsta()
    for user in users:
        grafo.add_user(user)
    return grafo


def obter_conexoes(arquivo):
    with open(arquivo, encoding='utf-8', mode='r') as conexoes:
        leitura = csv.reader(conexoes)
        lista_conexoes = [conexao_peso for conexao_peso in leitura]
    return lista_conexoes


def adicionar_conexoes(grafo, arquivo):
    # Conexos será uma lista de tuplas como:
    # (usuario, amigo, peso(1-amigo, 2-melhor amigo)
    conexoes = obter_conexoes(arquivo)
    for conexao in conexoes:
        grafo.connect_user(usuario=conexao[0], username_amigo=conexao[1],
                           tipo_amizade=conexao[2])
    print('\033[32mUsuarios conectados com sucesso\033[m')


instagram = adicionar_usuarios('usuarios.csv')
adicionar_conexoes(instagram, 'conexoes.csv')
print(instagram.rede_instagram['maria_helena6'])
print(instagram.exibir_numero_seguidores('samuel45'))
print(instagram.exibir_numero_seguindo('maria_helena6'))
print(instagram.ordenar_stories('maria_helena6'))
print(instagram.ordenar_top_influencers(10))
for pessoa in instagram.rede_instagram.keys():
    print(instagram.encontrar_caminho('maria_helena6', pessoa))
