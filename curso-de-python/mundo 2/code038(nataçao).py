from datetime import date
print('--Confederação Nacional de Natação--')
nome = str(input('Digite o nome do atleta: '))
ano = int(input('Digite o ano de nacimento do atleta {}: '.format(nome)))
aa = date.today().year
af = aa - ano 
print('{} tem {} anos'.format(nome,af))
if af < 9:
   print('{} e um atleta MIRIM'.format(nome))
elif af > 9 and af < 14:
    print('{} e um atleta INFANTIL'.format(nome))
elif af > 14 and af < 19:
    print('{} e um atleta JUNIOR'.format(nome))
elif af > 19 and af < 25:
    print('{} e um atleta SENIOR'.format(nome))
else:
    print('{} e um atleta MASTER'.format(nome))
    