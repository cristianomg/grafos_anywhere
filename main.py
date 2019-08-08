from grafos import grafo
print('-'*30, 'MENU', '-'*30)

menu = int(input('Digite uma opção: '))

if menu == 1:
	grafo = grafo.Grafo()
	grafo.adicionar_vertice('v1','v2','v3')
	grafo.adicionar_arestas(('v1','v2'),('v1','v3'),('v2','v3'))
	print('Vertices:', grafo.vertices)
	print('Arestas:', grafo.arestas)
	print('Adjacentes:', grafo.adjacentes('v3'))
	print(f'É completo: {grafo.ehCompleto()}')
	print(f'É regular: {grafo.ehRegular()}')