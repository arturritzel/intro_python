a = float(input("Digite o valor de a: "))
b = float(input("Digite o valor de b: "))
c = float(input("Digite o valor de c: "))

dobroa = a+a
quatac = 4*a*c
bquad = b*b
menosb = b*-1
delta = bquad-quatac
raiz = float(delta) ** 0.5

resultado1 = (menosb + raiz)/dobroa
resultado2 = (menosb - raiz)/dobroa
print("")
print("")
print(f"{a}x² + {b}x + c")
print("")
print("Resultados:")
print("x'  =", resultado1)
print("x'' =", resultado2)
print("")
print("a =", a)
print("b =", b)
print("c =", c)
print("")
print("delta:", delta)
