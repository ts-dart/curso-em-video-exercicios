f = str(input('Digite seu nome: ')).strip()
print('ANALISANDO SEU NOME...')
print('seu nome todo em maiusculo e : {}'.format(f.upper()))
print('seu nome todo em minusculo e: {}'.format(f.lower()))
print('seu nome {} tem ao todo {} letras'.format(f,len(f) - f.count(' ')))
s = f.split()
print('O seu primeiro nome e {} e ele tem {} letras'.format(s[0],len(s[0])))

