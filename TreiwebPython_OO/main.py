#Importando as algumas funções do módulo
#from math import pow, factorial
#Importando todas as funções do módulo, porém, não é uma boa prática
#from math import *
#import math
#import cmath
#print(math.pow(2, 3))
#print(cmath.cos(4))

import carro
uno_vermelho = carro.Carro('vermelho', 4, 'Flex', 1.0, 0, False, 0)
help(uno_vermelho.abastecer)#Metodo help, retorna o valor dentro da docstring
uno_vermelho.ligar()
uno_vermelho.abastecer(50)
uno_vermelho.abastecer(10)
print(f'A qtd de combustivel do carro é : {uno_vermelho.qtd_combustivel}.')

uno_preto = carro.Carro('preto', 2, 'Flex', 1.4, 0, False, 0)
uno_preto.desligar()
print(f'A qtd de combustivel do carro é : {uno_preto.qtd_combustivel}.')
uno_preto.acelerar(20)