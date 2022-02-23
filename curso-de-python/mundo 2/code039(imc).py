print('-Cauclando o IMC-')
print('-')
n = str(input('Qual e o seu nome: '))
p = float(input('{} Qual e o seu peso: '.format(n)))
a = float(input('{} Qual e a sua altura: '.format(n)))
imc = p / (a ** 2)
print('{} Seu IMC e de {:.3}'.format(n,imc))
if imc < 18.5:
    print('{} esta abaixo do peso'.format(n))
elif imc > 18.5 and imc < 25:
    print('{} esta com o peso ideal'.format(n))
elif imc > 25 and imc < 30:
    print('{} esta com sobre peso'.format(n))
elif imc > 30 and imc < 40:
    print('{} esta com obesidade'.format(n))
else:
    print('{} esta com obesidade morbida'.format(n))