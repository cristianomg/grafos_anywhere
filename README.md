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

Grafo direcionado = True

Vertices que serão declarados =  1,2,3,4.

Arestas que serão declaradas =  1 ate 2 , 1 ate 3, 2 ate 4, 3 ate 4.

Resultado no arquivo json = 
    {
        "direcionado": "True",
        "vertices": "v1,v2,v3,v4",
        "arestas": "v1-v2,v1-v3,v2-v4,v3-v4"
    }
    
## Funções 

Para testar as funções solicitadas no documento da atividade foi feito um menu ilustrativo onde cada opção escolhida executa uma
das funções solicitadas.

1. Representação do grafo
2. getAdjacentes
3. ehRegular
4. ehCompleto
