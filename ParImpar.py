from random import randint
while True:
    tipo = str(input('Escolha par ou impar:  \n')) #Escolha par ou impar
    usuario = int(input('Digite um numero:  \n'))  # Digite um número
    computador = randint (0,10)  #pc escolhe o número de 0 a 10
    total = usuario + computador
    print (f'Você jogou {usuario} e o computador {computador}. Total de {total}')
    if tipo == 'par': #se a escolha for par retorna resposta...
        if total % 2 == 0:
            print ('Você ganhou total é par')
        else:
            print ('Você perdeu total é impar!')
    if tipo == 'impar': #se a soma for impar retorna a resposta...
        if total % 2 == 1:
            print ('Você ganhou total é impar')
        else:
            print ('Você perdeu total é par!')