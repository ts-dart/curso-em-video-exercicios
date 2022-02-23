resp = 'S'
soma = quant = media = maior = menor = 0
while resp in 'Ss':
    num = int(input('Digite um numero: '))
    soma = soma + num
    quant = quant + 1
    if quant == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num 
        if num < menor:
            menor = num
    resp = str(input('Quer continuar S/N: ')).upper().strip()[0]
m = soma / quant
print('{} numeros {} media',format(quant,media))
print('maior {] menor {}',format(maior,menor))    

    
