from random import *

# inserir na pilha
# remover da pilha
# consultar o topo da pilha

class Rocha:
    def __init__(self, data):
        self.data = data
        self.next = None

class Lixo:
    def __init__(self, data):
        self.data = data
        self.next = None

class Curiosity:
    def __init__(self):
        self.top = None
        self._size = 0

    def pushRocha(self, elem):
        #insere um elemento na pilha
        armazanemento = Rocha(elem)
        armazanemento.next = self.top
        self.top = armazanemento
        self._size = self._size + 1

    def popRocha(self):
        # remove o elemento do topo da pilha
        if self._size > 0:
            armazanemento = self.top
            self.top = self.top.next
            self._size = self._size - 1
            return armazanemento.data
        raise IndexError("A pilha está vazia")

    def peekRocha(self):
        # retorna o topo sem remover
        if self._size > 0:
            return self.top.data
        raise IndexError("A pilha está vazia")

    def pushLixo(self, elem):
        #insere um elemento na pilha
        armazanemento = Lixo(elem)
        armazanemento.next = self.top
        self.top = armazanemento
        self._size = self._size + 1

    def popLixo(self):
        # remove o elemento do topo da pilha
        if self._size > 0:
            armazanemento = self.top
            self.top = self.top.next
            self._size = self._size - 1
            return armazanemento.data
        raise IndexError("A pilha está vazia")

    def peekLixo(self):
        # retorna o topo sem remover
        if self._size > 0:
            return self.top.data
        raise IndexError("A pilha está vazia")


    def __len__(self):
        """Retorna o tamanho da lista"""
        return self._size

    def __repr__(self):
        # retorna que objeto está visualizando
        r = ""
        pointer = self.top
        while(pointer):
            r = r + str(pointer.data) + "\n"
            pointer = pointer.next
        return r

    def __str__(self):
        #Retorna o valor em string
        return self.__repr__()