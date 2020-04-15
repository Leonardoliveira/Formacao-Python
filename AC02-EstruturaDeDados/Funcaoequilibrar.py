from random import randrange, uniform
import random


tipo1 = [10, 10, 10, 10, 10, 10, 10, 10, 10]
tipo2 = [10, 10, 10, 10, 10.685]
tipo3 = [10, 10, 10, 2.96146849, 10, 10.69584, 10, 10, 10]


Peso_Total = 0.0
comparacao = []

Peso_Total += sum(tipo1)
Peso_Total += sum(tipo2)
Peso_Total += sum(tipo3)
print(Peso_Total)
if Peso_Total <=70:#Verificar o peso do armazenamento 
    print("True")
            
else:
    comparacao.append(len(tipo1))
    comparacao.append(len(tipo2))
    comparacao.append(len(tipo3))
    comparacaomenor = 3
    vazio = 0
    for i in range(3):
        if comparacao[i] == 0:
            vazio += 1
    #Caso apenas uma das lista tenha valor
    if vazio == 2:
        if len(tipo1)>0:
            acima = tipo1

        elif len(tipo2)>0:
            acima = tipo2

        else:
            acima = tipo3
        unico = max(comparacao)//2
        for i in range(unico):
            del(acima[i])      
    else:

        #Para verificar se alguma dos(tipo1,tipo2 e tipo3) for vazia 
        if len(tipo1) == 0:
            comparacaomenor = 0
        elif len(tipo2) == 0:
            comparacaomenor = 1
        else:
            comparacaomenor = 2

        maior = max(comparacao)
        #Verificar se as 3 lista(tipo1,tipo2 e tipo3) tem valor acima de 0.
        if comparacaomenor!= 3:
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
                    print(comparacao,"2")
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
            if len(tipo2) == len(tipo1) ==  len(tipo3) or len(tipo1) == len(tipo2) or len(tipo2) == len(tipo3) or len(tipo3) == len(tipo1) :
                controle = 2
            else:
                x=comparacao.index(maior)#Pegar o indece do maior valor da comparacao
                if x == 0:
                    for i in range(tirar):
                        del(tipo1[i])#Apagar valor dentro da lista
                    comparacao[0]=menor
                elif x == 1:
                    for i in range(tirar):
                        del(tipo2[i])#Apagar valor dentro da lista
                else:
                    for i in range(tirar):
                        del(tipo3[i])#Apagar valor dentro da lista
            maior = max(comparacao)
            maior = max(comparacao)
            menor = min(comparacao)
            tirar = maior - menor

        