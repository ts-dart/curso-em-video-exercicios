from random import choice, shuffle, randint
from math import sqrt, trunc
n1 = randint(1,1000)
n2 = randint(1,1000)
n3 = randint(1,1000)
print('O primeiro numero selecionado pelo computador foi: {}'.format(n1))
print('O segundo numero selecionado pelo computador foi: {}'.format(n2))
print('O terceiro numero seleionado pelo computador foi: {}'.format(n3))
n1r = sqrt(n1)
n2r = sqrt(n2)
n3r = sqrt(n3)
a = trunc(n1r)
b = trunc(n2r)
c = trunc(n3r)
l = [a, b, c]
shuffle(l)
print('A lista selecionada foi: {}'.format(l))
l2 = [a, b, c]
v = choice(l2)
print('o numero escolido de dentro da lista foi: {}'.format(v))