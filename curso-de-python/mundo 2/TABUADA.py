print('TABUADA')
while True:
    n = int(input('Digite um numero e sua tauada sera mostrada: '))
    if n < 0:
        break
    for c in range(1,11):
        print('{} x {} + {}'.format(n,c,n*c))
print('PROGRAMA ENCERRADO, :)')