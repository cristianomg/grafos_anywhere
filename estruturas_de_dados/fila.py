from listas import lista_ligada


class Fila:

    def __init__(self):
        self.__elementos = lista_ligada.ListaLigada()

    def enfilerar(self, elemento):
        self.__elementos.inserir(elemento)

    def desenfilerar(self):
        if self.__elementos.tamanho >= 1:
            elemento = self.__elementos.recuperar_elemento_no(0)
            self.__elementos.remover_pos(0)
            return elemento
        else:
            return None

    def __str__(self):
        return self.__elementos.__str__()
