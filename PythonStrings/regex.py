import re

email1 = "Meu numero é 1234-1234"
email2 = "Fale comigo em 1234-1234 esse é meu telefone"
email3 = "1234-1234 é o meu celular"

#criando um padrão
padrao = "[0-9]{4,5}[-]*[0-9]{4}" #Não pode ter espaço

retorno = re.search(padrao, email2)

print(retorno.group())