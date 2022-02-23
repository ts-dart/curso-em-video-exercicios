import datetime
at = datetime.date.today().year
for c in range(1,8,1):
    an = int(input('Qual a sua data de naciemento: '))
    c = at - an
    if c < 18:
        print('voce tem {} anos e naoe aior de idade '.format(c))
    else:
        print('voce tem {} anos e maior de idade'.format(c))