def soma(x,y):
    calculo = x+y
    return calculo


def subtracao(x,y):
    calculo = x-y
    return calculo


def multiplicacao(x,y):
    calculo = x*y
    return calculo


def divisao(x,y):
    calculo = x/y
    return calculo

x = int(input('digite um numero: '))
y = int(input('digite o segundo numero: '))
print(soma(x,y))