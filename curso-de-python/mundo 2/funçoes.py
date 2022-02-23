def l():
    print('-------')


def area(l, c):
    a = l * c    
    print('O COMPRIMENTO E {} E A LARGURA E {} CONTUDO A AREA E {}'.format(c,l,a))


l()
c = float(input('Digite o comprimento: '))
l = float(input('Digite a largura: '))
area(l, c)

l()  
