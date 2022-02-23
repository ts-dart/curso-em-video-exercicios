from random import randint
n = randint(1,10)
p = 0
n2 = int(input('Adivinhe o numero que o comptador escolheu entre 1 a 10: '))
if n == n2:
    print('Voce acertou {} e igual {} na {} vez'.format(n,n2,p))
else:
    while n != n2:
        print('Voce errou {} e difeerente de {}'.format(n,n2))
        n2 = int(input('Tente outra vez: '))
        p = p + 1
        if n == n2:
            print('voce aceerto na {} vez'.format(p))