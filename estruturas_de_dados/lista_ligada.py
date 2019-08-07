from .no import No

class ListaLigada:
	def __init__(self):
		self.__primeiro_no = None
		self.__ultimo_no = None
		self.__tamanho = 0

	@property
	def tamanho(self):
		return self.__tamanho

	def __str__(self):
		no = self.__primeiro_no
		elementos = ''
		for i in range(self.__tamanho):
			elementos = f'{elementos}{no.elemento} '
			no = no.proximo
		return elementos

	def inserir(self, elemento):
		novo_no = No(elemento)
		if self.__primeiro_no == None:
			self.__primeiro_no = novo_no
			self.__ultimo_no = novo_no
		else:
			self.__ultimo_no.proximo = novo_no
			self.__ultimo_no = novo_no
		self.__tamanho += 1

	def inserir_elemento_posicao_especifica(self, elemento, posicao):
		if posicao == 0:
			novo_no = No(elemento)
			novo_no.proximo = self.__primeiro_no
			self.__primeiro_no = novo_no
		elif posicao == self.__tamanho:
			novo_no = No(elemento)
			self.__ultimo_no.proximo = novo_no
			self.__ultimo_no = novo_no
		else:
			no_anterior = self.recuperar_no(posicao - 1)
			no_atual = self.recuperar_no(posicao)
			novo_no = No(elemento)
			novo_no.proximo = no_atual
			no_anterior.proximo = novo_no
		self.__tamanho += 1

	def recuperar_no(self, posicao):
		resultado = 0
		for i in range(posicao + 1):
			if i == 0:
				resultado = self.__primeiro_no
			else:
				resultado = resultado.proximo
		return resultado

	def recuperar_elemento_no(self, posicao):
		no = self.recuperar_no(posicao)
		if no != None:
			return no.elemento
		else:
			return None

	def contem(self, elemento):
		for i in range(self.__tamanho):
			if elemento == self.recuperar_elemento_no(i):
				return True
		return False

	def indice(self, elemento):
		for i in range(self.__tamanho):
			if elemento == self.recuperar_elemento_no(i):
				return i
		return None
	def remover_pos(self, posicao):
		if posicao == 0:
			self.__primeiro_no = self.__primeiro_no.proximo
			self.__tamanho -= 1
		elif posicao == (self.__tamanho-1):
			self.__ultimo_no = self.recuperar_no(posicao-1)
			self.__ultimo_no.proximo = None
			self.__tamanho -= 1
		elif posicao >= self.__tamanho:
			print('Posição invalida')
		else:
			no_anterior = self.recuperar_no(posicao-1)
			no_posterior = self.recuperar_no(posicao+1)
			no_anterior.proximo = no_posterior
			self.__tamanho -= 1

	def remover_elemento(self, elemento):
		if self.indice(elemento) != None:
			self.remover_pos(self.indice(elemento))
		else:
			print('ELemento não existe na lista')