#Referente as questões 7 e 7.1
print('_'*30)
print('menu de temperaturas')
print('_'*30)
print(' [1] para Celcius\n [2] para Fahrenheit')
opcao = int(input('digite sua opção: '))
if opcao == 1:
    temperatura = float(input('digite a temperatura em C°: '))
    fah = (temperatura * 9/5) + 32
    print(f'Sua temperatura em Fahrenheit é igual {fah}°')
elif opcao == 2:
    temperatura = float(input('digite a temperatura em F°: '))
    cel = (temperatura - 32) * 5/9
    print(f'Sua temperatura em Celcius é igual {cel}°')

