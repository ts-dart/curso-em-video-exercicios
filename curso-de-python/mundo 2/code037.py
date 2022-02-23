no = str(input('Qual o nome do aluno: '))
tu = int(input('Qual e a turma de {}: '.format(no)))
an = int(input('Qual e o ano de {}: '.format(no)))
n1 = int(input('Qual a primeira nota de {}: '.format(no)))
n2 = int(input('Qual a segunda nota do aluno {}: '.format(no)))
n3 = int(input('Qual a terceira nota do aluno {}: '.format(no)))
m = n1 + n2 + n3 / 3
print('-')
print('ALUNO: {}   TURMA: {}   ANO: {}'.format(no,tu,an))
print('-')
if m < 60:
    print('O aluno {} esta de REPROVADO sua media foi {}'.format(no,m))
elif m > 50 and m < 60:
    print('O aluno {} esta de RECUPERAÇAO sua media foi {}'.format(no,m))
else:
    print('O aluno {} esta APROVADO sua media foi {} PARABENS'.format(no,m))
print('-')