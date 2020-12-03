from math import factorial
n = int(input('Digite um numero para calcular seu fatorial: '))
c = n
for c in range (n):
    print ('{}'.format(c), end= '')
    print ('x' if c > 1 else '=', end= '')
    c -= 1


