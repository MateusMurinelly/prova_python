n1 = float(input('informe 1º numero: '))
n2 = float(input('informe 2º numero: '))
n3 = float(input('informe 3º numero: '))
n4 = float(input('informe 4º numero: '))
n5 = float(input('informe 5º numero: '))
soma = n1+n2+n3+n4+n5
print(f'A soma dos valores é {soma}')
if n1 > n2 and n1 > n3 and n1 > n4 and n1 > n5:
    print(f'{n1} é o maior')
elif n2 > n1 and n2 > n3 and n2 > n4 and n2 > n5:
    print(f'{n2} é o maior')
elif n3 > n2 and n3 > n1 and n3 > n4 and n3 > n5:
    print(f'{n3} é o maior')
elif n4 > n1 and n4 > n2 and n4 > n3 and n4 > n5:
    print(f'{n4} é o maior')
elif n5 > n1 and n5 > n2 and n5 > n3 and n5 > n4:
    print(f'{n5} é o maior')