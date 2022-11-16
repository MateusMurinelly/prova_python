def positivoounegativo(numero):
    if numero > 0:
        print(f'O numero {numero} é positivo')
    else:
        print(f'O numero {numero} é negativo')

x = float(input('digite um numero para ser verificado: '))
print(positivoounegativo(x))