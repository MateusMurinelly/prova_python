horas = int(input('digite a quantidade de HORAS que você permaneceu: '))
if horas == 0 or horas == 1:
    print(f'O valor para {horas}H corresponde a R$ 10,00')
else:
    valor = ((horas-1) * 5) + 10
    print(f'O valor para {horas}H é de R$ {valor},00')