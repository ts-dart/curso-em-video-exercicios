from random import randint
i = ''
p = ''
fim = ''
while True:
    jc = randint(1,9)
    jj = int(input('Vamos jogar par o impar, Digite um numero: '))
    es = str(input('Escolha [I] para IMPAR OU [P] para PAR: ')).upper()
    tt = jc + jj
    re = tt % 2
    if re == 0:
        fim = 'PAR'
    else: 
        if re == 1:
            fim = 'IMPAR'
    if es in p and re == 0:
        print('O Parabens voce venceu o resutado final foi {} com sobra {} - {}'.format(tt,re,fim))
    else:
        break
print('O computador venceu o resutado final foi {} com sobra {} - {}'.format(tt,re,fim))
            
                                                                                                                                                                                                                                                                                           
































