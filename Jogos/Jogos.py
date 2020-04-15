import Forca
import Adivinhacao
def escolha_jogo():
    print('*********************************')
    print('       Escolha o seu jogo!       ')
    print('*********************************')
    print('Selecione uma opção:')
    jogo = int(input('1.Forca.\n2.Adivinhação.\n3.Sair\nDigite aqui: '))
    if jogo == 1:
        print('Você escolheu jogo da forca!')
        Forca.jogar()
    elif jogo == 2:
        print('Você escolheu jogo da Adivinhação!')
        Adivinhacao.jogar()
    elif jogo == 3:
        print('Você escolheu sair do jogo!')

if __name__ == '__main__':
    escolha_jogo()