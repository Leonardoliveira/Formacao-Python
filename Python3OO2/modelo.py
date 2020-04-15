class Programa:

    def __init__(self, nome, ano):
        self._nome = nome.title() #Atributos privados
        self.ano = ano
        self._likes = 0 #Atributos privados

    @property #usar esse comando para chamar atributos privados
    def likes(self):
        return self._likes

    def dar_likes(self):
        self._likes += 1

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome.title()

    def __str__(self):
       return f'Programa: {self._nome} - {self.ano} - {self._likes}'

class Filme(Programa): #para herdar caracteristicas de uma classe mãe, deve colocar entre parenteses(nome da classe mãe)

    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano) # Quando precisar herdar os atributos da classe mãe, usar a função super()
        self.duracao = duracao

    def __str__(self):
       return f'Programa: {self._nome} - Ano: {self.ano} - Duração: {self.duracao} - {self._likes} Likes.'

class Serie(Programa):

    def __init__(self, nome, ano, temporada):
        super().__init__(nome, ano)
        self.temporada = temporada

    def __str__(self):
        return f'Programa: {self._nome} - Ano: {self.ano} - Temporadas: {self.temporada} - {self._likes} Likes.'

#Exemplo de uma classe herdando caracteristicas de outra classe vindo do python
# class Playlist(list):#A Classe 'list' já vem no python, coloquei como paramentro para herdar suas funções para classe playlist.
#     def __init__(self, nome, programas):
#         self.nome = nome
#         super().__init__(programas)

class Playlist():
    def __init__(self, nome, programas):
        self.nome = nome
        self._programas = programas

    #Representa os comportamentos de uma lista, que deixa a classe interavel.
    def __getitem__(self, item):
        return self._programas[item]

    #Função para mostrar os dados
    @property
    def listagem(self):
        return self._programas

    # Função para contar os elementos da lista de programas
    # @property
    # def tamanho(self):
    #     return len(self._programas)

    #metodo que retorna o tamanho da lista
    def __len__(self):
        return len(self._programas)