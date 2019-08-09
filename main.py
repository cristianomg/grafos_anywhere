from grafos import grafo
import json

####################Entrada de dados#########################

with open('grafo.json') as f:    
	data = json.load(f)
vertices = data['vertices'].split(",")

arestas = [tuple(aresta.split('-')) for aresta in data['arestas'].split(',')]

grafo = grafo.Grafo()
grafo.adicionar_vertice(vertices)
grafo.adicionar_arestas(arestas)

print('-'*30, 'CONFIGURAÇÃO DO JSON', '-'*30)
print('Vertices: ',end="")
for n, i in	enumerate(vertices):
	if n == len(vertices)-1:
		print(i,end="")
	else:
		print(i,end=", ")
print()
print('Arestas: ',end="")

for n,i in enumerate(arestas):
	if n == len(arestas)-1:
		print(i[0],"--",i[1],end="")
	else:
		print(i[0],"--",i[1],end=", ")
print()
print()

#############################################################


print('-'*33, 'MENU DE FUNÇÕES', '-'*33)
print('1 - getAdjacentes')
print('2 - ehRegular')
print('3 - ehCompleto')
menu = int(input('Digite uma opção: '))
if menu == 1:
	var = input('Insira o nome do vertice que deseja verificar os adjacentes: ')
	print(f'Adjacentes: {grafo.adjacentes(var)}')
	
elif menu == 2:
	print(f'É regular: {grafo.ehRegular()}')

elif menu ==3:
	print(f'É completo: {grafo.ehCompleto()}')

elif menu == 4:
	grafo.