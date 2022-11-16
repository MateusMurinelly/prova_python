altura = float(input('Digite sua altura em metros: ').replace(',','.'))
peso = float(input('Digite seu peso em Kg: '))

imc = peso / altura ** 2

print('Seu IMC é: %.4f' % imc)

if imc < 16:
    print('Magreza grave')
elif imc < 17:
    print('Magreza moderada')
elif imc < 18.5:
    print('Magreza leve')
elif imc < 25:
    print('Saudável')
elif imc < 30:
    print('Sobrepeso')
elif imc < 35:
    print('Obesidade Grau 1')
elif imc < 40:
    print('Obesidade Grau 2')
else:
    print('Obesidade Grau 3')