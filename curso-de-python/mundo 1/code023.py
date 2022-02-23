from random import shuffle
nu = str(input('Digite o nome da primeira pessoa: '))
nd = str(input('Digite o nome da segunda pessoa: '))
nt = str(input('Digite o ome da terceira pessoa: '))
nq = str(input('Digite o nome da quarta pessoa: '))
l = [nu, nd, nt, nq]
v = shuffle(l)
print('a ordem da lista e')
print(l)
