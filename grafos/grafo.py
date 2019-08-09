from .aresta import Aresta
from .vertice import Vertice
from estruturas_de_dados import lista_ligada

class Grafo:

	def __init__(self, direcionado=False):
		self.__lista_de_Vertices = []
		self.__lista_de_Arestas = []
		self.__lista_de_Adjacentes = {}
		self.__direcionado = direcionado
		self.__regular = False
		self.__completo = False

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

	def adjacentes(self, vertice):
		"""
		Retorna a lista de adjacentes de um determinado vertice.

		Exemplo: grafo.adjacentes('v1') --- retorn [v2,v3].

		"""
		return self.__lista_de_Adjacentes[vertice]

	def adicionar_vertice(self, vertices): 
		"""
		adiciona os vertices no grafo.

		parametros: nome dos vertices --> 'v1','v2','v3' ... 
		
		"""
		self.__lista_de_Vertices = [Vertice(nome) for nome in vertices]
		self.__criar_lista_adjacentes()
	
	def adicionar_arestas(self, arestas):
		"""		
		adiciona as arestas no grafo.
		
		parametros: Tupla com os vertices participantes ---> ('v1','v2'), ('v1','v3'), ('v2','v3').
		
		após adicionar as arestas ao grafo  chama a função __set_adjacentes()
		"""
		self.__lista_de_Arestas = [Aresta(aresta[0], aresta[1]) for aresta in arestas]
		self.__set_adjacentes()

	def __criar_lista_adjacentes(self):
		"""
		Cria um dicionario onde a chave é um vertice e o valor instancia uma lista ligada.

		"""
		for i in self.__lista_de_Vertices:
			self.__lista_de_Adjacentes[i.nome] = lista_ligada.ListaLigada()

	def __set_adjacentes(self):
		"""
		Seta as adjacencias na lista de adjacencias,  a partir das arestas adicionadas
		Para cada vertice do grafo será inserido, na lista ligada que foi instanciada na função __criar_lista_adjacentes, os seus respectivos vertices adjacentes.all

		                           -------- Exemplo --------
		Aresta(v1,v2)

		lista_de_adjacentes = {
			'v1': v2
			'v2': v1
		}		

		"""
		if self.__direcionado == False:
			for aresta in self.__lista_de_Arestas:
				self.__lista_de_Adjacentes[aresta.pontoA].inserir(self.__select_vertice(aresta.pontoB))
				self.__lista_de_Adjacentes[aresta.pontoB].inserir(self.__select_vertice(aresta.pontoA))
			#print(type(self.__lista_de_Adjacentes['v1'].recuperar_elemento_no(0))) # teste
		else:
			for aresta in self.__lista_de_Arestas:
				self.__lista_de_Adjacentes[aresta.pontoA].inserir(self.__select_vertice(aresta.pontoB))

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
			if adjacentes.tamanho == len(self.vertices)-1:
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
				if adjacentes.tamanho == j.tamanho:
					self.__regular = True
				else:
					self.__regular = False
					return self.__regular
		return self.__regular
