class No:
	def __init__(self, elemento, proximo=None):
		self.__elemento = elemento
		self.__proximo = proximo

	@property
	def elemento(self):
		return self.__elemento

	@elemento.setter
	def elemento(self, elemento):
		self.__elemento = elemento
	
	@property
	def proximo(self):
		return self.__proximo

	@proximo.setter
	def proximo(self, proximo):
		self.__proximo = proximo