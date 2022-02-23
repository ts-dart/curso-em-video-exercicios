print('Alugel do carro')
print('=====================')
km = float(input('Quantos quilometros o carro percorreu km: '))
di = int(input('Quantos dias o carro ficou alugado: '))
pd = di * 60
pk = km * 0.15
vp = pd + pk
print('o preço do alugel foi de {}'.format(vp))
