from estruturas_de_dados import pilha
from grafos.vertice import Vertice


class Dfs:

    def init(self, lista_vertices, lista_adjacentes):
        self.vertices = lista_vertices
        self.lista_adjacentes = lista_adjacentes
        self.conexo = None
        self.pilha = pilha.Pilha()
        for vertice in self.vertices:
            vertice.visitado = False

    def buscar(self, vertice_inicio):
        self.pilha.empilhar(vertice_inicio)
        while self.pilha.tamanho != 0:
            vertice = self.pilha.desempilhar()
            vertice_inicio.visitado = True
            adjacentes = self.lista_adjacentes[vertice.nome]
            for i in range(adjacentes.tamanho):
				adjacente = adjacentes.recuperar_no_posição(i)
				if not adjacente.visitado:
            		self.pilha.empilhar(adjacente)

