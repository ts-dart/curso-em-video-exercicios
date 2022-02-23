vl = int(input('Qual foi a velocidade do carro: '))
if vl > 80:
    print('Voce utrapasou o limite de velocidade e sera mutado')
    m = vl - 80
    m2 = m * 7
    print('O valor da muta e de {}'.format(m2)) 
else:
    print('tenha uma boa viagem') 