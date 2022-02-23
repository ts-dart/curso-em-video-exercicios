#declaraçao de variaveis
vc = float(input('Qual e o valor da casa que voce prretende comprar R$: '))
sal = float(input('Qual e o seu salario R$: '))
ano = int(input('Em quantos anos pretende pagar a casa: '))
#cauculo 
pa = vc / ano
pm = pa / (6 + 6)
sa = sal * 30 / 100
#estrutura condicional
if pm > sa:
    print('Com o salario de R${} a sua parcela mensao corresponde ''30%'' do se salario o que da R${} do seu salario mensal seu emprestimo foi negado'.format(sal,sa))
else:
    print('O seu emprestimo foi APROVADO a sua parcela mensl sera de R${}'.format(pm))               