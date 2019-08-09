from listas import lista_duplamente_ligada
class Pilha:
	def __init__(self):
		self.__elementos = lista_duplamente_ligada.ListaDuplamenteLigada()

	@property
	def tamanho(self):
		return self.__elementos.tamanho

	def empilhar(self, elemento):
		self.__elementos.inserir(elemento)

	def desempilhar(self):
		if self.__elementos.tamanho >= 1:
			elemento = self.__elementos.recuperar_elemento_no(self.__elementos.tamanho-1)
			self.__elementos.remover_pos(self.__elementos.tamanho-1)
			return elemento
		else:
			return None

	def __str__(self):
		return self.__elementos.__str__()