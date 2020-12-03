from random import randint
print ('''Opções:
  [ 0 ] Apresenta febre e tosse seca por mais de 2 dias (os dois sintomas)
  [ 1 ]  Apresenta febre por mais de 3 dias. É considerado febre temperatura corporal a partir de 38ºC
  [ 2 ] Cansaço por mais de 2 dias
  [ 3 ] Falta de ar (idicação de ida imediata, independente dos demais sintomas)
  [ 4 ] Perda de olfato e/ou paladar
  [ 5 ] Contato com alguém suspeito/confirmado do Covid-19 a menos de 14 dias
  [ 6 ] Retorno de viagem a regiões com alto índice de infecção a menos de 14 dias
  ''')
pontos = 0
cont = 0
itens = ('sintoma 0', 'sintoma 1', 'sintoma 2', 'sintoma 3', 'sintoma 4', 'sintoma 5')
r = 'S'
while r == 'S':
  usuário = int(input('escolha uma opção de sintoma:  '))
  r = str(input('Mais algum sintoma? [S/N]  ')).upper()
print ('-=' * 10)
if usuário == 0:
  print ('Leve')
elif usuário == 1 and usuário == 2:
    print ('ir ao medico')
elif usuário == 2:
  print ('ir ao medico')
else:
    print ('sint leves')
if usuário == 1:
  print ('Sint leves')
if usuário == 2:
  print ('Sint leves')
if usuário == 3:
  print ('Ir ao médico imediatamente!')
if usuário == 4:
  print ('Ir ao médico imediatamente!')
if usuário == 5:
  print ('Sint leves')
if usuário == 6:
  print ('Sint leves')