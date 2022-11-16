print('_'*30)
print('menu de digitos')
print('_'*30)
print(' [1] para digitar um numero\n [2] para digitar uma palavra\n [3] para booleanos\n [4] para sair')

while True:
    opcao = int(input('digite qual opção você deseja: '))
    if opcao == 1:
        numero = input('Digite seu numero: ')
        if numero.isdecimal() == False:
            numero = float(numero)
            print(type(numero))
            break
        else:
            numero = int(numero)
            print(type(numero))
            break
    elif opcao == 2:
        palavra = input('digite a sua palavra: ')
        print(type(palavra))
        break
    elif opcao == 3:
        booleano = input('digite algo: ')
        booleano = bool(booleano)
        print(type(booleano))
        break

    elif opcao == 4:
        desejo = input('deseja realmente sair?\n [s] para sim\n [n] para não: ').lower()
        if desejo == 's':
            print('Adeus')
            break
        elif desejo == 'n':
            opcao
