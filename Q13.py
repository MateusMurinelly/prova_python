listap = []
listai = []
for i in range(10):
    numero = int(input(f'digite o {i+1}º numero: '))
    if numero == 0:
        print(f'O numero {numero} é neutro mas dessa vez ele será PAR')
        listap.append(numero)
    elif numero % 2 == 0:
        print(f'O numero {numero} É PAR')
        listap.append(numero)
    else:
        print(f'O numero {numero} É IMPAR')
        listai.append(numero)

print(listai)
print(listap)
somap = sum(listap)
somai = sum(listai)
print(f'A soma da lista dos pares é {somap}')
print(f'A soma da lista dos impares é {somai}')
somag = somai + somap
print(f'A soma geral é {somag}')