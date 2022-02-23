sexo = str(input('Informe se sexo: ')).strip().upper()[0]
while sexo not in 'MnFf':
    sexo = str(input('erro, Informe se sexo: ')).strip().upper()[0]
print('sexo {} registrado'.format(sexo))
    
