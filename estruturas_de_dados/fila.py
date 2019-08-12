from estruturas_de_dados import lista_ligada


class Fila:

	def __init__(self):
		self.__elementos = lista_ligada.ListaLigada()

	@property
	def tamanho(self):
		return self.__elementos.tamanho

	@property
	def inicio(self):
		return self.__elementos.recuperar_elemento_no(0)

	def enfilerar(self, elemento):
		self.__elementos.inserir(elemento)

	def desenfilerar(self):
		if self.__elementos.tamanho >= 1:
			elemento = self.__elementos.recuperar_elemento_no(0)
			self.__elementos.remover_pos(0)
			return elemento
		else:
			return None

	def contem(self, elemento):
		return self.__elementos.contem(elemento)

	def __str__(self):
		return self.__elementos.__str__()
