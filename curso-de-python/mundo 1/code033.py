n1 = int(input('Digite um valor: '))
n2 = int(input('Digite um valor: '))
n3 = int(input('Digite um valor: '))
print('-')
if n1<n2 and n1<n3:
    m = n1 
    print('O numero de menor valor e {}'.format(m))
if n2<n1 and n2<n3:
    m2 = n2
    print('O numero de menor valor e {}'.format(m2))
if n3<n1 and n3<n2:
    m3 = n3
    print('O nuemro de menor valor e {}'.format(m3))    
print('-')
if n1>n2 and n1>n3:
    m4 = n1
    print('O numero de maior valor e {}'.format(m4))
if n2>n1 and n2>n3:
    m5 = n2
    print('O numero de maior valor e {}'.format(m5))
if n3>n1 and n3>n2:
   m6 = n3
   print('O numero de maior valor e {}'.format(m6))
print('-')
