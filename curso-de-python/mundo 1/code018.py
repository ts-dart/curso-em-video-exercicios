print('Algoritimo que calcuala descotos')
print('=================================')
np = str(input('Digite o nome do produto: '))
vp = float(input('Digite o valor do produto R$: '))
de = float(input('Digite o valor do deconto R$: '))
vf = vp * de/100
print('O desconto do produto {} que custa {} com o descoto de {} vai para {}'.format(np, vp, de, vf))