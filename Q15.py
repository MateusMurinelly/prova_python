listaid = []
for i in range(5):
    idade = int(input(f'digite a {i+1}° idade: '))
    listaid.append(idade)
print(listaid)
maiores = [x for x in listaid if x > 17]
print(maiores)
print(f'A soma das idades é {sum(listaid)}')
media = sum(listaid)/len(listaid)
print(f'A media das idades é {media}')
print(f'O maior valor é {max(listaid)}')
print(f'O menor valor é {min(listaid)}')
listaid.sort()
print(f'As idades em ordem cresente são: {listaid}')
listaid.sort(reverse=True)
print(f'As idades em ordem cresente são: {listaid}')