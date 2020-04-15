#Nome da Disciplina: Estrutura de Dados.
#Turma: 3° BD
#Número da pergunta: 2
#Titúlo da pergunta: Rover Curiosity
#Integrante 1: Ivan Szoboszlay Junior
#Integrante 2: Leonardo Silva de Oliveira
#Data: 31/03/2020
#Professor: Jorge Carlos Valverde Rebaza
import random
from random import randrange, uniform

class Rocha:
    def __init__(self):
        listarocha = []

    def PuchPostRocha(self):
        tamanho = random.randint(30, 120)
        listarochapeso = []
        listadiamentro = []
        for rocha in range(100):
            listarochapeso.append(uniform(0.5, 2.5))
            listadiamentro.append(uniform(0, 0.74))
        return listarochapeso, listadiamentro

'''
class LixoEspacial:
    def __init__(self, pinha = None):
        lista = []

    def PushPost(self):
        tamanho = random.randint(30,120)

        for peso in range(tamanho):
            lista.append(uniform(1.2,8.55))#peso do lixo espacial
'''

class Curiosity:

    def __init__(self, lista=None, tipo1=None, tipo2=None, tipo3=None):
        self.lista = []
        self.lixo = []
        self.tipo1 = []
        self.tipo2 = []
        self.tipo3 = []
        self.teste = 0

    #Metodo de criação de post
    def PushPost(self,tipo, peso, diamentro):
        
        if tipo == 1:  #Validar se o tipo é rocha

            if (peso>= 0.0 and peso<= 2.5) and (diamentro>=0.0 and diamentro<=0.74):#Condicao de peso ser menor de 2,5Kg e diamentro for menor de 0,74m
                classpropria = Curiosity()
                #classpropria.equilibrar()
                              
                if peso <=0.83 and diamentro<=0.24:#Tipo 1
                    self.tipo1.append(peso)
                
                elif peso > 0.83 and peso <= 1.25 and diamentro >0.24 and diamentro<=0.50:#Tipo 2
                    self.tipo2.append(peso)
                else:
                    self.tipo3.append(peso)

            else:   
                self.teste += 1
                print("Rocha Descartado")  

        else:
            if tipo == "metalico":

                return 1  
            else:# Lixo nao metalico
                return 1  
    #Função para equilibrar as rocha 

    #o robô avalia a
    #quantidade de rochas em função do seu tipo e, rejeita (elimina) as rochas necessárias até
    #ter uma quantidade mais ou menos equilibrada de tipos de rochas.

    def equilibrar(self):
        print(self.tipo1)
        Peso_Total = 0
        comparacao = []
        Peso_Total += sum(self.tipo1)
        Peso_Total += sum(self.tipo2)
        Peso_Total += sum(self.tipo3)
        print(Peso_Total,"Teste")
        if Peso_Total <= 70:#Verificar o peso do armazenamento
            return True
        else:
            print("Acionou a funcao de equilibrar")    
            comparacao.append(len(self.tipo1))
            comparacao.append(len(self.tipo2))
            comparacao.append(len(self.tipo3))
            comparacaomenor = 3
            vazio = 0
            for i in range(3):
                if comparacao[i] == 0:
                    vazio += 1
            
            #Caso apenas uma das lista tenha valor
            if vazio == 2:
                if len(self.tipo1) > 0:
                    acima = self.tipo1

                elif len(self.tipo2) > 0:
                    acima = self.tipo2

                else:
                    acima = self.tipo3
                    
                unico = max(comparacao) // 2
                for i in range(unico):
                    del(acima[i])  
                return True     
            else:

                #Para verificar se alguma dos(tipo1,tipo2 e tipo3) for vazia 
                if len(self.tipo1) == 0:
                    comparacaomenor=0
                elif len(self.tipo2) == 0:
                    comparacaomenor = 1
                else:
                    comparacaomenor = 2

                maior=max(comparacao)
                #Verificar se as 3 lista(tipo1,tipo2 e tipo3) tem valor acima de 0.
                if comparacaomenor != 3:
                    posicaomaior = comparacao.index(maior)
                    #Sa tipo1 for vazia 
                    if comparacaomenor == 0:
                        #verificar se a posicao é igual a 1 e adicioar o valor da posicao 2 na 0.
                        if posicaomaior == 1:
                            comparacao[0] = comparacao[2]
                        #falso adicioar o valor da posicao 1 na 0.
                        else:
                            comparacao[0] = comparacao[1]
                    #Se a tipo2 for vazio
                    elif comparacaomenor == 1:
                        #verificar se a posicao do maior é 0 se for adicionar o valor da posição 2 na posicao 1 da lista comparacao
                        if posicaomaior == 0:
                            comparacao[1] = comparacao[2]
                            print(comparacao,"1")
                        #Falso a posicao 1 o valor da posicao 0
                        else:
                            comparacao[1] = comparacao[0]
                            print(comparacao, "2")
                    #Se a tipo3 for vazia 
                    else:
                        #verificar se a posicao do maior é 0 se for adicionar o valor da posição 1 na posicao 2 da lista comparacao
                        if posicaomaior == 0:
                            comparacao[2] = comparacao[1]
                    
                        #Falso substituir o valor da posicao 2 com o da posicao 0
                        else:
                            comparacao[2] = comparacao[0]
                            
            
                menor = min(comparacao)
                tirar = maior-menor
                controle = 0
                #Loop para apagar valor das tipo1, tipo2 e tipo3 e deixa equilibrado 
                while controle != 2:
                    #Verificar se as tipo1,tipo2 e tipo3 esta equilibrada 
                    if len(self.tipo2) == len(self.tipo1) ==  len(self.tipo3) or len(self.tipo1) == len(self.tipo2) or len(self.tipo2) == len(self.tipo3) or len(self.tipo3) == len(self.tipo1) :
                        controle = 2
                    else:
                        x = comparacao.index(maior)#Pegar o indece do maior valor da comparacao
                        if x == 0:
                            for i in range(tirar):
                                del(self.tipo1[i])#Apagar valor dentro da lista
                            comparacao[0] = menor
                        elif x == 1:
                            for i in range(tirar):
                                del(self.tipo2[i])#Apagar valor dentro da lista
                        else:
                            for i in range(tirar):
                                del(self.tipo3[i])#Apagar valor dentro da lista
                    maior = max(comparacao)
                    maior = max(comparacao)
                    menor = min(comparacao)
                    tira = maior-menor
                return True 
   
'''

    def rejeita(self):
        pinha=[]
        lista=[]
        #instancia a class 
        armazenamento=Rocha()
        for x in range(30):
            
            tamanho=random.randint(30,120)
            pinha.append(uniform(0.5,14.2))#Peso das rocha

'''
robo = Curiosity()
rocha = Rocha()
peso, diamentro = rocha.PuchPostRocha()
print(f"Peso das rochas coletadas: {peso}.")
print(f"Diamentro das rochas coletadas: {diamentro} .")

for x in range(len(peso)):
    robo.PushPost(1, peso[x], diamentro[x])
print("Teste ", robo.teste)
print("Tipo1: ", robo.tipo1)
print("Tipo2: ", robo.tipo2)
print("Tipo3: ", robo.tipo3)


