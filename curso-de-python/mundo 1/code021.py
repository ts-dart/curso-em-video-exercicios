import math
a = float(input('Digite um numero para cucular seu angulo: '))
se = math.sin(math.radians(math.ceil(a)))
cos = math.cos(math.radians(math.ceil(a)))
tan = math.tan(math.radians(math.ceil(a)))
print('O ANGULO DE {} TEM O SENO DE {:.2}'.format(a, se))
print('O ANGULO DE {} TEM O COSENO DE {:.2}'.format(a, cos))
print('O ANULO DE {} TEM A TANGENTE DE {:.2}'.format(a, tan))
