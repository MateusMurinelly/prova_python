def media(nota1,nota2):
    x = nota1+nota2/2
    return x

aluno1 = []
for i in range(2):
    nota = float(input(f'digite a {i+1}ª nota do aluno 1: '))
    aluno1.append(nota)
    somas = media(nota,nota)
print(aluno1)
print(somas)


aluno2 = []
for i in range(2):
    nota = float(input(f'digite a {i+1}ª nota aluno 2: '))
    aluno2.append(nota)
    somas2 = media(nota,nota)
print(aluno2)
print(somas2)
print(f'A soma das medias é {somas+somas2}')