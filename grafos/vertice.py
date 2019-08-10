class Vertice:

	def __init__(self, nome):
		self.__nome = nome
		self.__visitado = False

	@property
	def nome(self):
		return self.__nome
	
	@property
	def visitado(self):
		return self.__visitado

	@visitado.setter
	def visitado(self, booleano):
		self.__visitado = booleano

	def __str__(self):
		return self.__nome

	def __repr__(self):
		return self.__str__()

