nome = input("digite o nome do aluno: ")
print("")

nota1 = float(input("digite o valor da primeira nota: "))
nota2 = float(input("digite o valor da segunda nota: "))
nota3 = float(input("digite o valor de terceira nota: "))
print("")

media = (nota1 + nota2 + nota3)/3

print(f"a média de {nome} é {media:.2f}")
print("")
if media < 5:
    print(f"{nome} foi reprovado(a)")
if 7 >= media >= 5:
    print(f"{nome} está de recuperação.")
if media > 7:
    print(f"{nome} foi aprovado(a)")
