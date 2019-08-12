from grafos import grafo
import util

vertices, arestas, direcionado = util.iniciar_dados()
util.printar_inicialização(vertices, arestas)

grafo = grafo.Grafo(direcionado)
grafo.adicionar_vertice(vertices)
grafo.adicionar_arestas(arestas)

print('-'*33, 'MENU DE FUNÇÕES', '-'*33)
print('1 - Representação do grafo')
print('2 - getAdjacentes')
print('3 - ehRegular')
print('4 - ehCompleto')
print('5 - ehConexo')
menu = int(input('Digite uma opção: '))
if menu == 1:
	grafo.representacao()
elif menu == 2:
	var = input('Insira o nome do vertice que deseja verificar os adjacentes: ')
	print(f'Adjacentes: {grafo.getAdjacentes(var)}')
	
elif menu == 3:
	print(f'É regular: {grafo.ehRegular()}')

elif menu == 4:
	print(f'É completo: {grafo.ehCompleto()}')

elif menu==5:
	print(f'É Conexo: {grafo.ehConexo()}')