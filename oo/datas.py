#Fazendo o desafio de criar uma classe que recebe uma data e faz a formatação
class Data:
    def __init__(self, dia, mes, ano):
        self.dia = dia
        self.mes = mes
        self.ano = ano
    def formatar_data(self):
        print(self.dia, self.mes, self.ano, sep='/')
