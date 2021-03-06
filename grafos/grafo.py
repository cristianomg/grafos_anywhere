from .vertice import Vertice
from .aresta import Aresta
from estruturas_de_dados import pilha, fila
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
        for adjacentes in self.__lista_de_Adjacentes.values():
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

        for adjacentes in self.__lista_de_Adjacentes.values():
            for j in self.__lista_de_Adjacentes.values():
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
        pilhaPais = pilha.Pilha()
        self.pilha = pilha.Pilha()
        vertice = self.__select_vertice(vertice)
        print(vertice)
        vertice.visitado = True
        self.pilha.empilhar(vertice)
        posicaoVisitado = 0
        while self.pilha.tamanho != 0:
            vertice = self.pilha.desempilhar()
            vertice.visitado = True
            for i in range(len(self.__lista_de_Adjacentes[vertice.nome])):
                if not self.__lista_de_Adjacentes[vertice.nome][i].visitado:
                    if not self.pilha.contem(self.__lista_de_Adjacentes[vertice.nome][i]):
                        self.pilha.empilhar(self.__lista_de_Adjacentes[vertice.nome][i])
            if vertice.nome not in result:
                pai = pilhaPais.top()
                while pai != None:
                    pai = pilhaPais.top()
                    if pai != None:
                        if len(list(filter(lambda x: x.pontoA == pai.nome and x.pontoB == vertice.nome,
                        self.__lista_de_Arestas))) > 0:
                            vertice.pai = pai
                            break
                        else:
                            pai = pilhaPais.desempilhar()
                print(self.pilha)
                pilhaPais.empilhar(vertice)
                vertice.posicaoVisitado = posicaoVisitado
                result.append(vertice)
            posicaoVisitado += 1
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
                result.append(v)
            self.fila.desenfilerar()
        return result

    def ehConexo(self, algoritmo='bfs'):
        result_bool = False
        if algoritmo == 'bfs':
            result = self.bfs(self.__lista_de_Vertices[0].nome)
            result_bool = False
            print(result)
            for i in self.__lista_de_Vertices:
                if i in result:
                    result_bool = True
                else:
                    result_bool = False
        elif algoritmo == "dfs":
            result = self.dfs(self.__lista_de_Vertices[0].nome)
            result_bool = False
            print(result)
            for i in self.__lista_de_Vertices:
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
            x.visitado = False
            dist.update({x.nome: math.inf})
            path.update({x.nome: None})
        self.fila = fila.Fila()
        s.append(vInicial)
        dist[vInicial], path[vInicial], vertice = 0, vInicial, self.__select_vertice(vInicial)
        vertice.visitado = True
        self.fila.enfilerar(vertice)
        if vFinal == None:
            while self.fila.tamanho >= 1:
                v = self.fila.inicio
                for i in (self.__lista_de_Adjacentes[v.nome]):
                    aresta = self.__select_arestas(v.nome, i.nome)
                    if aresta.peso + dist[v.nome] < dist[i.nome]:
                        dist[i.nome] = aresta.peso + dist[v.nome]
                        path[i.nome] = v
                menor, elemento = math.inf, ""
                for i, j in dist.items():
                    adicionar = False
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
                menor, elemento = math.inf, ""
                for i, j in dist.items():
                    adicionar = False
                    if i not in s:
                        if j < menor:
                            menor, elemento, adicionar = j, i, True
                    if adicionar:
                        s.append(elemento)
                        self.fila.enfilerar(self.__select_vertice(elemento))
                    if elemento == vFinal:
                        finalizar = True
                self.fila.desenfilerar()
        self.__imprimirTabelaMenorCaminho(s, dist, path)

    def __imprimirTabelaMenorCaminho(self, s, dist, path):
        print("{:<10}{:<10}{:<10}".format("Vertices", "Distancia", "Caminho"))
        for i in s:
            print("{:^10}{:^10}{:^10}".format(i, dist[i], str(path[i])))


    #retorna a lista de arestas após a remoção do vertice de grau 0
    def getListaVerticesRestantes(self, listaVertice ,listaArestas):
        dic = {}
        for vertice in listaVertice:
            grauEntrada = vertice.getGrauEntrada(listaArestas)
            dic[vertice.nome] = grauEntrada
        lista = [self.__select_vertice(x) for x in sorted(dic, key = dic.get)]
        return lista

    #necessita de um grafo direcionado 
    #ordena o grafo de acordo com as dependencias
    def ordenacaoTopologica (self):
        result = []
        listaArestas = self.__lista_de_Arestas.copy()
        listaVertice = self.__lista_de_Vertices.copy()
        for vertice in self.__lista_de_Vertices:
            listaVertice = self.getListaVerticesRestantes(listaVertice,listaArestas)
            if len(listaVertice) >= 1:
                listaArestas = list(filter(lambda x: x.pontoA != listaVertice[0].nome, listaArestas))
                result.append(listaVertice[0].nome)
                listaVertice.remove(listaVertice[0])
            else:
                break
        print('{}'.format(' '.join(result)))

    #retorna as arestas da arvore geradora minima
    #necessita um grafo em forma de arvore
    def arvoreGeradoraMinima(self):
        conjuntoB = [self.__lista_de_Vertices[0].nome]
        arvore = []
        while True:
            menor = float('inf')
            aresta = None
            for x in self.__lista_de_Arestas:
                if (x.pontoA in conjuntoB and x.pontoB not in conjuntoB) or (x.pontoB in conjuntoB and x.pontoA not in conjuntoB):
                    if x.peso < menor:
                        aresta = x
                        menor = x.peso
            if (aresta.pontoA not in conjuntoB):
                 conjuntoB.append(aresta.pontoA)
                 arvore.append(aresta)
            else:
                conjuntoB.append(aresta.pontoB)
                arvore.append(aresta)
            if (len(conjuntoB) == len(self.__lista_de_Vertices)):
                break
        return arvore
    

    def buscaPorArticulacao(self):
        articulacao = []
        result = self.dfs(self.__lista_de_Vertices[0].nome)
        print(result)
        for vertice in result:
            if vertice.pai == None:
                filhos = list(filter(lambda x: x.pai == vertice, result))
                if len(filhos) > 1:
                    for filho in filhos:
                        if list(filter(lambda x: x.pontoB == filho, self.__lista_de_Arestas)) == 1:
                            articulacao.append(vertice)
                            break
            elif len(list(filter(lambda x: x.pai == vertice, result))) > 0:
                ancestrais = list(filter(lambda x: x.posicaoVisitado < vertice.posicaoVisitado, result))
                descendentes = list(filter(lambda x: x.posicaoVisitado > vertice.posicaoVisitado, result))
                descendentes = list(filter(lambda x: x.pai.posicaoVisitado >= vertice.posicaoVisitado, descendentes ))
                for ancestral in ancestrais:
                    for descendente in descendentes:
                        aresta = list(filter(lambda x: x.pontoA == ancestral.nome and
                         x.pontoB == descendente.nome, self.__lista_de_Arestas))
                        if len(aresta) == 0:
                            if vertice not in articulacao:
                                articulacao.append(vertice)
        print("Articulações:", end=" ")
        print(articulacao)