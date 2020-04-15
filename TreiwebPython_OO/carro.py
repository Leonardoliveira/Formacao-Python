class Carro:
    """
    Exemplo de DocString.
    Essa é a classe carro. Esta classe é utilizada para instanciar novos carros em nosso programa.
    """
    def __init__(self, cor, qtd_portas, tipo_combustivel, potencia, qtd_combustivel, is_ligado, velocidade):
        self.cor = cor
        self.qtd_portas = qtd_portas
        self.tipo_combustivel = tipo_combustivel
        self.potencia = potencia
        self.qtd_combustivel = qtd_combustivel
        self.is_ligado = is_ligado
        self.velocidade = velocidade

    def abastecer(self, qtd_combustivel):
        """
        O metodo abastecer recebe como parametro a quantidade de combustivel
        e incrementa no atributo qtd_combustivel do objeto carro

        """
        self.qtd_combustivel += qtd_combustivel

    def ligar(self):
        if self.is_ligado:
            print('O carro já está ligado!')
        else:
            self.is_ligado = True
            print('O carro foi ligado')

    def desligar(self):
        if self.is_ligado == FileExistsError:
            print('O carro já está desligado!')
        else:
            self.is_ligado = False

    def acelerar(self, velocidade=10):
        if self.is_ligado:
            self.velocidade += velocidade
        else:
            print('O carro precisa está ligado!')