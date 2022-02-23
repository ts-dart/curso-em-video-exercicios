m = f = s = n = ''
while True:
    i = int(input('Idade: '))
    s = str(input('Seu sexo? M/F:')).strip().upper()
    resp = str(input('Quer continuar? S/N:')).strip().upper()
    if resp == 'N':
        break