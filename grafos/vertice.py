class Vertice:

	def __init__(self, nome): # a inicialização recebe o nome do vertice como parametro
		self.__nome = nome

	@property
	def nome(self):
		return self.__nome

	def __str__(self):
		return self.__nome