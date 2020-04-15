from usuario import Usuario

continuar = 1
lista_usuarios =[]

while continuar != 0:
    try:
        nome = input('Digite seu nome: ')
        idade = int(input('Digite sua idade: '))
        sobrenome = input('Digite seu sobrenome: ')
        usuario = Usuario(nome, idade, sobrenome)

        lista_usuarios.append(usuario)

        if usuario.idade == 99:
            break

        if usuario.idade == 98:
            continue

        print(f'Olá, {usuario.nome} {usuario.sobrenome}, sua idade é {usuario.idade}.  ')

        if usuario.idade >=1 and usuario.idade <= 11:
            print(f'{usuario.nome} é adolecente.')

        elif usuario.idade >= 12 and usuario.idade <= 17:
            print(f'{usuario.nome} é adolecente.')

        elif usuario.idade >= 18 and usuario.idade <= 50:
            print(f'{usuario.nome} é adulto.')

        else:
            print(f'{usuario.nome} é idoso.')
        continuar = int(input('Deseja sair?\n0. Sim\n1. Não '))
        if continuar == 0:
            print('Saindo...')

        else:
            while continuar != 1:
                continuar = int(input('Opção Inválida!!\nDeseja sair?\n0. Sim\n1. Não '))
                if continuar == 0:
                    print('Saindo...')
    except ValueError:
        print("Erro!\nVocê deve informar um número válido.")


else:
    print('Lista de usuários: ')
    for usuario in lista_usuarios:
        print(f'Nome Completo: {usuario.nome} {usuario.sobrenome} Idade: {usuario.idade}.')
