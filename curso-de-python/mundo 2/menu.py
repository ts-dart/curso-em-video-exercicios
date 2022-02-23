n = int(input('Digite um numero: '))
n2 = int(input('Digite outro numero: '))
print('''ESSA SAO SUAS OPÇOES
[1] SOMAR OS DOIS NUMEROS 
[2] MUTIPLICAR OS DOIS NUMEROS
[3] MOSTRAR O MAIOR ENTRE ELES
[4] PARA DIGITAR NOVOS NUMEROS 
[5] PARA ENCERRAR O PROGRAMA ''')
r = int(input('Qual a sua opçao: '))
if r == 1:
    s = n + n2
    print('A soma dos numeros digitados e {}'.format(s))
elif r == 2:
    m = n * n2
    print('A mutiplicaçao dos numeros digitados e {}'.format(m))
elif r == 3:
    if n < n2:
        print('O segundo {} numero e o maior'.format(n2))
    else:
        if n2 < n:
            print('O primeiro numero {} e maior'.format(n))
while r == 4:
    print('Digite novamente os numeros')
    n = int(input('Digite um numero: '))
    n2 = int(input('Digite outro numero: '))
    print('''ESSA SAO SUAS OPÇOES
    [1] SOMAR OS DOIS NUMEROS 
    [2] MUTIPLICAR OS DOIS NUMEROS
    [3] MOSTRAR O MAIOR ENTRE ELES
    [4] PARA DIGITAR NOVOS NUMEROS 
    [5] PARA ENCERRAR O PROGRAMA ''')
    r = int(input('Qual a sua opçao: '))
    if r == 1:
        s = n + n2
        print('A soma dos numeros digitados e {}'.format(s))
    elif r == 2:
        m = n * n2
        print('A mutiplicaçao dos numeros digitados e {}'.format(m))
    elif r == 3:
        if n < n2:
            print('O segundo {} numero e o maior'.format(n2))
        else:
            if n2 < n:
                print('O primeiro numero {} e maior'.format(n))
if r == 5:
    print('PROGRAMA ENCERRADO, volte sempre')



