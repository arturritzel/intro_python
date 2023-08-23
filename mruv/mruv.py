print("Fórmulas:")
print("Função horária do espaço no MRUV: S = Si + Vi * t + (a*t^2)/2")
print("")

print("1: calcular posição com 5 tempos")
print("2: calcular posição com 1 tempo exato")
print("3: calcular aceleração com V, Vi e t")
print("4: gerar gráficos")
print("")

fisicacalc = float(input("calculadora: "))
print("")

if fisicacalc == 1:

    Si = float(input("Si: "))
    Vi = float(input("Vi: "))
    a = float(input("a: "))
    t1 = float(input("t1: "))
    t2 = float(input("t2: "))
    t3 = float(input("t3: "))
    t4 = float(input("t4: "))
    t5 = float(input("t5: "))
    print("")

    S = Si + Vi * t1 + (a*(t1*t1))/2
    V = Vi + a * t1

    print(f"t = {t1}")
    print(f"S = {S}")
    print(f"V = {V}")
    print("")

    S = Si + Vi * t2 + (a*(t2*t2))/2
    V = Vi + a * t2

    print(f"t = {t2}")
    print(f"S = {S}")
    print(f"V = {V}")
    print("")

    S = Si + Vi * t3 + (a*(t3*t3))/2
    V = Vi + a * t3

    print(f"T = {t3}")
    print(f"S = {S}")
    print(f"V = {V}")
    print("")

    S = Si + Vi * t4 + (a*(t4*t4))/2
    V = Vi + a * t4

    print(f"T = {t4}")
    print(f"S = {S}")
    print(f"V = {V}")
    print("")

    S = Si + Vi * t5 + (a*(t5*t5))/2
    V = Vi + a * t5

    print(f"T = {t5}")
    print(f"S = {S}")
    print(f"V = {V}")
    print("")

if fisicacalc == 2:

    Si = float(input("Si: "))
    Vi = float(input("Vi: "))
    a = float(input("a: "))
    t = float(input("t: "))
    print("")

    S = Si + Vi * t + (a*(t*t))/2
    V = Vi + a * t

    print(f"t = {t}")
    print(f"S = {S}")
    print(f"V = {V}")
    print("")

if fisicacalc == 3:

    Vi = float(input("Vi: "))
    V = float(input("V: "))
    t = float(input("t: "))

    a = (V - Vi)/t
    print(f"a = {a}")

if fisicacalc == 4:
    import matplotlib.pyplot as plt

    Si = float(input("Si: "))
    Vi = float(input("Vi: "))
    a = float(input("a: "))
    t1 = float(input("t1: "))
    t2 = float(input("t2: "))
    t3 = float(input("t3: "))
    t4 = float(input("t4: "))
    t5 = float(input("t5: "))
    print("")

    S1 = Si + Vi * t1 + (a * (t1 * t1)) / 2
    V1 = Vi + a * t1

    print(f"t = {t1}")
    print(f"S = {S1}")
    print(f"V = {V1}")
    print("")

    S2 = Si + Vi * t2 + (a * (t2 * t2)) / 2
    V2 = Vi + a * t2

    print(f"t = {t2}")
    print(f"S = {S2}")
    print(f"V = {V2}")
    print("")

    S3 = Si + Vi * t3 + (a * (t3 * t3)) / 2
    V3 = Vi + a * t3

    print(f"t = {t3}")
    print(f"S = {S3}")
    print(f"V = {V3}")
    print("")

    S4 = Si + Vi * t4 + (a * (t4 * t4)) / 2
    V4 = Vi + a * t4

    print(f"t = {t4}")
    print(f"S = {S4}")
    print(f"V = {V4}")
    print("")

    S5 = Si + Vi * t5 + (a * (t5 * t5)) / 2
    V5 = Vi + a * t5

    print(f"t = {t5}")
    print(f"S = {S5}")
    print(f"V = {V5}")
    print("")

    #################
    # conjuntos

    cS = [S1, S2, S3, S4, S5]
    ct = [t1, t2, t3, t4, t5]
    cV = [V1, V2, V3, V4, V5]
    ca = [a, a, a, a, a]

    #################

    names = ['S x t', 'V x t', 'a x t']

    plt.figure(figsize=(12, 4))

    # s x t
    plt.subplot(131)
    plt.plot(ct, cS)
    plt.ylabel("S")
    plt.xlabel("t")
    plt.title("S x t")
    plt.grid(True)

    # v x t
    plt.subplot(132)
    plt.plot(ct, cV)
    plt.ylabel("V")
    plt.xlabel("t")
    plt.title("V x t")
    plt.grid(True)

    # a x t
    plt.subplot(133)
    plt.plot(ct, ca)
    plt.ylabel("a")
    plt.xlabel("t")
    plt.title("a x t")
    plt.grid(True)

    plt.suptitle(f"Gráficos MRUV")
    plt.show()
