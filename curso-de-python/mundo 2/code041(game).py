from random import randint
l = ['Pedra', 'Papel', 'Tesoura']
jc = randint(0,2)
print('')
print('')
print('{:^40}'.format('JOKENPO GAME'))
print('-=' * 20)
print('''SUAS OPIÇÕES SÃO
[0] APERTE 0 PARA JOGAR PEDRA
[1] APERTE 1 PARA JOGAR PAPEL
[2] APERTE 2 PARA JOGAR TESOURA''')
print('{:^40}'.format('-'))
jj = int(input('Qual e a sua jogada? '))
print('O jogador jogou {} e o computador jogou {}'.format(l[jj],l[jc]))
print('{:^40}'.format('-'))
if jc == 0:
    if jj == 0:
        print('EMPATE')
    elif jj == 1: 
        print('JOGADOR VENCEU')
    elif jj == 2:
        print('COMPUTADOR VENNCEU')
if jc == 1:
    if jj == 0:
        print('COMPUTADOR VENCEU')
    elif jj == 1: 
        print('EMPATE')
    elif jj == 2:
        print('JOGADOR VENCEU')
if jc == 2:
    if jj == 0:
        print('JOGADOR VENCEU')
    elif jj == 1: 
        print('COMPUTADOR VENCEU')
    elif jj == 2:
        print('EMPATE')
print('-=' * 20)
print('')
print('')
