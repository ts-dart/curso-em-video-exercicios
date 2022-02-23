print('Ola bom tudo bom')
print('iphone x custa R$:4.000')
print('samsung galaxy s10e custa R$:4.500')
print('motorola one custa R$:2.000')
i = float(4.000)
s = float(4.500)
m = float(2.000)
if i < s and i < m:
    print('compre um iphone')
elif s < i and s < m:
    print('compre galaxy s10e')
elif m < i and m < s:
    print('compre moto one')
print('[i] para iphone x')
print('[s] para galay s10e')
print('[m] para moto one')
c = str(input('qual produto voce quer: '))
if c == m:
    print('escolheu o mais barato')
else:
    print('nao escolheu o mais barato foi BURRO')

