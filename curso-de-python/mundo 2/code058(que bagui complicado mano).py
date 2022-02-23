pn = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razao da PA: '))
t = pn
c = 1 
tt = 0
m = 10
while m != 0:
    tt = tt + m
    while c <= tt:
        print('{}'.format(t))
        t = t + r
        c = c + 1
    m = int(input('Quantos termos a mais voce quer : ')) 
print('FIM')