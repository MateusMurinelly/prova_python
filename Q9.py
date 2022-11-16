numero = float(input('Digite um numero: '))
if numero == 0:
    print(f'O numero {numero} é neutro ')
elif numero % 2 == 0:
    print(f'O numero {numero} É PAR')
else:
    print(f'O numero {numero} É IMPAR')