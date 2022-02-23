n = int(input('Digite um numero: '))
for c in range(1,n,1):
    print('{}'.format(c), end=' ')
if n % c == 0:
    print('{} e um numero primo'.format(n), end=' ')
else: 
    print('{} nao e um numero primo'.format(n), end=' ')
        