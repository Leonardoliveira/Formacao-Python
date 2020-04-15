import requests
from acesso_cep import BuscaEndereco
cep = "06622000"
obj_cep = BuscaEndereco(cep)
# print(obj_cep)
# r = requests.get('https://viacep.com.br/ws/01001000/json/')
# print(r.text)
bairro, cidade, uf = obj_cep.acessa_via_cep()
print(bairro, cidade, uf)



#Formatando datas
from datetime import datetime, timedelta
# from datas_Br import datasBr
#
# hoje = datasBr()
# print(hoje.tempo_cadastro())

# hoje = datetime.today()
# amanha = datetime.today() + timedelta(days=1)
# print(amanha - hoje)


# cadastro = datasBr()
# print(cadastro)


# hoje = datetime.today()
# hoje_formatado = hoje.strftime("%d/%m/%Y - %H:%M")
# print(hoje, hoje_formatado, sep="\n")


# cadastro = datasBr()
# print(cadastro.momento_cadastro.today())
# print(cadastro.dia_semana())
# print(cadastro.mes_cadastra())

# #Expressões REgulares
# from telefonesBr import TelefonesBr
# import re

# telefone = "551126481234"
# telefone_objeto = TelefonesBr(telefone)
# telefone_objeto.formata_numero()
#padrao = "([0-9]{2,3})?([0-9]{2})([0-9]{4,5})([0-9]{4})"
#resposta = re.search(padrao, telefone)
#print(resposta.group())

#fazendo um padrão para telefones
# padrao_molde = "(xx)aaaa-wwww"
# padrao = "[0-9]{2}[0-9]{4,5}[0-9]{4}"
# texto = "eu gosto do numero 211234-5678"
# resposta = re.findall(padrao, texto)
# print(resposta)


#criando um padrão para receber email
# padrao = "\w{5,50}@\w{3,10}.\w{2,3}.\w{2,3}"
# texto = "aaabbbcc leonardo@gmail.com.br"
# resposta = re.search(padrao, texto)
# print(resposta.group())

# texto = "123 1a2 1cc aal"
# resposta = re.search(padrao, texto)
# print(resposta.group())imprimir o padrão .group

#Imporantando biblioteca de validação de CPF
# from validate_docbr import CPF
# from cpf_cnpj import Documento
# exemplo_CNPJ = "60862295000137"
# exemplo_CPF = "42285183895"
# documento = Documento.cria_documento(exemplo_CNPJ)
# documento1 = Documento.cria_documento(exemplo_CPF)
# print(documento, documento1, sep="\n")

# cpf_um = Cpf(42285183895)
# print(cpf_um)
# cpf = CPF()
# cpf1 = str(15763822064)
# objeto_cpf = Cpf(cpf1)

#Fatiando o cpf
# fatia1 = cpf[:3]
# fatia2 = cpf[3:6]
# fatia3 = cpf[6:9]
# fatia4 = cpf[9:]
# lista1 = [fatia1, fatia2, fatia3, fatia4]
# # for fatia in range(len(lista1)):
# # #     print(fatia, lista1[fatia])
# cpf_formatado = "{}.{}.{}-{}".format(fatia1, fatia2, fatia3, fatia4)
# print(objeto_cpf)
# print(cpf.validate("42285183895")) # Verificando se o CPF é válido