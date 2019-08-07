class Aresta:

	def __init__(self, pontoA, pontoB): # a inicialização recebe os pontos adjacentes como parametros
		self.__pontoA = pontoA
		self.__pontoB = pontoB


	@property
	def pontoA(self):
		return self.__pontoA
		
	@property
	def pontoB(self):
		return self.__pontoB

	def __str__(self):
		return f'{self.__pontoA}-{self.__pontoB}'