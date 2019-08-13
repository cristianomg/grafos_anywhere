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


Resultado no arquivo json

    {
        "direcionado": "True",
        "vertices": "v1,v2,v3,v4",
        "arestas": "v1-v2,v1-v3,v2-v4,v3-v4"
    }
 

## Funções 

Para testar as funções solicitadas no documento da atividade foi feito um menu ilustrativo onde cada opção escolhida executa uma
das funções solicitadas.

1- Representação do grafo
```
Retorna uma representação do grafo do tipo chave/valor
```
2- getAdjacentes
```
Retorna os adjacentes de um determinado vertice passado no paremetro
```
3- ehRegular
```
Retorna True se o grafo for regular e False se o grafo não for regular
```
4- ehCompleto
```
Retorna True se o grafo for completo e False se o grafo não for completo
```
5- ehConexo
```
Faz uma busca utilizando os algoritmos de busca em largura e busca em profundidade.
Caso o resultado da busca sem fazer saltos for igual aos vertices do grafo retorna True caso não, retorna False.
Os algoritmos são escolhidos no paremetro, por padrão utiliza o algoritmo bfs.  
```
