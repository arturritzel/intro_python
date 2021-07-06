nota = 0
notasquant = 0
notatotal = 0

while nota != 999:
    nota = int(input("Digite uma nota do aluno ou 999 para sair: "))
    if nota != 999:
        notasquant += 1
        notatotal += nota

media = notatotal / notasquant

print(f"media das notas do aluno: {media:.2f}")
