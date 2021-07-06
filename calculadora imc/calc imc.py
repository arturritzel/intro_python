nome = input("Digite seu nome: ")
peso = float(input("Digite seu peso em kg: "))
altura = float(input("Digite seu peso em cm: "))

altura = altura / 100

imc = peso / (altura**2)

print("")
print(f"{nome}, seu imc é {imc:.2f}")
