class Aresta:

	def __init__(self, pontoA, pontoB, peso):
		self.__pontoA = pontoA
		self.__pontoB = pontoB
		self.__peso = peso


	@property
	def pontoA(self):
		return self.__pontoA
		
	@property
	def pontoB(self):
		return self.__pontoB

	@property
	def peso(self):
		return self.__peso

	def __str__(self):
		return f'{self.__pontoA}-{self.__pontoB}: {self.__peso}'
