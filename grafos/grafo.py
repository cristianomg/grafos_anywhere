from estruturas_de_dados import pilha, fila
from .aresta import Aresta
from .vertice import Vertice
import math


class Grafo:

    def __init__(self, direcionado=False):
        self.__lista_de_Vertices = []
        self.__lista_de_Arestas = []
        self.__lista_de_Adjacentes = {}
        self.__direcionado = direcionado
        self.__regular = False
        self.__completo = False
        self.pilha = None
        self.fila = None

    @property
    def vertices(self):
        """
        retorna uma lista contendo os vertices adicionados ao grafo.

        """
        return [vertice.__str__() for vertice in self.__lista_de_Vertices]

    @property
    def arestas(self):
        """
        retorna uma lista contendo uma tupla com os pontos de cada aresta adicionada ao Grafo.

        """
        return [aresta.__str__() for aresta in self.__lista_de_Arestas]

    @property
    def digrafo(self):
        '''
        Retorna True se for digrafo e False se não for digrafo.

        '''
        return self.__direcionado

    def representacao(self):
        for vertice, adjacentes in self.__lista_de_Adjacentes.items():
            print(f'Vertice: "{vertice}" - Adjacentes: "{adjacentes}"')

    def getAdjacentes(self, vertice):
        """
        Retorna a lista de adjacentes de um determinado vertice.

        Exemplo: grafo.adjacentes('v1') --- retorn [v2,v3].

        """
        return [i.__str__() for i in self.__lista_de_Adjacentes[vertice]]

    def adicionar_vertice(self, vertices):
        """
        adiciona os vertices no grafo.

        parametros: nome dos vertices --> 'v1','v2','v3' ...

        """
        self.__lista_de_Vertices = [Vertice(nome) for nome in vertices]
        self.__criar_lista_adjacentes()

    def adicionar_arestas(self, arestas, pesosArestas):
        """
        adiciona as arestas no grafo.

        parametros: Tupla com os vertices participantes ---> ('v1','v2'), ('v1','v3'), ('v2','v3').

        após adicionar as arestas ao grafo  chama a função __set_adjacentes()
        """
        self.__lista_de_Arestas = [Aresta(aresta[0], aresta[1], pesosArestas[pos]) for pos, aresta in
                                   enumerate(arestas)]
        self.__set_adjacentes()

    def __criar_lista_adjacentes(self):
        """
        Cria um dicionario onde a chave é um vertice e o valor instancia uma lista ligada.

        """
        for i in self.__lista_de_Vertices:
            self.__lista_de_Adjacentes[i.nome] = []

    def __set_adjacentes(self):
        """
        Seta as adjacencias na lista de adjacencias,  a partir das arestas adicionadas
        Para cada vertice do grafo será inserido, na lista ligada que foi instanciada na função __criar_lista_adjacentes,
        os seus respectivos vertices adjacentes.all

                                    -------- Exemplo --------
        Aresta(v1,v2)

        lista_de_adjacentes = {
            'v1': v2
            'v2': v1
        }

        """
        if not self.__direcionado:
            for aresta in self.__lista_de_Arestas:
                self.__lista_de_Adjacentes[aresta.pontoA].append(self.__select_vertice(aresta.pontoB))
                self.__lista_de_Adjacentes[aresta.pontoB].append(self.__select_vertice(aresta.pontoA))
        else:
            for aresta in self.__lista_de_Arestas:
                self.__lista_de_Adjacentes[aresta.pontoA].append(self.__select_vertice(aresta.pontoB))

    def __select_vertice(self, nome_vertice):
        """
        Seleciona um vertice da lista de vertices a partir do seu nome.

        parametro: Nome do Vertice
        Return: <grafos.vertice.Vertice object at 0x7f18966b2a90>
        """
        for vertice in self.__lista_de_Vertices:
            if vertice.nome == nome_vertice:
                return vertice
        else:
            return None

    def ehCompleto(self):
        """
        verifica se o grafo é completo
        caso o grafo seja completo  retorna True
        caso o grafo não seja completo retorna False

        """
        for vertice, adjacentes in self.__lista_de_Adjacentes.items():
            if len(adjacentes) == len(self.__lista_de_Vertices) - 1:
                self.__completo = True
            else:
                self.__completo = False
        return self.__completo

    def ehRegular(self):
        """
        Verifica se o grafo é regular.

        Caso seja regular retorna True.

        Caso não seja regular retorna False.

        """

        for v, adjacentes in self.__lista_de_Adjacentes.items():
            for i, j in self.__lista_de_Adjacentes.items():
                if len(adjacentes) == len(j):
                    self.__regular = True
                else:
                    self.__regular = False
                    return self.__regular
        return self.__regular

    def dfs(self, vertice):
        for i in self.__lista_de_Vertices:
            i.visitado = False
        result = []
        self.pilha = pilha.Pilha()
        vertice = self.__select_vertice(vertice)
        print(vertice)
        vertice.visitado = True
        self.pilha.empilhar(vertice)
        while self.pilha.tamanho != 0:
            vertice = self.pilha.desempilhar()
            vertice.visitado = True
            for i in range(len(self.__lista_de_Adjacentes[vertice.nome])):
                if not self.__lista_de_Adjacentes[vertice.nome][i].visitado:
                    if not self.pilha.contem(self.__lista_de_Adjacentes[vertice.nome][i]):
                        self.pilha.empilhar(self.__lista_de_Adjacentes[vertice.nome][i])
            if vertice.nome not in result:
                result.append(vertice.nome)
            print(self.pilha)
        return result

    def bfs(self, vertice):
        for i in self.__lista_de_Vertices:
            i.visitado = False
        result = []
        self.fila = fila.Fila()
        vertice = self.__select_vertice(vertice)
        vertice.visitado = True
        self.fila.enfilerar(vertice)
        while self.fila.tamanho > 0:
            v = self.fila.inicio
            for i in range(len(self.__lista_de_Adjacentes[v.nome])):
                if not self.__lista_de_Adjacentes[v.nome][i].visitado:
                    self.__lista_de_Adjacentes[v.nome][i].visitado = True
                    self.fila.enfilerar(self.__lista_de_Adjacentes[v.nome][i])
            print(self.fila)
            if v.nome not in result:
                result.append(v.nome)
            self.fila.desenfilerar()
        return result

    def ehConexo(self, algoritmo='bfs'):
        result_bool = False
        if algoritmo == 'bfs':
            result = self.bfs(self.__lista_de_Vertices[0].nome)
            vertices = [vertice.nome for vertice in self.__lista_de_Vertices]
            result_bool = False
            print(result)
            for i in vertices:
                if i in result:
                    result_bool = True
                else:
                    result_bool = False
        elif algoritmo == "dfs":
            result = self.dfs(self.__lista_de_Vertices[0].nome)
            vertices = [vertice.nome for vertice in self.__lista_de_Vertices]
            result_bool = False
            print(result)
            for i in vertices:
                if i in result:
                    result_bool = True
                else:
                    result_bool = False
        return result_bool

    def __select_arestas(self, pontoA, pontoB):
        for i in self.__lista_de_Arestas:
            if pontoA == i.pontoA and pontoB == i.pontoB:
                return i
            elif pontoB == i.pontoA and pontoA == i.pontoB:
                return i

    def dijkstra(self, vInicial, vFinal=None):
        s, dist, path = [], {}, {}
        for x in self.__lista_de_Vertices:
            dist.update({x.nome: math.inf})
            path.update({x.nome: None})
        self.fila = fila.Fila()
        s.append(vInicial)
        dist[vInicial], path[vInicial], vertice = 0, vInicial, self.__select_vertice(vInicial)
        self.fila.enfilerar(vertice)
        if vFinal == None:
            while self.fila.tamanho >= 1:
                v = self.fila.inicio
                for i in (self.__lista_de_Adjacentes[v.nome]):
                    aresta = self.__select_arestas(v.nome, i.nome)
                    if aresta.peso + dist[v.nome] < dist[i.nome]:
                        dist[i.nome] = aresta.peso + dist[v.nome]
                        path[i.nome] = v
                menor, elemento, adicionar= math.inf, "", False
                for i, j in dist.items():
                    if i not in s:
                        if j < menor:
                            menor, elemento, adicionar = j, i, True                        
                if adicionar:
                    s.append(elemento)
                    self.fila.enfilerar(self.__select_vertice(elemento))
                self.fila.desenfilerar()
        else:
            finalizar = False
            while self.fila.tamanho >= 1 and finalizar == False:
                v = self.fila.inicio
                for i in (self.__lista_de_Adjacentes[v.nome]):
                    aresta = self.__select_arestas(v.nome, i.nome)
                    if aresta.peso + dist[v.nome] < dist[i.nome]:
                        dist[i.nome] = aresta.peso + dist[v.nome]
                        path[i.nome] = v
                menor, elemento, adicionar = math.inf, "", False
                for i, j in dist.items():

                    if i not in s:
                        if j < menor:
                            menor, elemento, adicionar = j, i, True
                if adicionar:
                    s.append(elemento)
                    self.fila.enfilerar(self.__select_vertice(elemento))
                if s[len(s)-1] == vFinal:
                    finalizar = True
                self.fila.desenfilerar()
        self.__imprimirTabelaMenorCaminho(s, dist, path)

    def __imprimirTabelaMenorCaminho(self, s, dist, path):
        print("{:<10}{:<10}{:<10}".format("Vertices", "Distancia", "Caminho"))
        for i in s:
            print("{:^10}{:^10}{:^10}".format(i, dist[i], str(path[i])))
