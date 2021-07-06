numtabuada = int(input("digite o número que deseja ver a tabuada: "))
initabuada = int(input("número base inicial: "))
fintabuada = int(input("número base final: "))
print("")


for numero in range ((initabuada),(fintabuada)):
    mult = numero * numtabuada
    print(f"{numero} * {numtabuada} = {mult}")
