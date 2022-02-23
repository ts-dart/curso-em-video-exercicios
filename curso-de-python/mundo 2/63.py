c = 0
n = 0
while True:
    c = int(input('Digite um numero: '))
    if c == 999:
        break
    n = n + c
print('{}'.format(c))
print('A soma dos numeros foi {}'.format(n))
