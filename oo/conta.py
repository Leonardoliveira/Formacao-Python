#criando uma classe em python
class Conta:
    #Atributos são as caracteriscas do objeto e os metodos são o que o objeto pode fazer

    def __init__(self, numero, titular, saldo, limite): #Tem que colocar o "self", pois ele guarda a referencia do objeto de forma automtica e se tiver, adicionar os outros atributos
        print('Construindo um objeto... {}'.format(self))

        #Criando atributos da classe conta
        self.__numero = numero # deixar o atributo privado no python é colocando __ na frente do elemento
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite


    def extrato(self):
        print('Olá, {}!\nSaldo Atual:R$ {}.'.format(self.__titular, self.__saldo))

    def deposita(self, valor):
        self.__saldo += valor

    def __pode_sacar(self, valor_a_sacar):
        valor_disponivel_a_sacar = self.__saldo + self.__limite
        return valor_a_sacar <= valor_disponivel_a_sacar

    def sacar(self, valor):
        if self.__pode_sacar(valor):
            self.__saldo -= valor
        else:
            print('O valor de R${} passou o limite de R${}.\nEntre em contato com seu gerente, para avaliação do limite.'.format(valor, self.__limite))

    def transefere(self, valor, destino):
        print('Saldo anterior:R$ {}.'.format(self.__saldo))
        self.sacar(valor)
        destino.deposita(valor)
        print('Transferindo de {} para {} no valor de R${}.'.format(self.__titular, destino.__titular, valor))
        self.extrato()

    @property#Trata o metodo como uma propriedade, mas para funcionar, precisar deixar o atributo privado
    def saldo(self):
        return self.__saldo

    @property
    def titular(self):
        return self.__titular.title()

    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, valor): # o Set não retorna. se colocar return, vai dar ruim
        self.__limite = valor

    @staticmethod # Atribui um valor estatico
    def codigo_banco():
        return '001'

    @staticmethod
    def codigos_bancos():
        return {'BB': '001', 'Caixa': '104', 'Bradesco': '234'}


