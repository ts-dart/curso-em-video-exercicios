from random import randint
n = 0
c = 0
while n != 2:
    n = randint(1,10)
    print(n)
    c = c + 1
    if n == 2:
        for r in range(2):
            print('ola muundo')
    else:
        if n != 2:
            for t in range(2):
                print('nao ola mundo')
print('foram {} tentativas'.format(c))
