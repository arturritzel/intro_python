## imports
from time import sleep

# fundinhos fofos
WHITE_BACKGROUND = "\033[1;40m" # fundo branco
RED_BACKGROUND = "\033[1;41m" # fundo vermelho
GREEN_BACKGROUND = "\033[1;42m" # fundo verde
YELLOW_BACKGROUND = "\033[1;43m" # fundo amarelo
BLUE_BACKGROUND = "\033[1;44m" # fundo azul
PINK_BACKGROUND = "\033[1;45m" # fundo rosa
CYAN_BACKGROUND = "\033[1;46m" # fundo ciano
GRAY_BACKGROUND = "\033[1;47m" # fundo cinza

# cores fofinhas
WHITE = "\033[1;30m" # branco
RED = "\033[1;31m" # vermelho
GREEN = "\033[1;32m" # verde
YELLOW = "\033[1;33m" # amarelo
BLUE = "\033[1;34m" # azul
PINK = "\033[1;35m" # rosa
CYAN = "\033[1;36m" # ciano
GRAY = "\033[1;90m" # cinza

# utility oba
SQUARED = "\033[1;51m" # enquadrado
CROSSED = "\033[1;09m" # riscadinho tlg?
UNDERLINE = "\033[1;04m" # sublinhado
ITALIC = "\033[1;03m" # itálico
RESET = "\033[0;0m" # reset




#################### presets
## debug
xptotal = 0
ourototal = 0
nivel = 1
knightskill = 0
xp = 0
maxxp = 20
mainadv = 1
vida = 0
vidamax = 0
classe = 0
ataque = 0
defesa = 0
moedas = 0
leuregrasfoda123 = 0
bichosderrotados = 0
navalha = 1
manto = 1
couraca = 1
potfor = 1
potres = 1
potdiv = 1
towncity = 9
missaoconfirm1 = 0
## mobs
#orc1
vidaorc1 = 7
ataqueorc1 = 4
#homemporco1
vidahomemporco1 = 9
ataquehomemporco1 = 5
####################

## quebrar
quebrar = (f"{RED}...por favor, pare de tentar quebrar o jogo! O único easter egg fugindo das regras do jogo é a classe secreta!{RESET}")
## dead end
dead_end = (f"{RED}É o fim de sua jornada. Você pode começar novamente.{RESET}")

##regras inicio
if mainadv == 0:
    print(f"{CYAN}Leia atentamente às regras!");sleep(2)
    print(f"{BLUE}1- não fica vendo o script po... assim tu vai saber o que acontece em cada ocasião e como passar por ela!");sleep(3)
    print(f"2- digite apenas quando pedido! Você pode perceber isso quando houverem ':' indicando.");sleep(4)
    print(f"3- em TODAS ocasiões binárias, 1 = sim e 2 = não.");sleep(2)
    print(f"4- if vc for o pedro vai tomar no seu cu");sleep(2)
    print(f"5- else aproveite{RESET}");sleep(2)
    print("")
    print(f"{BLUE}Você leu e concorda com as regras? {RESET}");sleep(2)

    leuregrasfoda123 = float(input("1- sim, 2- não: "));sleep(1)
