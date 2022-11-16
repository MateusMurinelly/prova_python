#Programa compreende as questões 16 e 17
nome = input('digite seu nome: ')
endereco = input('digite seu endereço: ')
idade = input('digite sua data de nascimento: ')
cpf = input('digite seu CPF: ')
nacio = input('Digite seu pais de origem: ')
dicionario = {'nome': nome,
              'endereço': endereco,
              'nascimento': idade,
              'CPF': cpf,
              'nacionalidade': nacio}

print(dicionario['nome'])
print(dicionario['endereço'])
print(dicionario['nascimento'])
print(dicionario['CPF'])
print(dicionario['nacionalidade'])