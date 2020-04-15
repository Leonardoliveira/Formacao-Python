#criando uma função para criar contas
def cria_conta(numero, titular, saldo, limite):
    conta = {'numero':numero, 'titular': titular, 'saldo': saldo, 'limite': limite}
    return conta
#Criando funções para conta

def deposita(conta, valor):
    conta['saldo'] += valor
def sacar(conta, valor):
    conta['saldo'] -= valor
def extrato(conta):
    print("Seu saldo: R$ {}.".format(conta['saldo']))