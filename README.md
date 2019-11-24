# Grafos Anywhere

Implementação de grafos em python para a disciplina de teoria dos grafos

## Representação do grafo

O grafo foi representado a partir da implementação de uma lista de adjacentes. A lista consiste em um dicionário onde
cada chave é o nome de um vertice do grafo e seu respectivo valor é uma lista de objetos, cada objeto representa uma
vertice adjacente ao vertice chave.

## Configurando o grafo

Para configurar o grafo foi feito um arquivo.json que possui um dicionario com 3 chaves. Na chave 'direcionado' é declarado se o grafo é direcionado ou não.  Na chave 'vertice' é declarado
os vertices do grafo. Na chave 'arestas' é declarado as arestas presentes no grafo.

Exemplo de declaração

Grafo direcionado

```
True
```

Vertices que serão declarados

````
1,2,3,4
````

Arestas que serão declaradas

```
1 ate 2, 1 ate 3, 2 ate 4, 3 ate 4
```

Pesos das arestas que serão declarados

```
Se o grafo possui 5 arestas necessita declarar 5 pesos.
Exemplo [10,2,5,9,3]
```

Resultado no arquivo json

    {
       "direcionado": false,
        "vertices": ["a","b","c","d","e","f","g"],
        "arestas": [
            ["a","b"],["a","d"],["b","c"],["b","d"],["b","e"],["c","e"], ["c","f"],["d","e"],["d","g"],["e","f"],["e","g"],["f","g"]
            ],
        "pesosAresta": [1,4,2,6,4,5,6,3,4,8,7,3]
    }

## Inicialização

Para iniciar o programa, após configurar o grafo no arquivo json, execute o arquivo main.py

## Funções

Para testar as funções solicitadas no documento da atividade foi feito um menu ilustrativo onde cada opção escolhida executa uma
das funções solicitadas.

1- Representação do grafo

<p>
Retorna uma representação do grafo do tipo chave/valor
</p>
2- getAdjacentes

<p>
Retorna os adjacentes de um determinado vertice passado no paremetro
</p>

3- ehRegular

Retorna True se o grafo for regular e False se o grafo não for regular

4- ehCompleto

<p>
Retorna True se o grafo for completo e False se o grafo não for completo
</p>
5- ehConexo
<p>

Faz uma busca utilizando os algoritmos de busca em largura e busca em profundidade.
Caso o resultado da busca sem fazer saltos for igual aos vertices do grafo retorna True caso não, retorna False.
Os algoritmos são escolhidos no paremetro, por padrão utiliza o algoritmo bfs. </p>

6- Algoritmo do menor caminho

Essa função busca o menor caminho entre os os vertices do grafo. O mesmo pode ser configurado de 2 maneiras.
A primeira forma será informado apenas o vertice de inicio e o algorimo irá mostrar o menor caminho para todos os
vertices.
A segunda forma será informado o vertice de inicio e o vertice final e o algoritmo ira mostrar todos os caminhos
ate achar o menor caminho ate o vertice final

7 - ordenação topologica

Essa função ordena os grafo dado um conjunto de dependencias (Arestas) de um grafo

8 - arvore geradora minima

Gera a arvore geradora minima a partir de um grafo , a arvore geradora minima possui todos os vertices do grafo porém apenas as arestas que somadas dão o menor valor e não formem ciclos, para esse algoritmo foi desenvolvido a abordagem de Prim

9 - busca por articulação

Dado um grafo e retornado os vertices que são articulações