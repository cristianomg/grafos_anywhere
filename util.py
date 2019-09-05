import json


def iniciar_dados():
    with open('grafo.json') as f:
        data = json.load(f)
    vertices = data['vertices'].split(",")
    arestas = [tuple(aresta.split('-')) for aresta in data['arestas'].split(',')]
    pesosArestas = data['pesosAresta']
    if data['direcionado'] == "True":
        direcionado = True
    else:
        direcionado = False
    return vertices, arestas, direcionado, pesosArestas

def printar_inicialização(vertices, arestas):
    print('-' * 30, 'CONFIGURAÇÃO DO JSON', '-' * 30)
    print('Vertices: ', end="")
    for n, i in enumerate(vertices):
        if n == len(vertices) - 1:
            print(i, end="")
        else:
            print(i, end=", ")
    print()
    print('Arestas: ', end="")

    for n, i in enumerate(arestas):
        if n == len(arestas) - 1:
            print(i[0], "--", i[1], end="")
        else:
            print(i[0], "--", i[1], end=", ")
    print()
    print()