n = int(input('Digite um numero entre 0 e 10: '))
if n <= 10:
    print('O numero digitado foi {}'.format(n))
while n > 10:
    print('ERRO')
    n = int(input('Digite um numero valido'))
    if n <= 10:
        print('O numero digitado foi {}'.format(n))
