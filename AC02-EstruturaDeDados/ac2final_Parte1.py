#Nome da Disciplina: Estrutura de Dados.
#Turma: 3° BD
#Número da pergunta: 1
#Titúlo da pergunta: Likes de Postagens em Redes Sociais
#Integrante 1: Ivan Szoboszlay Junior
#Integrante 2: Leonardo Silva de Oliveira
#Data: 31/03/2020
#Professor: Jorge Carlos Valverde Rebaza
from random import randint

class LinkRedeSocias:
    def __init__(self, lista = None):
        self.lista = []
        self.indice = []

    #Metodo de criação de post
    def PushPost(self):
        self.lista.append(0)
        self.indice.append(len(self.lista)-1)     
        return self.lista

    #Metodo de Link
    def PushLink(self, posicao, link):

        # If para testar se a posição existe dentro da lista. 
        if posicao <= len(self.lista)-1:

            self.lista[posicao] += link #Acumula link a um post 2
            if link > 1 and link <= 10: #Quantidade de link entre 1 a 10 politica de bonus
                
                if posicao == 0: #Verificando se a posiçao é 0 para adicionar o bonus uma posicao a frente.
                    self.lista[posicao+1] += 1
                
                elif posicao == len(self.lista) - 1: #Verificando se a posiçao é a ultima para adicionar o bonus uma posicao atraz .
                    self.lista[posicao-1] += 1
                
                else:    
                    self.lista[posicao-1] += 1
                    self.lista[posicao+1] += 1

            else: #Quantidade de link acima de 10 politica de bonus
                
                if posicao == 0:# Verificando se a posiçao é 0 para adicionar o bonus uma posicao a frente.
                    self.lista[posicao+1] += int(link/2)
                
                elif posicao == len(self.lista) -1: # Verificando se a posiçao é a ultima para adicionar o bonus uma posicao atraz .
                    self.lista[posicao-1] += int(link/2)
                
                else:    
                    self.lista[posicao-1] += int(link/2)
                    self.lista[posicao+1] += int(link/2)
        else:
            print("Posição não existe na lista")
            posicao=(randint(0, len(self.lista)-1))#Gera numero aleatorio de 0 ao tamanho da lista
            self.lista[posicao] += link
            return self.lista

    #Metodo de top 3
    def top(self):
        listatop = self.lista
        Top = []#Lista para pegar os mairos  links
        indecetop = []#Pegar o indece da lista
        for i in range(3):#Loop para rodar 3 vezes apenas para pegar o 3 com mais links
            #Pegar o primeiro elemtno da lista e a indece(posicao) 
            Comparador = listatop[0]
            posicao = 0

            for x in range(len(listatop)):
                if listatop[x] > Comparador:
                    Comparador = listatop[x]
                    posicao = x

            #Adicionar a index a lista indecetop
            indecetop.append(posicao)

            #Adicionar o comparador a lista TOP
            Top.append(Comparador)

            #Apegar o elemento da lista que foi encontrado pela indece 
            listatop.pop(posicao)
        print("-----------------------------------")
        print("O top-3 posts com mais likes são:")
        print("                            ")
        print("TOP:     1  2  3")
        print("Indice:", indecetop)
        print("Likes: ", Top)
        print("                                    ")

        return 

#instancia a class 
Postlink=LinkRedeSocias()

#Menu de interação com o usario 
print("Iniciar o programa")
print("Digite 1 para Criar um post " )  
print("Digite 2 para Dar likes a um post ")
print("Digite 3 para Top 3 posts com mais likes ")
Menu=int(input("Digite aqui: "))

while Menu != 4: #Loop para que o programa fica em execução até o usario digita 4 para finalizar o programa. 
    
    if Menu ==1: #Registrar um novo post:
        Postlink.PushPost()
        print("-----------------------------------")
        print("Publicacao Criada")
        print("Indice:",Postlink.indice)
        print("Likes: ",Postlink.lista)
        print("                        ")
        voltar=str(input("Aperte R para voltar: "))

    if Menu == 2:# Dar link nos post:
        print("---------------------------------------------------------------")
        Publicacao=int(input("Digite o indece da publicacao que deseja incluir likes: "))
        Likes=int(input("Digite a quantidade de likes: "))
        Postlink.PushLink(Publicacao,Likes)
        print("Indice:",Postlink.indice)
        print("Likes: ",Postlink.lista)
        print("                        ")
        voltar=str(input("Aperte R para voltar: "))
    
    if Menu==3:# Os 3 post com mais link 
        Postlink.top()
        print("                                ")
        voltar=str(input("Aperte R para voltar: "))
   
    if voltar == "R" or voltar =="r":
        #Menu de interação com o usario 
        print("-----------------------------------")
        print("                            ")
        print("           Menu             ")
        print("                            ")

        print("Digite 1 para Criar um post " )  
        print("Digite 2 para Dar likes a um post ")
        print("Digite 3 para Top 3 posts com mais likes ")
        print("Digite 4 para finalizar a execucao ")
        Menu=int(input("Digite aqui: "))

print("Fim da execução do programa")