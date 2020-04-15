class Cliente:
    def __init__(self, nome):
        self.__nome = nome

    @property #Trata o metodo como uma propriedade, mas para funcionar, precisar deixar o atributo privado
    def nome(self):
        print('Chamado @propety nome()')
        return self.__nome.title()

    @nome.setter # Usando como set
    def nome(self, nome):
        self.__nome = nome