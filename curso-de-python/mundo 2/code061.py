c = 0
s = 0
n = 0
n = int(input('Digite um numero '))
while n != 999:
    c = c + 1 
    s = s + n
    n = int(input('Digite um numero '))
print('foram digitados {} numeros e a soma deles e {}'.format(c,s))

