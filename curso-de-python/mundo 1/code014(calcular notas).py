from random import choice
print('{:^40}'.format('-'))
print('Boletin escolar')
print('{:^40}'.format('-'))
l1 = ['thiago', 'lucas', 'sandra', 'ana']
v1 = choice(l1)
print('Digite o nome do aluno: {}'.format(v1))
l2 = ['1 ano', '2 ano', '3 ano']
v2 = choice(l2)
print('Digite o ano de {}: {}'.format(v1, v2))
l3 = [111, 110, 105, 210]
v3 = choice(l3)
print('Digite a turma de {}: {}'.format(v1, v3))
print('{:^40}'.fomat('-'))
mat = float(input('Dgite a nota de matematica: '))
pot = float(input('Digite a nota de portugues: '))
qui = float(input('Digite a nota de qimica: '))
fis = float(input('Digite a nota de fisica: '))
geo = float(input('Digite a nota de geografia: '))
his = float(input('Digite a nota de historia:'))
s = mat + pot + qui + fis + geo + his
m = s / 6
print('ALUNO: {}   ANO: {}   TURMA: {}'.format(v1, v3, v2))
if m < 40:
    print('A media anual de {} foi: {:.3} REPROVADO'.format(v1, m))
elif m < 60:
    print('A media anual de {} foi: {:.3} RECUPERAÇAO'.format(v1, m))
else:
    print('A media anual de {} foi: {:.3} APROVADO: '.format(v1, m))
print('{:^40}'.format('-'))
print('{:^40}'.format('-'))
