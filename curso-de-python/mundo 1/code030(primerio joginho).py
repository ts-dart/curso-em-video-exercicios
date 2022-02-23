from random import randint
n = randint(1,3)
print(n)
print('====== lets play ==========')
n1 = str(input('Ola qual o seu nome: '))
print('Ola {} vamos jogar? comutador vai gerar um numero aleatoriamente tente descobrir qual e esse numero'.format(n1))
n2 = int(input('De 0 a 3 qual o numero que o computador escolheu: '))
if n2 == n:
    print('Parabens {} voçe acertou o numero escolido foi {}'.format(n1,n))
else:
    while n2 != n:
        print('Que pena {} o numero escolido foi {} Nao foi dessa vez tente de novo'.format(n1,n))
    if n2 == n:
            print('Voce acertou')
print('============================')
