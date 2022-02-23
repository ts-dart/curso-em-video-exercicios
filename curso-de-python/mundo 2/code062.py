n = int(input('Digite um numero: '))
md = 0
ma = 0
me = 0
c = 0
while n != '-':
    nx = str(input('Voce quer continuar [S/N]: '))
    c = c + 1
    if nx in 'Ss':
       n = int(input('Digite outro valor: '))
    else:
        if nx in 'Nn':
            print('Programa encerrado')
md = n / nx
if c == 1:
    ma = n
else:
    if n > ma:
        ma = n 
if c < md:
    me = n
print('A media dos numeros digitados foi: {}'.format(md))
print('O maior e {} e o menor e {}'.format(ma,me))
