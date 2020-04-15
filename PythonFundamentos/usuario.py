class Usuario:

    def __init__(self, nome, idade, sobrenome):
        self.nome = nome.title()
        self.idade = idade
        self.sobrenome = sobrenome.title()