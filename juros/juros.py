capital = int(input("digite a capital: "))
taxa = int(input("digite a taxa de juros mensal (sem %): "))
meses = int(input("digite a quantidade de meses: "))
print("")

taxa100 = taxa/100
juroscapital = capital

print(f"mês 0: {juroscapital:.2f}")
for mes in range (0, meses):
    juroscapital = juroscapital + (juroscapital * taxa100)
    print(f"mês {mes+1}: {juroscapital:.2f}")

print("")
print(f"total a pagar: {juroscapital:.2f}")
print(f"juros: {juroscapital-capital:.2f}")
print(f"capital inicial: {capital}")
