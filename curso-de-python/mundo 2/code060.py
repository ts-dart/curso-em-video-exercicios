n = int(input('Digite um numero: '))
t1 = 0
t2 = 1
t3 = t1 + t2
c = 3
print(' .{}'.format(t1))
print(' .{}'.format(t2))
while c <= n:
    t3 = t1 + t2
    print(' .{}'.format(t3))
    c = c + 1
    t1 = t2
    t2 = t3
print('FIM')
