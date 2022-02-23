print('{:=^40}'.format(' LOJAS TA BARATO '))
p = float(input('Qual o valor do produto R$: '))
print('[1] A VISTA NO DINHERO/CHEQUE 10% DE DESCONTO')
print('[2] A VISTA NO CARTAO 5% DE DESCONTO')
print('[3] EM ATE 2x NO CARTÃO PREÇO NORMAL')
print('[4] 3x OU MAIS NO CARTÃO 20%  DE JUROS')
print('[5] SAIR')
print('{:=^40}'.format('='))
op = int(input('Qual e a sua opção de pagamento?: '))
if op == 1:
    n1 = p - (p * 10 / 100)
    print('PAGAMENTO A VISTA (DINHEIRO/CHEQUE) COM 10% DE DESCONTO O PREÇO DE R${} VAI PARA R${}'.format(p,n1))
elif op == 2:
    n2 = p - (p * 5 / 100)
    print('PAGAMENTO A VISTA (CARTÃO) COM 5% DE DESCONTO O PREÇO CAI DE R${} PARA R${}'.format(p,n2))
elif op == 3:
    print('PAGAMENTO EM ATE 2x NO CARTÃO PREÇO NORMAL DE R${}'.format(p))
elif op == 4:
    n3 = p + (p * 20 / 100)
    pa = int(input('Quantas vezes? '))
    pa2 = n3 / pa 
    print('PAGAMENTO EM ATE 3X NO CARTÃO COM JUROS DE 20% O PREÇO VAI DE R${} PARA R${}'.format(p,n3,))
    print('SUA COMPRA SERA PARCELADA EM {}x DE R${:.4}'.format(pa,pa2))
elif op == 5:
    print('OBRIADO PELA SUA VISITA')
else:
    op = 0
    print('ERRO, ESCOLHA UMA DAS OPÇÕES ACIMA')
print('{:=^40}'.format('='))
