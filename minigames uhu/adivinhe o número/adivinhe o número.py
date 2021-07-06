WHITE = "\033[1;30m" # branco
RED = "\033[1;31m" # vermelho
GREEN = "\033[1;32m" # verde
YELLOW = "\033[1;33m" # amarelo
CYAN = "\033[1;36m" # ciano
PINK = "\033[1;35m" # rosa

from random import randint
n = int(randint(0,1000))
t = 1

print(f"{WHITE}Número gerado!")
print("")

p = int(input(f"{WHITE}Insira um número: "))

while p != n:
    if p < n:
        print(f"{RED}O número é maior do que seu palpite!")
    if p > n:
        print(f"{CYAN}O número é menor do que seu palpite!")
    print("")
    p = int(input(f"{WHITE}Insira um número: "))
    t += 1

if p == n:
    print(f"{GREEN}Correto!")
    print(f"{YELLOW}Você acertou o número em {PINK}{t}{YELLOW} tentativas!")
