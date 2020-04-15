import random
import Jogos

def jogar():
    print('*********************************')
    print('Bem-vindo ao jogo de adivinhação!')
    print('*********************************')

    #Iniciando variáveis!
    numero_secreto = random.randrange(1, 101)
    total_de_tentativas = 0
    pontos = 1000

    print('Selecione o nível de dificuldade:')
    nivel = int(input('1.Fácil.\n2.Médio.\n3.Dificil.\nDigite aqui: '))
    if nivel == 1:
        total_de_tentativas = 20
    elif nivel == 2:
        total_de_tentativas = 10
    elif nivel == 3:
        total_de_tentativas = 5
    else:
        print('Você digitou uma opção inválida!\nTerá apenas uma tentativa.')
        total_de_tentativas = 1
    '''
    rodada = 1
    
    while rodada <= total_de_tentativas:
        print("Tentativa {} de {}".format(rodada, total_de_tentativas), end=".\n")
        chute = int(input('Digite um número: '))
        print('Você digitou', chute, end='.\n')
    
        acertou = numero_secreto == chute
        maior   = chute > numero_secreto
        menor   = chute < numero_secreto
    
        if acertou:
            print('Você acertou', end='!\n')
        else:
            if maior:
                print('Ah que pena!\nVocê digitou um número maior que o número secreto', end='.\n')
            elif menor:
                print('Ah que pena!\nVocê digitou um número menor que o número secreto', end='.\n')
        rodada += 1
      '''
    for rodada in range(0, total_de_tentativas, 1):
        print("Tentativa {} de {}".format(rodada + 1, total_de_tentativas), end=".\n")
        chute = int(input('Digite um número entre 1 e 100: '))
        print('Você digitou', chute, end='.\n')

        if chute < 1 or chute > 100:
            print('Atenção!!!\nVocê digitou um número não permitido.')
            continue
        acertou = numero_secreto == chute
        maior   = chute > numero_secreto
        menor   = chute < numero_secreto

        if acertou:
            print('Você acertou!\nNúmero secreto era {} e você fez {} pontos'.format(numero_secreto,pontos), end='!\n')
            break
        else:
            if maior:
                print('Ah que pena!\nVocê digitou um número maior que o número secreto', end='.\n')
                if rodada + 1 == total_de_tentativas:
                    print("O número secreto era {}. Você fez {} pontos.".format(numero_secreto, pontos))
            elif menor:
                print('Ah que pena!\nVocê digitou um número menor que o número secreto', end='.\n')
                if rodada + 1 == total_de_tentativas:
                    print("O número secreto era {}. Você fez {} pontos.".format(numero_secreto, pontos))
        pontos_perdidos = round(abs(numero_secreto - chute))# Função abs faz calculos transformando numeros negativos em positivos
        pontos = pontos - pontos_perdidos

    print('Fim do jogo', end='!!!')
    Jogos.escolha_jogo()
if __name__ == '__main__':
    jogar()