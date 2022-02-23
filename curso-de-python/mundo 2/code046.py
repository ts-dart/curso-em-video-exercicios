soma = 0
cont = 0
for c in range(2, 501, 2):
    if c % 3 == 0:
        print(c) 
        cont = cont + 1
        soma = soma + c
print('a soma de todos os valoes {} soliccitados e {}'.format(cont,soma))