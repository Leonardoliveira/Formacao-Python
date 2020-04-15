#Criando uma classe para datas
from datetime import datetime, timedelta
class datasBr:
    def __init__(self):
        self.momento_cadastro = datetime.today()

    #criando metodo de string
    def __str__(self):
        return self.format_data()

    #metodo para retornar o mes de cadastro
    def mes_cadastra(self):
        meses_do_ano = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]
        mes_cadastro = self.momento_cadastro.month - 1
        return meses_do_ano[mes_cadastro]

    #metdod para retornar a semana
    def dia_semana(self):
        dias_semana = ["Segunda-Feira", "Terça-Feira", "Quarta-Feira", "Quinta-Feira", "Sexta-Feira", "Sábado", "Domingo"]
        dia_semana = self.momento_cadastro.weekday()
        return dias_semana[dia_semana]

    #Criando metodo de formatação de data
    def format_data(self):
        dataformatada = self.momento_cadastro.strftime("%d/%m/%Y - %H:%M")
        return dataformatada

    #criando metodo de comparção das datas
    def tempo_cadastro(self):
        tempo_cadastro = (datetime.today() + timedelta(days=30)) - self.momento_cadastro
        return tempo_cadastro