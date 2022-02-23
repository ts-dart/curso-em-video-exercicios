import random
au = str(input('Digite o nome do primeiro aluno: '))
ad = str(input('Digite o nome do segundo alno: '))
at = str(input('Digite o nome do terceiro aluno: '))
aq = str(input('Digite o nome do quarto aluno: '))
l = [au, ad, at, aq]
v = random.choice(l)
print('o aluno escolido foi {}'.format(v))