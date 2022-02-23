ma = 0 
me = 0 
for t in range(1,6):
    p = float(input('{} Pessoa qual e o seu peso? '.format(t)))
    if t == 1:
        ma = p
        me = p 
    else:
        if p > ma:
            ma = p
        if p < me:
            me = p
print('O maior peso digitado foi o {}'.format(ma))
print('O menor peso digitado foi o {}'.format(me))