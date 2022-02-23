import datetime
ano = int(input('Digite o ano em que vc naceu: '))
at = datetime.date.today().year
c = at - ano
if c < 18:
    f = 18 - c
    print('Voce tem {} anos ainda e menor de idade e ira se alistar daqui a {} anos'.format(c,f))
elif c == 18:
    print('Voce tem {} anos procure o local de alistamento da sua cidade'.format(c))
elif c > 18:
    f = c - 18
    print('Voce tem {} anos e passou do tempo de se alistar a {} anos'.format(c,f))