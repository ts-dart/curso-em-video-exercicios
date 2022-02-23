from math import factorial
n = int(input('Digite um numero e veja o seu valor fatorial: '))
c = n
v = factorial(c)
while c > 0:
    print('{}'.format(c,v))
    c = c - 1
print('O resultado e {}'.format(v))