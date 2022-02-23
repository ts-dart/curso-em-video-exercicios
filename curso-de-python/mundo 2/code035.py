n1 = int(input('Digite um numero: '))
n2 = int(input('Digite um numero: '))
if n1 > n2:
    print('O primeiro numero {} e maior que o segundo {}'.format(n1,n2))
elif n2 > n1:
     print('O segundo numero {} e maior que o primeiro nuemero {}'.format(n2,n1))  
else:
    print('Os dois numeros {} e {} sao iguais'.format(n1,n2))