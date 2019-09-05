from grafos import grafo
import util

vertices, arestas, direcionado, pesosArestas = util.iniciar_dados()
util.printar_inicialização(vertices, arestas)

grafo = grafo.Grafo(direcionado)
grafo.adicionar_vertice(vertices)
grafo.adicionar_arestas(arestas, pesosArestas)

print('-'*33, 'MENU DE FUNÇÕES', '-'*33)
print('1 - Representação do grafo')
print('2 - getAdjacentes')
print('3 - ehRegular')
print('4 - ehCompleto')
print('5 - ehConexo')
print('6 - Algoritmo do menor caminho')
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

elif menu == 5:
	opc = input("Digite o algoritmo que deseja utilizar [dfs] [bfs]")
	print(f'É Conexo: {grafo.ehConexo(opc)}')

elif menu == 6:
	print('1- Escolher o vertice de inicio e fim')
	print('2- EScolher apenas o vertice de inicio')
	opc = int( input("Escolha uma opção"))
	if opc == 1:
		verticeInicio = input("digite o vertice de inicio")
		verticeFim = input("digite o vertice final")
		grafo.dijkstra(verticeInicio, verticeFim)
	else:
		verticeInicio = input("digite o vertice de inicio")
		grafo.dijkstra(verticeInicio)