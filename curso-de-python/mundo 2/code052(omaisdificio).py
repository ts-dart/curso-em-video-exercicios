#variaveis
mi = 0
mv = ''
s2 = ''
m20 = 0
for r in range(1,5):
    n = str(input('Pessoa {} qual e seu nome? '.format(r)))
    s = str(input('Pessoa {} qual e o seu sexo? [M,F]'.format(r)))
    i = int(input('Pessoa {} qual e a sua idade? '.format(r)))
    print('{:^3}'.format('-='))
#mais velho
    if r == 1:
        mi = i
        mv = n
    else:
        if i > mi and s2 in 'Mm':
            mi = i
            mv = n
#mulher-20  
    if i < 20 and s in 'Ff':
        m20 = r
#media de idade
md = i / 4
#resutado
print('A media de idade das pessoas acima e {}'.format(md))
print('O homem mais velho e {} e tem {} anos'.format(mv,mi))
print('{} mulheres tem menos de 20 anos'.format(m20))
for h in range(1,11):
    print('Aeeeeeeee BOOOM BOOOM COMPILOOOOOUUUU')
