from random import randint
itens = ('pedra', 'Papel', 'Tesoura')
while (itens != '0, 1, 2'): #enquanto a opção é 0, 1 e 2 o jogo continua.
    print ('''Opções:
        [ 0 ] Pedra
        [ 1 ] Papel
        [ 2 ] Tesoura''')
    usuário = int(input('escolha uma opção:  '))
    print ('-=' * 10)
    print ('Você escolheu  {}'.format (itens [usuário]))
    computador = randint (0,2)
    print ('O computador escolheu {}'.format (itens[computador]))
    print ('-=' * 10)
    if computador == 0: #pc jogou pedra
        if usuário == 0:
            print ('Vocês empataram')
        elif usuário == 1:
            print ('Computador venceu!')
        elif usuário == 2:
            print ('Computador venceu! ')
        else:
            print ('Jogada inválida!')
    if computador == 1: #pc jogou papel
        if usuário == 0:
            print ('Computador venceu')
        elif usuário == 1:
            print ('Vocês empataram')
        elif usuário == 2:
            print ('Você Ganhou!')
        else:
            print ('Jogada inválida!')
    if computador == 2: #pc jogou tesoura
        if usuário == 0:
            print ('Você ganhou')
        elif usuário == 1:
            print ('Computador ganhou')
        elif usuário == 2:
            print ('Vocês empataram')
        else:
             print ('Jogada inválida')