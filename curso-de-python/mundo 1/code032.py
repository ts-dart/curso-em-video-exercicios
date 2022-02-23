v = float(input('Qual e a distancia da viagem: '))
if v <= 200:
    s = v * 0.50
    print('O preço da viagem de {}km e de R${}'.format(v,s))
else:
    s2 = v * 0.45
    print('O preço da viagme de {}km e de R${}'.format(v,s2))
print('Tenha ma boa viagem')