##regras fim
if leuregrasfoda123 != 12312312:
    nick = input(f"{BLUE}Digite seu nick: {RESET}");sleep(1)
    print("")
    print(f"{CYAN}Olá {nick}! Seja bem-vindo.");sleep(1)
    print("Esse jogo ainda está em fase de testes.");sleep(1.5)
    print("Ele ainda está sendo programado. Você está tendo acesso à fase alpha.")
    print("");sleep(5)

    print(f"{BLUE}Escolha sua classe!")
    print(f"{RESET}=============================={BLUE}")

    print(f"{BLUE}1 = Mago: alto poder de fogo, mas pouca resistência.{RESET}")
    print(f"{YELLOW}Habilidade Especial: dano causado aumentado em {GREEN}20%{YELLOW}.{RESET}")
    print(f"{WHITE}Atributos: {CYAN}Resistência ++{RESET}, {GREEN}Ataque +++");sleep(3)

    print("")

    print(f"{BLUE}2 = Guerreiro: baixo poder de ataque, mas muita resistência.{RESET}")
    print(f"{YELLOW}Habilidade Especial: na primeira morte, ressucita com {RED}25% {YELLOW}da vida máxima.{RESET}")
    print(f"{WHITE}Atributos: {CYAN}Resistência +++{RESET}, {GREEN}Ataque ++");sleep(3)

    print("")

    print(f"{BLUE}3 = Vanguarda: poder de fogo e resistência razoáveis.{RESET}")
    print(f"{YELLOW}Habilidade Especial: aumenta o poder da defesa em {CYAN}20%{YELLOW}.{RESET}")
    print(f"{WHITE}Atributos: {CYAN}Resistência +++{RESET}, {GREEN}Ataque ++")

    print(f"{RESET}==============================");sleep(3)
    classestart = float(input(f"{BLUE}Sua escolha: {RESET}"));sleep(2)

    if classestart == 1:
        print(f"{GREEN}Classe selecionada: {BLUE}mago{RESET}");sleep(2)
        defesa = 2
        ataque = 2
        classe = "Mago"

    if classestart == 2:
        print(f"{GREEN}Classe selecionada: {BLUE}cavaleiro{RESET}");sleep(2)
        defesa = 3
        ataque = 2
        classe = "Cavaleiro"
        knightskill = 2025

    if classestart == 3:
        print(f"{GREEN}Classe selecionada: {BLUE}vanguarda{RESET}");sleep(2)
        defesa = 2
        ataque = 2
        classe = "Vanguarda"

    if classestart == 4:
        print(f"{BLUE}Sim amigo. Isso é um {GREEN}easter egg.{RESET}");sleep(2)
        print(f"{BLUE}Essa classe possui atributos especiais.{RESET}");sleep(2)
        print(f"{BLUE}Ela é chamada {CYAN}Travecão de Butantã{BLUE}.{RESET}");sleep(2)
        print(f"{GREEN}Habilidade especial: vê um atributo aleatório do inimigo antes da batalha.{RESET}")
        defesa = 2
        ataque = 3
        classe = "Travecão de Butantã"

    if 0 < classestart < 5:
        vidamax = 10
        vida = vidamax
        print("")
        print(f"Você é um {PINK}{classe}{RESET} com {RED}{vida:.2f}/{vidamax:.2f}{RESET} de vida, {GREEN}{ataque}{RESET} de ataque e {CYAN}{defesa}{RESET} de defesa!")
        print("");sleep(2)
        print(f"Sua história começa em {GREEN}Glasland{RESET}. Uma cidade rural onde a economia é baseada em plantação e exportação de vegetais.");sleep(2)
        print("Você vivia uma vida tranquila. Até um grupo de anjos caídos seguidores de Azazel atacarem uma cidade próxima.");sleep(2)
        print("Membros de sua família foram mortos pela crueldade dos atos dos seguidores de Azazel. Você jurou vingança.");sleep(2)
        print("Mas isso foram há muitos anos atrás. Agora você vive como caçador de monstros menores, e é reconhecido por isso.");sleep(2)
        print("É mais uma de suas jornadas, e você encontrou um orc.")
        print("");sleep(2)
        print("Deseja lutar com esse orc?")

    if classestart == 4:
        print(f"{GREEN}Por ser um {PINK}{classe}{GREEN}, você pode ver quanta vida esse orc possui: {RED}{vidaorc1}{GREEN}.{RESET}")
    if 0 < classestart < 5:
        orcbatalha1 = float(input("1- sim, 2- não: "));sleep(1)
        print("")
        if orcbatalha1 == 2:
            towncity = 1
        if orcbatalha1 == 1:
            round = 0 ##################################################################
            while vida > 0 and vidaorc1 > 0:  #######
                round = round + 1
                if classestart == 3:
                    if ataqueorc1 > (1.2 * defesa):
                        vida = vida - (ataqueorc1 - (1.2 * defesa))
                    vidaorc1 = vidaorc1 - ataque
                if classestart == 1:
                    if ataqueorc1 > defesa:
                        vida = vida - (ataqueorc1 - defesa)
                    vidaorc1 = vidaorc1 - (1.2 * ataque)
                else:
                    if ataqueorc1 > defesa:
                        vida = vida - (ataqueorc1 - defesa)
                    vidaorc1 = vidaorc1 - ataque
                sleep(1.5)
                print(f"{CYAN}Round {GREEN}{round}{RESET}")
                print(f"Sua vida: {RED}{vida:.2f}{RESET}")
                print(f"Vida do orc: {RED}{vidaorc1:.2f}{RESET}")

            if vida <= 0:
                if knightskill == 2025:
                    knightskill = 0
                    print("Sua habilidade de cavaleiro foi utilizada.")
                    vida = 0.25 * vidamax
                    while vida > 0 and vidaorc1 > 0:  #########
                        round = round + 1
                        if ataqueorc1 > defesa:
                            vida = vida - (ataqueorc1 - defesa)
                        vidaorc1 = vidaorc1 - ataque

                        print(f"{CYAN}Round {GREEN}{round}{RESET}")
                        print(f"Sua vida: {RED}{vida:.2f}{RESET}")
                        print(f"Vida do orc: {RED}{vidaorc1:.2f}{RESET}")

                    if vida <= 0:
                        print(f"{RED}Você morreu.{RESET}")
                        print(dead_end)
                    else:
                        print(f"{GREEN}Você venceu!{RESET}")  ##############
                        mainadv = 822

                else:
                    print(f"{RED}Você morreu.{RESET}")
                    print(dead_end)
            else:
                print(f"{GREEN}Você venceu!{RESET}")  ##############
                mainadv = 822 ###################################################

            if mainadv == 822:
                sleep(2)
                print("")
                print(f"{YELLOW}O orc foi derrotado.{RESET}")
                bichosderrotados = bichosderrotados + 1
                print(f"{BLUE}Parabéns! Você ganhou {PINK}20 {BLUE}xp e {PINK}5 {BLUE}moedas de ouro!{RESET}") ############################################
                xp = xp + 20
                xptotal = xptotal + 20
                moedas = moedas + 5
                ourototal = ourototal + 5
                #############################################################
                sleep(2)
                if xp >= maxxp:
                    xp = xp - maxxp
                    maxxp = maxxp * 2.5
                    nivel = nivel + 1
                    vida = vidamax
                    print("")
                    print(f"{BLUE}Você subiu de nível! Escolha um atributo para evoluir:{RESET}")
                    print(f"{YELLOW}Nível atual: {PINK}{nivel} {YELLOW}/ xp: {PINK}{xp}/{maxxp}{YELLOW}.{RESET}")
                    print(f"{RED}1 = +2 vida máxima {BLUE}/ {GREEN}2 = +1 ataque {BLUE}/ {CYAN}3 = +1 defesa{BLUE}: ")
                    evolui_lvl = float(input(f"Sua escolha: {RESET}"));sleep(2)
                    if evolui_lvl == 1:
                        vidamax = vidamax + 2
                    if evolui_lvl == 2:
                        ataque = ataque + 1
                    if evolui_lvl == 3:
                        defesa = defesa + 1
                    if evolui_lvl > 3 or evolui_lvl < 1:
                        print("Você tentou quebrar o sistema de escolhas, e como punição, não ganhará novos atributos.")
                    sleep(2)
                    print(f"Agora você é um {PINK}{classe}{RESET} com {RED}{vida:.2f}/{vidamax:.2f}{RESET} de vida, {GREEN}{ataque}{RESET} de ataque e {CYAN}{defesa}{RESET} de defesa!")
                        ################################################################
                print("")

        print(f"Depois de certos eventos, você será redirecionado à cidade.{RESET}");sleep(2)
        print(f"Vamos fazer um tour pela cidade nesse momento.{RESET}")
        print("");sleep(2)
        print(f"Está tudo ficando muito perigoso por aqui.{RESET}");sleep(2)
        print(f"Você decide voltar para a cidade.{RESET}")
        towncity = 1
        print("");sleep(2)
        #################################################################
        print(f"{BLUE}Bem-vindo à cidade, {nick}!")
        while towncity != 0:
            ferreirolegal = 0
            bruxolegal = 0
            print("")
            print(f"{YELLOW}0 {RESET}= {WHITE}Saída{RESET}. Saia da cidade em busca de novas aventuras.")
            print(f"{YELLOW}1 {RESET}= {WHITE}Ferreiro{RESET}. Compre equipamentos do ferreiro.")
            print(f"{YELLOW}2 {RESET}= {WHITE}Bruxo{RESET}. Compre consumíveis do bruxo.")
            print(f"{YELLOW}3 {RESET}= {WHITE}Status{RESET}. Veja suas estatísticas.");sleep(2)
            towncity = float(input(f"{BLUE}Sua escolha: {RESET}"))
            print("")
            if towncity == 0:
                towncity = 0
            if towncity == 1:
                print(f"{YELLOW}Balanço atual: {moedas} moedas.")
                print(f"{PINK}1 {RESET}= {YELLOW}13 moedas{RESET} = Navalha: {PINK}+2 ataque{RESET}.{RESET}")
                print(f"{PINK}2 {RESET}= {YELLOW}11 moedas{RESET} = Manto Encantado: {PINK}+3 vida{RESET}.{RESET}")
                print(f"{PINK}3 {RESET}= {YELLOW}13 moedas{RESET} = Couraça Cristalina: {PINK}+2 defesa{RESET}.{RESET}")
                print(f"{PINK}4 {RESET}= Saída{RESET}.");sleep(2)
                ferreirolegal = float(input(f"{BLUE}Sua escolha: "))
                if ferreirolegal == 1:
                    if moedas >= 13 and navalha == 1:
                        print(f"{BLUE}Você comprou: {PINK}Navalha{RESET}")
                        moedas = moedas - 13
                        navalha = 0
                        ataque = ataque + 2
                        print(f"Agora você possui {GREEN}{ataque}{RESET} de ataque!")
                    else:
                        print(f"{BLUE}Você não tem moedas suficiente ou já comprou esse item!{RESET}")
                if ferreirolegal == 2:
                    if moedas >= 11 and manto == 1:
                        print(f"{BLUE}Você comprou: {PINK}Manto Encantado{BLUE}.{RESET}")
                        moedas = moedas - 11
                        manto = 0
                        vidamax = vidamax + 3
                        print(f"Agora você possui {RED}{vida:.2f}/{vidamax:.2f}{RESET} de vida!")
                    else:
                        print(f"{BLUE}Você não tem moedas suficiente ou já comprou esse item!{RESET}")
                if ferreirolegal == 3:
                    if moedas >= 13 and couraca == 1:
                        print(f"{BLUE}Você comprou: {PINK}Couraça Cristalina{BLUE}.{RESET}")
                        moedas = moedas - 13
                        couraca = 0
                        defesa = defesa + 2
                        print(f"Agora você possui {CYAN}{defesa}{RESET} de defesa!")
                    else:
                        print(f"{BLUE}Você não tem moedas suficiente ou já comprou esse item!{RESET}")


            if towncity == 2:
                print(f"{YELLOW}Balanço atual: {moedas} moedas.")
                print(f"{PINK}1 {BLUE}= {YELLOW}3 moedas{BLUE} = Poção de vida: {PINK}regenera sua vida{BLUE} (sem limite de compra).{RESET}")
                print(f"{PINK}2 {BLUE}= {YELLOW}45 moedas{BLUE} = Poção de força: {PINK}+15 ataque{BLUE}.{RESET}")
                print(f"{PINK}3 {BLUE}= {YELLOW}50 moedas{BLUE} = Poção de resistência: {PINK}+10 defesa{BLUE}.{RESET}")
                print(f"{PINK}4 {BLUE}= {YELLOW}450 moedas{BLUE} = Poção divina: {PINK}dobra sua defesa e ataque{BLUE}.{RESET}")
                print(f"{PINK}5 {BLUE}= Saída{RESET}.");sleep(2)
                bruxolegal = float(input(f"{BLUE}Sua escolha: "))
                if bruxolegal == 1:
                    if moedas >= 3:
                        print(f"{BLUE}Você comprou: {PINK}Poção de vida{BLUE}.{RESET}")
                        moedas = moedas - 3
                        vida = vidamax
                        print(f"Agora você possui {RED}{vida:.2f}/{vidamax:.2f}{RESET} de vida")
                    else:
                        print(f"{BLUE}Você não tem moedas suficiente!{RESET}")
                if bruxolegal == 2:
                    if moedas >= 45 and potfor == 1:
                        potfor = 0
                        moedas = moedas - 45
                        ataque = ataque + 15
                        print(f"Agora você possui {GREEN}{ataque}{RESET} de ataque!")
                    else:
                        print(f"{BLUE}Você não tem moedas suficiente ou já comprou esse item!{RESET}")
                if bruxolegal == 3:
                    if moedas >= 50 and potres == 1:
                        potres = 0
                        moedas = moedas - 50
                        defesa = defesa + 10
                        print(f"Agora você possui {CYAN}{defesa}{RESET} de defesa!")
                    else:
                        print(f"{BLUE}Você não tem moedas suficiente ou já comprou esse item!{RESET}")
                if bruxolegal == 4:
                    if moedas >= 450 and potdiv == 1:
                        potdiv = 0
                        moedas = moedas - 450
                        defesa = defesa + defesa
                        ataque = ataque + ataque
                        print(f"Agora você possui {GREEN}{ataque}{RESET} de ataque e {CYAN}{defesa}{RESET} de defesa!")
                    else:
                        print(f"{BLUE}Você não tem moedas suficiente ou já comprou esse item!{RESET}")

            if towncity == 3:
                print(f"{RESET}Você é {BLUE}{nick}{RESET}, um {PINK}{classe}{RESET} com {RED}{vida:.2f}/{vidamax:.2f}{RESET} de vida, {GREEN}{ataque}{RESET} de ataque e {CYAN}{defesa}{RESET} de defesa!")
                print(f"Nível atual: {PINK}{nivel}{RESET}")
                print(f"Xp atual: {PINK}{xp}/{maxxp}{RESET}.")
                print(f"Balanço atual: {YELLOW}{moedas}{RESET} moedas.")
                print(f"Você já derrotou {PINK}{bichosderrotados}{RESET} inimigos, que te proporcionaram {WHITE}{xptotal}{RESET} xp e {YELLOW}{ourototal}{RESET} moedas!");sleep(2)
            if towncity < 0 or towncity > 3:
                print(quebrar)
        if towncity == 0: #############################################################################
            print("");sleep(2)
            print("Mais um de seus clientes aparece.");sleep(2)
            print(f"- {WHITE}Por favor... minha filha foi raptada por um enorme homem-porco!{RESET}");sleep(2)
            print(f"{GRAY}Recompensas da missão: 20 moedas e 90 xp{RESET}");sleep(2)
            print("Deseja aceitar a missão?");sleep(1)
            print("1- sim / 2- não")
            missao1 = float(input(f"Sua escolha: "))
            if missao1 == 1:
                missaoconfirm1 = 1
            if missao1 == 2:
                missaoconfirm1 = 0
            if missao1 > 2 or missao1 < 1:
                print(quebrar)

            print("")
            if missaoconfirm1 == 0:
                print("Você sai da cidade em busca de novos monstros.");sleep(2)
                mainadv = 1991
            if missaoconfirm1 == 1:
                print("Você sai da cidade em busca do homem-porco.");sleep(2)
                mainadv = 1991

            if mainadv == 1991:
                print("Existem algumas pegadas ao lado da cidade em direção à floresta.");sleep(2)
                print("Talvez elas levem você exatamente aos montros que procura.");sleep(2)
                print("Você decide seguir as pegadas e, começa à ouvir barulhos estranhos.")
                print("");sleep(2)
                print("Ao fundo da floresta, bichomtdoido tem um porcao com um porrete")
                print("Deseja lutar com o monstro?")
                print("1- sim / 2- não")
                if classestart == 4:
                    print(f"{GREEN}Por ser um {PINK}{classe}{GREEN}, você pode ver quanta vida esse monstro possui: {CYAN}{vidahomemporco1}{GREEN}.{RESET}")
                print("")

                homemporco1batalha = float(input("Sua escolha: "))

                if homemporco1batalha < 1 or homemporco1batalha > 2:
                    print(quebrar)

                if homemporco1batalha == 2:
                    mainadv = 88

                if homemporco1batalha == 1:
                    round = 0  ##################################################################
                    while vida > 0 and vidahomemporco1 > 0:  #######
                        round = round + 1
                        if classestart == 3:
                            if vidahomemporco1 > (1.2 * defesa):
                                vida = vida - (ataquehomemporco1 - (1.2 * defesa))
                            vidahomemporco1 = vidahomemporco1 - ataque
                        if classestart == 1:
                            if ataquehomemporco1 > defesa:
                                vida = vida - (ataquehomemporco1 - defesa)
                            vidahomemporco1 = vidahomemporco1 - (1.2 * ataque)
                        else:
                            if ataquehomemporco1 > defesa:
                                vida = vida - (ataquehomemporco1 - defesa)
                            vidahomemporco1 = vidahomemporco1 - ataque
                        sleep(1.5)
                        print(f"{CYAN}Round {GREEN}{round}{RESET}")
                        print(f"Sua vida: {RED}{vida:.2f}{RESET}")
                        print(f"Vida do homem-porco: {RED}{vidahomemporco1:.2f}{RESET}")

                    if vida <= 0:
                        if knightskill == 2025:
                            knightskill = 0
                            print("Sua habilidade de cavaleiro foi utilizada.")
                            vida = 0.25 * vidamax
                            while vida > 0 and vidahomemporco1 > 0:  #########
                                round = round + 1
                                if ataquehomemporco1 > defesa:
                                    vida = vida - (ataquehomemporco1 - defesa)
                                vidahomemporco1 = vidahomemporco1 - ataque

                                print(f"{CYAN}Round {GREEN}{round}{RESET}")
                                print(f"Sua vida: {RED}{vida:.2f}{RESET}")
                                print(f"Vida do homem-porco: {RED}{vidahomemporco1:.2f}{RESET}")

                            if vida <= 0:
                                print(f"{RED}Você morreu.{RESET}")
                                print(dead_end)
                            else:
                                print(f"{GREEN}Você venceu!{RESET}")  ##############
                                mainadv = 993

                        else:
                            print(f"{RED}Você morreu.{RESET}")
                            print(dead_end)
                    else:
                        print(f"{GREEN}Você venceu!{RESET}")  ##############
                        mainadv = 993  ###################################################

                if mainadv == 993:
                    mainadv = 88
                    print("")
                    print(f"{YELLOW}O homem-porco foi derrotado.{RESET}")
                    bichosderrotados = bichosderrotados + 1
                    print(f"{BLUE}Parabéns! Você ganhou {PINK}36 {BLUE}xp e {PINK}8 {BLUE}moedas de ouro!{RESET}")  ############################################
                    xp = xp + 36
                    xptotal = xptotal + 36
                    moedas = moedas + 8
                    ourototal = ourototal + 8
                    #############################################################
                    if xp >= maxxp:
                        xp = xp - maxxp
                        maxxp = maxxp * 2.5
                        nivel = nivel + 1
                        vida = vidamax
                        print("")
                        print(f"{BLUE}Você subiu de nível! Escolha um atributo para evoluir:{RESET}")
                        print(f"{YELLOW}Nível atual: {PINK}{nivel} {YELLOW}/ xp: {PINK}{xp}/{maxxp}{YELLOW}.{RESET}")
                        print(f"{RED}1 = +2 vida máxima {BLUE}/ {GREEN}2 = +1 ataque {BLUE}/ {CYAN}3 = +1 defesa{BLUE}: ")
                        evolui_lvl = float(input(f"Sua escolha: {RESET}"));sleep(2)
                        if evolui_lvl == 1:
                            vidamax = vidamax + 2
                        if evolui_lvl == 2:
                            ataque = ataque + 1
                        if evolui_lvl == 3:
                            defesa = defesa + 1
                        if evolui_lvl > 3 or evolui_lvl < 1:
                            print("Você tentou quebrar o sistema de escolhas, e como punição, não ganhará novos atributos.")
                        sleep(2)
                        print(f"Agora você é um {PINK}{classe}{RESET} com {RED}{vida:.2f}/{vidamax:.2f}{RESET} de vida, {GREEN}{ataque}{RESET} de ataque e {CYAN}{defesa}{RESET} de defesa!")
                        ################################################################
                    if missaoconfirm1 == 1:
                        print("Lá estava. Enjaulada na moradia do homem-porco, a filha de um dos moradores da cidade.")
                        print("")
                        print(f"{WHITE}Missão Completa.{RESET}")
                        print(f"Você recebeu: {PINK}90{RESET} xp e {YELLOW}20{RESET} moedas!")
                        xp = xp + 90
                        xptotal = xptotal + 90
                        moedas = moedas + 20
                        ourototal = ourototal + 20
                        if xp >= maxxp:
                            xp = xp - maxxp
                            maxxp = maxxp * 2.5
                            nivel = nivel + 1
                            vida = vidamax
                            print("")
                            print(f"{BLUE}Você subiu de nível! Escolha um atributo para evoluir:{RESET}")
                            print(f"{YELLOW}Nível atual: {PINK}{nivel} {YELLOW}/ xp: {PINK}{xp}/{maxxp}{YELLOW}.{RESET}")
                            print(f"{RED}1 = +2 vida máxima {BLUE}/ {GREEN}2 = +1 ataque {BLUE}/ {CYAN}3 = +1 defesa{BLUE}: ")
                            evolui_lvl = float(input(f"Sua escolha: {RESET}"));sleep(2)
                            if evolui_lvl == 1:
                                vidamax = vidamax + 2
                            if evolui_lvl == 2:
                                ataque = ataque + 1
                            if evolui_lvl == 3:
                                defesa = defesa + 1
                            if evolui_lvl > 3 or evolui_lvl < 1:
                                print("Você tentou quebrar o sistema de escolhas, e como punição, não ganhará novos atributos.");sleep(2)
                            print(f"Agora você é um {PINK}{classe}{RESET} com {RED}{vida:.2f}/{vidamax:.2f}{RESET} de vida, {GREEN}{ataque}{RESET} de ataque e {CYAN}{defesa}{RESET} de defesa!")

                # cidade
                towncity = 1
                if mainadv == 88:
                    print(f"{BLUE}Bem-vindo à cidade, {nick}!")
                    while towncity != 0:
                        ferreirolegal = 0
                        bruxolegal = 0
                        print("")
                        print(f"{YELLOW}0 {RESET}= {WHITE}Saída{RESET}. Saia da cidade em busca de novas aventuras.")
                        print(f"{YELLOW}1 {RESET}= {WHITE}Ferreiro{RESET}. Compre equipamentos do ferreiro.")
                        print(f"{YELLOW}2 {RESET}= {WHITE}Bruxo{RESET}. Compre consumíveis do bruxo.")
                        print(f"{YELLOW}3 {RESET}= {WHITE}Status{RESET}. Veja suas estatísticas.");sleep(2)
                        towncity = float(input(f"{BLUE}Sua escolha: {RESET}"))
                        print("")
                        if towncity == 0:
                            towncity = 0
                        if towncity == 1:
                            print(f"{YELLOW}Balanço atual: {moedas} moedas.")
                            print(f"{PINK}1 {RESET}= {YELLOW}13 moedas{RESET} = Navalha: {PINK}+2 ataque{RESET}.{RESET}")
                            print(f"{PINK}2 {RESET}= {YELLOW}11 moedas{RESET} = Manto Encantado: {PINK}+3 vida{RESET}.{RESET}")
                            print(f"{PINK}3 {RESET}= {YELLOW}13 moedas{RESET} = Couraça Cristalina: {PINK}+2 defesa{RESET}.{RESET}")
                            print(f"{PINK}4 {RESET}= Saída{RESET}.");sleep(2)
                            ferreirolegal = float(input(f"{BLUE}Sua escolha: "))
                            if ferreirolegal == 1:
                                if moedas >= 13 and navalha == 1:
                                    print(f"{BLUE}Você comprou: {PINK}Navalha{RESET}")
                                    moedas = moedas - 13
                                    navalha = 0
                                    ataque = ataque + 2
                                    print(f"Agora você possui {GREEN}{ataque}{RESET} de ataque!")
                                else:
                                    print(f"{BLUE}Você não tem moedas suficiente ou já comprou esse item!{RESET}")
                            if ferreirolegal == 2:
                                if moedas >= 11 and manto == 1:
                                    print(f"{BLUE}Você comprou: {PINK}Manto Encantado{BLUE}.{RESET}")
                                    moedas = moedas - 11
                                    manto = 0
                                    vidamax = vidamax + 3
                                    print(f"Agora você possui {RED}{vida:.2f}/{vidamax:.2f}{RESET} de vida!")
                                else:
                                    print(f"{BLUE}Você não tem moedas suficiente ou já comprou esse item!{RESET}")
                            if ferreirolegal == 3:
                                if moedas >= 13 and couraca == 1:
                                    print(f"{BLUE}Você comprou: {PINK}Couraça Cristalina{BLUE}.{RESET}")
                                    moedas = moedas - 13
                                    couraca = 0
                                    defesa = defesa + 2
                                    print(f"Agora você possui {CYAN}{defesa}{RESET} de defesa!")
                                else:
                                    print(f"{BLUE}Você não tem moedas suficiente ou já comprou esse item!{RESET}")

                        if towncity == 2:
                            print(f"{YELLOW}Balanço atual: {moedas} moedas.")
                            print(f"{PINK}1 {BLUE}= {YELLOW}3 moedas{BLUE} = Poção de vida: {PINK}regenera sua vida{BLUE} (sem limite de compra).{RESET}")
                            print(f"{PINK}2 {BLUE}= {YELLOW}45 moedas{BLUE} = Poção de força: {PINK}+15 ataque{BLUE}.{RESET}")
                            print(f"{PINK}3 {BLUE}= {YELLOW}50 moedas{BLUE} = Poção de resistência: {PINK}+10 defesa{BLUE}.{RESET}")
                            print(f"{PINK}4 {BLUE}= {YELLOW}450 moedas{BLUE} = Poção divina: {PINK}dobra sua defesa e ataque{BLUE}.{RESET}")
                            print(f"{PINK}5 {BLUE}= Saída{RESET}.");sleep(2)
                            bruxolegal = float(input(f"{BLUE}Sua escolha: "))
                            if bruxolegal == 1:
                                if moedas >= 3:
                                    print(f"{BLUE}Você comprou: {PINK}Poção de vida{BLUE}.{RESET}")
                                    moedas = moedas - 3
                                    vida = vidamax
                                    print(f"Agora você possui {RED}{vida:.2f}/{vidamax:.2f}{RESET} de vida")
                                else:
                                    print(f"{BLUE}Você não tem moedas suficiente!{RESET}")
                            if bruxolegal == 2:
                                if moedas >= 45 and potfor == 1:
                                    potfor = 0
                                    moedas = moedas - 45
                                    ataque = ataque + 15
                                    print(f"Agora você possui {GREEN}{ataque}{RESET} de ataque!")
                                else:
                                    print(f"{BLUE}Você não tem moedas suficiente ou já comprou esse item!{RESET}")
                            if bruxolegal == 3:
                                if moedas >= 50 and potres == 1:
                                    potres = 0
                                    moedas = moedas - 50
                                    defesa = defesa + 10
                                    print(f"Agora você possui {CYAN}{defesa}{RESET} de defesa!")
                                else:
                                    print(f"{BLUE}Você não tem moedas suficiente ou já comprou esse item!{RESET}")
                            if bruxolegal == 4:
                                if moedas >= 450 and potdiv == 1:
                                    potdiv = 0
                                    moedas = moedas - 450
                                    defesa = defesa + defesa
                                    ataque = ataque + ataque
                                    print(f"Agora você possui {GREEN}{ataque}{RESET} de ataque e {CYAN}{defesa}{RESET} de defesa!")
                                else:
                                    print(f"{BLUE}Você não tem moedas suficiente ou já comprou esse item!{RESET}")

                        if towncity == 3:
                            print(f"{RESET}Você é {BLUE}{nick}{RESET}, um {PINK}{classe}{RESET} com {RED}{vida:.2f}/{vidamax:.2f}{RESET} de vida, {GREEN}{ataque}{RESET} de ataque e {CYAN}{defesa}{RESET} de defesa!")
                            print(f"Nível atual: {PINK}{nivel}{RESET}")
                            print(f"Xp atual: {PINK}{xp}/{maxxp}{RESET}.")
                            print(f"Balanço atual: {YELLOW}{moedas}{RESET} moedas.")
                            print(f"Você já derrotou {PINK}{bichosderrotados}{RESET} inimigos, que te proporcionaram {WHITE}{xptotal}{RESET} xp e {YELLOW}{ourototal}{RESET} moedas!");sleep(2)
                        if towncity < 0 or towncity > 3:
                            print(quebrar)

                    if towncity == 0:  #############################################################################
                        print("");sleep(2)
                        print(f"{BLUE}Obrigado por jogar a fase de testes, {nick}!");sleep(2)
                        print("Por favor, reporte qualquer erro que você tenha encontrado!")
                        print("");sleep(2)
                        print(f"{WHITE}Créditos:");sleep(2)
                        print(f"Script e desenvolvimento: Tuizinn");sleep(2)
                        print("História: VnniR");sleep(2)
                        print(f"ser um bosta kkk: pedro gay{RESET}");sleep(2)



        else:
            print(quebrar)


    else:
        print(quebrar)

else:
    print(f"{RED}adeus amigo...{RESET}")
