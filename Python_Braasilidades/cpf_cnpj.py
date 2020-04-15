#Importando biblioteca de validação de cpf
from validate_docbr import CPF, CNPJ
#Criando classe para CPF

#criando uma classe do tipo factory para selecionar o documento
class Documento:
    @staticmethod
    def cria_documento(documento):
        if len(documento) == 11:
            return DocCpf(documento)
        elif len(documento) == 14:
            return DocCnpj(documento)
        else:
            raise ValueError("Documento inválido!")

#Criando a classe para o cpf
class DocCpf:
    def __init__(self, cpf):
        if self.valida_cpf(cpf):
            self.cpf = cpf
        else:
            raise ValueError("CPF Inválido!")

    #Metodo para validar o CPF chamado a biblioteca validate_docbr
    def valida_cpf(self, cpf):
        validador = CPF()
        return validador.validate(cpf)

    #Metodo que retorna string
    def __str__(self):
        return self.formata_cpf()

    #Metodo para mascarar o cpf
    def formata_cpf(self):
        mascara = CPF()
        return mascara.mask(self.cpf)

#criando a classe para o cnpj
class DocCnpj:
    def __init__(self, cnpj):
        if self.valida_cnpj(cnpj):
            self.cnpj = cnpj
        else:
            raise ValueError("CNPJ Inválido!")

    #Metodo para validar Cnpj
    def valida_cnpj(self, cnpj):
        validate_cnpj = CNPJ()
        return validate_cnpj.validate(cnpj)

    #Metodo que retorna string
    def __str__(self):
        return self.formata_cnpj()

    #Metodo para mascarar cnpj
    def formata_cnpj(self):
        mascara = CNPJ()
        return mascara.mask(self.cnpj)


# class CpfCnpj:
#     #instanciando um objeto para o CPF
#     def __init__(self, documento, tipo_documento):
#         self.tipo_documento = tipo_documento
#         documento = str(documento)
#         if self.tipo_documento == "cpf":
#             if self.cpf_eh_valido(documento):
#                 self.cpf = documento
#             else:
#                 raise ValueError("CPF Inválido!")
#         elif self.tipo_documento == "cnpj":
#             if self.cnpj_e_valido(documento):
#                 self.cnpj = documento
#             else:
#                 raise ValueError("CNPJ Inválido!")
#         else:
#             raise ValueError("Documento inválido!")
#
#
#     #Metodo para imprimir mascara
#     def __str__(self):
#         if self.tipo_documento == 'cpf':
#             return self.format_cpf()
#         else:
#             return self.format_cnpj()
#
#     #CNPJ é válido
#     def cnpj_e_valido(self, cnpj):
#         if len(cnpj) == 14:
#             #instanciando a classe
#             validate_cnpj = CNPJ()
#             return validate_cnpj.validate(cnpj)
#         else:
#             raise ValueError("Quantidade de digitos, inválida!!")
#     #criando metodo para validar o cpf
#     def cpf_eh_valido(self, cpf):
#         if len(cpf) == 11:
#             validador = CPF()
#             return  validador.validate(cpf)
#         else:
#             raise ValueError("Quantidade de digitos, inválida!!")
#
#     #metodo para formatar o CPF
#     def format_cpf(self):
#         mascara = CPF()
#         return mascara.mask(self.cpf)
#
#     #Metodo para formatar o CNPJ
#     def format_cnpj(self):
#         mascara = CNPJ()
#         return mascara.mask(self.cnpj)