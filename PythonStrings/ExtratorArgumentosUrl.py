#criando uma classe para o extrator.
class ExtratorArgumentosUrl:
    #criando o metodo de inicializador.
    def __init__(self, url):
        if self.urlEhValida(url):
            self.url = url.lower()
        else:
            raise LookupError('URL inválida!')

    #Criando um metodo especial de contar
    def __len__(self):
        return len(self.url)

    def __str__(self):
        moedaOrigem, moedaDestino = self.extrairArgumento()
        representaçãoString = self.extraiValor() + " " + moedaOrigem + " " + moedaDestino
        representaçãoString2 = "VAlor: {}\nMoeda Origem: {}\nMoeda Destino: {}.".format(self.extraiValor(), moedaOrigem, moedaDestino)
        return representaçãoString

    def __eq__(self, outraInstancia):
        return self.url == outraInstancia.url

    #Verificando se a url é válida.
    #Criando um metodo estático.
    @staticmethod # Quando começa com @, é um decorador, no python. Não precisando passar o Self.
    def urlEhValida(url):
        if url and url.startswith("https://bytebank.com"):
            return True
        else:
            return False

    #Criando metodo de instancia(utilizando o self) para extrair os argumentos
    def extrairArgumento(self):
        #Criando varieveis para dividir a url e extrair os nomes das moedas

        buscaMoedaOrigem  = "moedaorigem=".lower() #nome do argumento
        buscaMoedaDestino = "moedadestino=".lower()

        # procurando a moeda origem
        indiceInicialMoedaOrigem    = self.encontraIndiceInicial(buscaMoedaOrigem)
        indiceFinalMoedaorigem      = self.url.find("&")

        #Adicionando o fatiamento nas varieveis
        moedaOrigem = self.url[indiceInicialMoedaOrigem:indiceFinalMoedaorigem]

        if moedaOrigem == "moedadestino":
            self.trocaMoedaOrigem()
            indiceInicialMoedaOrigem = self.encontraIndiceInicial(buscaMoedaOrigem)
            indiceFinalMoedaorigem = self.url.find("&")
            moedaOrigem = self.url[indiceInicialMoedaOrigem:indiceFinalMoedaorigem]

        #procurando a moeda destino
        indiceInicialMoedaDestino = self.encontraIndiceInicial(buscaMoedaDestino)
        indicefinalMoedaDestino = self.url.find("&valor")
        moedaDestino = self.url[indiceInicialMoedaDestino:indicefinalMoedaDestino]

        #retornando dois valores
        return moedaOrigem, moedaDestino

    #Criando metodo para achar o indice
    def encontraIndiceInicial(self, moedaBuscada):
        return self.url.find(moedaBuscada) + len(moedaBuscada)

    #metodo para trocar palavra "moedadestino" para "real"
    def trocaMoedaOrigem(self):
        self.url = self.url.replace("moedadestino", "real", 1)
        print(self.url)

    def extraiValor(self):
        buscaValor = "valor="
        indiceInicialValor = self.encontraIndiceInicial(buscaValor)
        valor = self.url[indiceInicialValor:]
        return valor



