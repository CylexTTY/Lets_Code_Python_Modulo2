# Para esse projeto nós criaremos uma rede social baseada no Instagram onde
# teremos um grafo direcionado, já que posso seguir alguém que não me segue.
# Além disso, teremos conexões que serão melhores amigos e outras que serão
# conexão comuns. Logo, teremos um grafo direcionado e ponderado.
# O objetivo será criar algumas funções relacionadas ao grafo e a rede social:
import csv
from collections import deque, defaultdict
from itertools import islice


class GrafoInsta(object):

    def __init__(self):
        self.rede_instagram = {}

    def add_user(self, username_usuario: str):
        self.rede_instagram[username_usuario] = {}

    def connect_user(self, username_usuario: str, username_amigo: str, tipo_amizade: int):
        """
        Conecta usuários no grafo
        :param username_usuario: Username do usuário
        :param username_amigo: Username do amigo
        :param tipo_amizade: 1 se amigo, 2 se melhor amigo
        """
        if self.usuario_existe(username_usuario) and self.usuario_existe(username_amigo):
            self.rede_instagram[username_usuario][username_amigo] = tipo_amizade

    def usuario_existe(self, username_usuario: str) -> bool:
        existe = username_usuario in self.rede_instagram.keys()
        if not existe:
            print('\033[31mUsuario não existe!\033[m')
        return existe

    # 1- Exibir número de seguidores
    def exibir_numero_seguidores(self, username_usuario: str) -> str | int:
        if self.usuario_existe(username_usuario):
            qnt_seguidores = self.contar_seguidores()[username_usuario]
            return f'@{username_usuario} é seguido(a) por {qnt_seguidores} seguidores.'

    def contar_seguidores(self):
        contador = defaultdict(int)
        for usuario in self.rede_instagram.values():
            for seguindo in usuario.keys():
                contador[seguindo] += 1
        return contador

    # 2- Exibir quantidades de pessoas que o usuário segue
    def exibir_numero_seguindo(self, username_usuario: str) -> str:
        if self.usuario_existe(username_usuario):
            return f'@{username_usuario} segue {len(self.rede_instagram[username_usuario])} amigos.'

    # 3- Ordenar a lista de Stories, ou seja, melhores amigos primeiro e depois conexões comuns
    # ordenadas por ordem alfabética -> [melhores amigos em ordem alfabética , amigos em ordem alfabética]
    def ordenar_stories(self, username_usuario: str) -> str:
        if self.usuario_existe(username_usuario):
            tipos = {}
            melhores_amigos = deque()
            amigos_comuns = deque()
            for amigo, tipo in self.rede_instagram[username_usuario].items():
                tipos.setdefault(tipo, []).append(amigo)
                if tipo == str(2):
                    melhores_amigos.append(amigo)
                else:
                    amigos_comuns.append(amigo)
            return f'@{username_usuario} - Amizades:\n' \
                   f'Melhores amigos: {"@" + " | @".join(self.ordenar_lista(melhores_amigos))}\n' \
                   f'Amigos comuns: {"@" + " | @".join(self.ordenar_lista(amigos_comuns))}'

    def ordenar_lista(self, lista: deque) -> deque:
        # Ordenado uma lista de strings de forma alfabética e crescente com merge sort
        tamanho_lista = len(lista)
        if tamanho_lista > 1:
            meio = tamanho_lista // 2
            esquerda = deque(islice(lista, 0, meio))
            direita = deque(islice(lista, meio, tamanho_lista))
            self.merge_sort(lista, self.ordenar_lista(esquerda), self.ordenar_lista(direita))
        return lista

    def merge_sort(self, lista: deque, lista_esquerda: deque, lista_direita: deque) -> deque:
        ponteiro_esquerdo = ponteiro_direito = 0

        for i in range(len(lista_esquerda) + len(lista_direita)):
            # Se o ponteiro esquerdo estourar OU
            # o ponteiro direito nao estourar E o elemento do ponteiro esquerdo >= elemento do ponteiro direito.
            # Lista recebe elemento direito e ponteiro direito avanca.
            if (
                ponteiro_esquerdo >= len(lista_esquerda)
                or (ponteiro_direito < len(lista_direita)
                    and lista_esquerda[ponteiro_esquerdo] >= lista_direita[ponteiro_direito])
            ):
                lista[i] = lista_direita[ponteiro_direito]
                ponteiro_direito += 1
            # Caso contrário, podemos considerar que o ponteiro direito estourou ou
            # elemento do ponteiro direito >= elemento do ponteiro esquerdo;
            # Portanto lista recebe elemento do ponteiro esquerdo e ponteiro esquerdo avança.
            else:
                lista[i] = lista_esquerda[ponteiro_esquerdo]
                ponteiro_esquerdo += 1
        return lista

    # 4- Encontrar top k influencers, ou seja, k pessoas que mais tem seguidores
    # da rede
    def ordenar_top_influencers(self, k: int) -> str:
        # Desafio: encontrar maiores vertices adjacentes a esse usuário.
        if k > 0:
            # Se o K for maior do que o limite de usuários do grafo, limita-se ao número de usuários
            k = min(len(self.rede_instagram.keys()), k)
            # Coletando o número de seguidores de cada usuário
            pessoas_seguidores = self.contar_seguidores()
            # Obtendo uma lista ordenada decrescente dos top influencers
            top_k_influencers = self.ordenar_dicionario_reverse(pessoas_seguidores, k)
            # Organizando visualmente os top influencers como string
            top_k_influencers = ''.join(f'\n{i + 1}º ' + f'{"@" + user_name}'
                                        for i, user_name in enumerate(top_k_influencers))
            return f'Top {k} influencers:{top_k_influencers}'

        return f'\033[31mNúmero {k} inválido\n' \
               f'Necessário numero de 1 a {len(self.rede_instagram)}\033[m'

    def ordenar_dicionario_reverse(self, dicionario: dict, qnt_influencers: int) -> deque:
        # Considerando que a lista será retornada na ordem decrescente sempre.
        # Usando o bubble sort com condição de parada.
        nomes_qntSeguidores = deque(dicionario.items())

        for i in range(qnt_influencers):
            for j in range(len(nomes_qntSeguidores)-1, 0+i, -1):
                # Comparando o maior valor e colocando no começo da lista
                if nomes_qntSeguidores[j][1] > nomes_qntSeguidores[j - 1][1]:
                    nomes_qntSeguidores[j], nomes_qntSeguidores[j - 1] = nomes_qntSeguidores[j - 1], nomes_qntSeguidores[j]
        # Fazendo um slice em um deque, obtendo os primeiros "k" influencers.
        top_influencers = islice(nomes_qntSeguidores, 0, qnt_influencers)
        return deque(nome for nome, qnt_seguidores in top_influencers)

    # 5- Encontrar o caminho entre uma pessoa e outra na rede
    def encontrar_caminho(self, usu_origem: str, usu_destino: str) -> str:
        # Usando BFS - Busca em Largura
        if self.usuario_existe(usu_origem) and self.usuario_existe(usu_destino):
            fila = deque([usu_origem])
            visitados = deque()
            predecessor = {usu_origem: None}
            # Enquanto a fila não estiver vazia:
            while fila:
                primeiro_elemento = fila.popleft()
                visitados.append(primeiro_elemento)
                for nos_adjacentes in self.rede_instagram[primeiro_elemento].keys():
                    # Se achar, montar caminho
                    if nos_adjacentes == usu_destino:
                        pred = primeiro_elemento
                        caminho_ordenado = [usu_destino]
                        while pred is not None:
                            # Colocando já na ordem correta ao invés de 'appendar' e inverter.
                            caminho_ordenado.insert(0, pred)
                            pred = predecessor[pred]
                        return '@' + ' -> @'.join(caminho_ordenado)
                    if nos_adjacentes not in visitados and nos_adjacentes not in fila:
                        predecessor[nos_adjacentes] = primeiro_elemento
                        fila.append(nos_adjacentes)
            return f'\033[31mUsuario {usu_origem} não tem ligação com {usu_destino}'


