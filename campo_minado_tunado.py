from random import randint as random

#GAME DIALOGS========================================================
def errorDialog():
    print(["Você, confuso, decidiu cavar onde não existem minas nem tesouros. Verdadeiramente interessante.",
            "Você escolheu um lugar fora do alcance do tesouro. Pensando bem, pelo menos parece seguro.",
            "Você bebeu um pouco demais para acalmar os nervos e acabou cavando sabe-se lá onde.",
            "Animado, você escolheu cavar em outro lugar. Depois de mais de 20 minutos, você percebeu que não estava onde deveria estar.",
            "Depois de uma análise cuidadosa, você percebeu que estava cavando fora da área do tesouro."][random(0,4)])
    
def digDialog():
    print(["Você cavou, cavou e cavou mas não encontrou nada.",
     "Depois de cavar por algum tempo você não encontrou nada.",
     "Não há nada aqui.",
     "Cavando por vários minutos, a única coisa que você encontrou foi terra e pedras, muitas pedras.",
     "Você cavou, mas não há nada valioso."][random(0,4)])

def treasureDialog():
    print(["Depois de encontrar um baú, você ficou tão aliviado que cai de joelhos e sente que poderia morrer em paz agora, bem, não exatamente agora.\n\n Você encontrou o tesouro",
     "Você encontrou um baú contendo várias joias e algumas moedas antigas. Você pode viver bem agora\n\n Você encontrou o tesouro.",
     "Você encontrou um baú contendo muitas moedas de ouro. A moeda em si não é utilizável, mas o ouro sim. Você pode viver em paz agora\n\n Você encontrou o tesouro.",
     "Você encontrou uma caixa de madeira coom várias barras de ouro. Você agora, não precisando mais arriscar sua própria vida, vai para casa com cuidado.\n\n Você encontrou o tesouro.",
     "Você acerta um pedaço de metal com sua pá e toda a sua vida passa diante de seus olhos. Depois de quase desmaiar de medo, você percebe que a tal caixa tem na verdade milhões em pérolas. Você agora vive o resto de sua vida em paz.\n\n Você encontrou o tesouro."][random(0,4)])

def deathDialog(chances):
    print(["Enquanto procura pelo tesouro, a última coisa que você ouve é um clique. \n\n Você morreu.",
     "Enquanto procurava pelo tesouro, você atingiu uma mina com uma pá, ela deveria estar desativada já que você estava pisando nela o tempo todo... Mas então você ouviu um clique. \n\n Você morreu.",
     "Você encontrou uma coisa de metal. SIM! O TESOURO!...... ...... você pensou, mas acontece que não era realmente um tesouro. Bem, venderia por um pouco de prata se não estivesse prestes a explodir. \n\n Você morreu, ",
     "Você pisou em uma mina. No final a busca pelo tesouro não valeu muita coisa...\n\n Você morreu.",
     "Enquanto procurava pelo tesouro, você atingiu uma mina com sua pá. 5 segundos se passaram como se fossem horas, mas nada aconteceu.\n\n Você recebeu uma nova chance."][chances])         

def nearDangerDialog(chances):
    print(["Você pode sentir o cheiro de pólvora vindo das paredes da escavação. Há uma mina por perto.",
            "Você sente um calafrio horrível. Tem algo próximo.",
            "Você consegue ouvir o impacto da sua pá ecoando em alguma mina próxima.",
            "Há polvora misturada na areia que você acabou de cavar. Tem um bomba por perto",
            "Você bateu forte demais com a pá e sentiu o chão tremer, uma mina explodiu por perto."][chances])

def nearTreasureDialog():
    print(["Antes de sair você encontrou uma moeda de ouro sob seu pé, talvez o tesouro esteja próximo.",
            "Depois de inspecionar com mais cuidado, você encontrou a peça de um relógio de ouro, talvez o tesouro esteja próximo.",
            "Um pó dourado misturado na areia brilha enquanto você sai do buraco, o tesouro deve estar próximo.",
            "Havia uma pequena pérola brilhando na terra que você acabou de cavar, o tesouro está próximo.",
            "Depois de olhar com mais cuidado você vê há um anel de prata na terra. O tesouro deve estar próximo."][random(0,4)])

#GAME CODE=============================================================
def generateMap():
    MAP_HEIGHT=9
    MAP_WIDTH=19

    Map = [[1 if (random(0,5))==0 else 0 for _ in range(MAP_WIDTH)] for _ in range(MAP_HEIGHT)]
    Map[random(0,MAP_HEIGHT-1)][random(0,MAP_WIDTH-1)]=4

    print(len(Map))
    print(len(Map[0]))
    return Map

def checkNearSquares(Map,x,y):
    nearDanger=False
    nearTreasure=False
    for i in [[y-1,x-1],[y,x-1],[y+1,x-1],
              [y-1,x  ],        [y+1,x  ],
              [y-1,x+1],[y,x+1],[y+1,x+1]]:
        try:
            if Map[i[1]][i[0]]==1:
                nearDanger=True
                mine=i
            if Map[i[1]][i[0]]==4:
                nearTreasure=True
        except:
            pass
        
    if nearDanger:
        chances=random(0,4)
        Map[x][y]=6
        if chances==4:
            Map[mine[1]][mine[0]]=2
        nearDangerDialog(chances)
    else:
        Map[x][y]=2
    if nearTreasure:
        Map[x][y]=6
        nearTreasureDialog()
    return Map

def Dig(Map,x,y):
    rich=False
    alive = Map[x][y]!=1
    if alive:
        if Map[x][y]==4:
            treasureDialog()
            Map[x][y]=5
            rich=True
        else:
            digDialog()
            Map[x][y]=2
            Map=checkNearSquares(Map,x,y)


    else:
        chances = random(0,4)
        alive = chances==4
        deathDialog(chances)
        Map[x][y]=3
    return[alive,Map,rich]

def chooseSquare(Map):
    coordinates = [int(i) for i in input("x y: ").split(" ")]
    x = coordinates[0]
    y = coordinates[1]
    print("\n\n\n\n\n\n")
    return(Dig(Map,x-1,y-1))

def printMap(m):
    counter=0
    for row in m:
        counter+=1
        print(counter, end=" ")
        for col in row:
            if col==0 or col==1 or col==4:
                print("█",end="")
            elif col==2:
                print(" ",end="")
            elif col==3:
                print("X",end="")
            elif col==5:
               print("O",end="")
            elif col==6:
                print("!",end="")
            else:
                print(col, end="")
        #    print(col,end="")
        print()

def Main(Map):
    rich=False
    alive=True
    print("There's a treasure and several mines on this field, select a square with 'X Y' to start searching.")
    printMap(Map)

    while alive and not rich:
        choosen=False
        while not choosen:
            try:
                turn = chooseSquare(Map)
                choosen=True
            except:
                errorDialog()
        alive = turn[0]
        Map=turn[1]
        rich = turn[2]
        printMap(Map)

Main(generateMap())


