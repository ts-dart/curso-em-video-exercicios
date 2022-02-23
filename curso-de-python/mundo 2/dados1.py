tot18 = totH = totM20 = 0
while True:
    i = int(input('idade: '))
    s = ''
    while s not in 'MF':
        s = str(input('Sexo: M/F: ')).strip().upper()[0]
    if i >= 18:
        tot18 += 1
    if s == 'M':
        totH += 1
    if s == 'F' and i < 20:
        totM20 += 1
    resp = ''
    while resp not in 'SN':
        resp = str(input('Quer continuar? S/N: ')).strip().upper()[0]
    if resp == 'N':
        break
print('total de pessoas com mais de 18 anos: {}'.format(tot18))
print('ao todo temos {} homens cadastrados'.format(totH))
print('e temos {} mulheres com menos de 20 anos'.format(totM20))