def obter_nickname(arquivo: str) -> list:
    with open(arquivo, encoding='utf-8', mode='r') as users:
        leitura = csv.reader(users)
        usuarios = [nickname[1] for nickname in leitura]
    return usuarios


def adicionar_usuarios(arquivo: str) -> object:
    users = obter_nickname(arquivo)
    grafo = GrafoInsta()
    for user in users:
        grafo.add_user(user)
    return grafo


def obter_conexoes(arquivo: str) -> list:
    with open(arquivo, encoding='utf-8', mode='r') as conexoes:
        leitura = csv.reader(conexoes)
        lista_conexoes = [conexao_peso for conexao_peso in leitura]
    return lista_conexoes


def adicionar_conexoes(grafo: object, arquivo: str):
    # Conexões será uma lista de tuplas com 3 elementos cada como:
    # (nome de usuário, nome de usuário do amigo, peso(1-amigo, 2-melhor_amigo))
    conexoes = obter_conexoes(arquivo)
    for conexao in conexoes:
        grafo.connect_user(username_usuario=conexao[0], username_amigo=conexao[1],
                           tipo_amizade=conexao[2])
    print('\033[32mUsuarios conectados com sucesso\033[m')


instagram = adicionar_usuarios('usuarios.csv')
adicionar_conexoes(instagram, 'conexoes.csv')
print(instagram.exibir_numero_seguidores('helena42'))
print(instagram.exibir_numero_seguindo('helena42'))
print(instagram.ordenar_stories('helena42'))
print(instagram.ordenar_top_influencers(6))
print(instagram.encontrar_caminho('helena42', 'isadora45'))
# print(instagram.rede_instagram['maria_helena6'])
# print(instagram.exibir_numero_seguidores('samuel45'))
# print(instagram.exibir_numero_seguindo('maria_helena6'))
# print(instagram.ordenar_stories('maria_helena6'))
# print(instagram.ordenar_top_influencers(15))
# for pessoa in instagram.rede_instagram.keys():
#     print(instagram.encontrar_caminho('maria_helena6', pessoa))
