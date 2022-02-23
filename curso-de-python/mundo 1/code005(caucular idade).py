from random import  choice, randint
print('=============================')
n = str(input('Ola como e o seu nome: '))
print('ola {} prazer em conhecelo'.format(n))
id = randint(1,90)
print('entao {} quantos anos voce tem? {}'.format(n, id))
v = id - 2020
print('entao se voce tem {} voce naceu no ano de {}'.format(id, v))
if id < 12:
    print('voce e uma crianca')
elif id < 18:
    print('voce e um adolecente')
elif id < 65:
    print('voce e um aduto')
else:
    print('voce e um idoso')
print('=============================')



