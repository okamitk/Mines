from random import randint as random

#GAME DIALOGS========================================================
def errorDialog():
    print(["You are confused, and decided to dig where nor mines nor treasure exists. Truly interesting.",
          "You chose a place outside the range of the treasure. Thinking positively, at least it seems safe.",
          "You drank a little to much to calm down your nerves and ended digging in who knows where.",
          "Excited, you chose to dig somewhere else. After more than 20 minutes, you realized that you wasn't where you were supposed to be.",
          "After a careful analysis you realized that you were digging outside the treasure area."][random(0,4)])
    
def digDialog():
    print(["You dug, dug, and dug more, and found nothing.",
    "After digging for some time you found nothing.",
    "There's nothing here.",
    "Digging for several minutes, the only thing you found is dirt and rocks, a lot of them.",
    "You dug, but there's nothing valuable in there."][random(0,4)])

def treasureDialog():
    print(["After finding a chest you're so relieved that you fall on knees, and feel like you could die in peace now, well not exactly now.\n\n You found the treasure",
    "You found a chest containing several pieces of jewelry and a few coins from a long gone currency. You can live well now\n\n You found the treasure.",
    "You found a chest containing lots of gold coins. The currency itself isn't usable but you can melt it. You can live peacefully now\n\n You found the treasure.",
    "You found a wooden box containing several gold bars. Now there's no need for risking your life anymore and you carefully go home.\n\n You found the treasure.",
    "You hit a piece of metal and your entire life passes before your eyes. After almost collapsing from fear you realize it's a metal crate with enough for living the rest of your life peacefully.\n\n You found the treasure."][random(0,4)])

def deathDialog(chances):
    print(["While searching for the treasure, the last thing you hear is a click. \n\n You died.",
    "While searching for the treasure you hit a mine with shovel, it should be deactivated because you were standing on it all the time... But then you heard a click. \n\n You died.",
    "You found a metal thing. YES! THE TREASURE!...... ......you thought, but turns out it wasn't really a treasure at all. Well, it would sell for a bit if it wasn't about to explode. \n\n You died,",
    "You stepped on a mine. Only if you wasn't so obsessed with being rich...\n\n You died.",
    "While searching for the treasure you hit a mine with your shovel. 5 seconds pass by like hours, but nothing happens.\n\n You have been given a new chance."][chances])         

def nearDangerDialog(chances):
    print(["You can smell gunpowder near.",
           "You feel a horrible chill on your spine. There's something near.",
           "You can hear the your shovel's hit reverberating through some mine near.",
           "You can see the dirt around you has already been excavated, there's a mine near.",
           "You feel the ground shake, a mine has exploded near."][chances])

def nearTreasureDialog():
    print(["Before leaving you found a gold coin under your foot, maybe the treasure is near.",
           "After inspecting more carefully, you found a golden clock's part, maybe the treasure is near.",
           "After a more careful analyse, you found some golden powder, the treasure must be near.",
           "There's was a small pearl under shining in the dirt, the treasure is near.",
           "After looking more carefully, there's a silver ring in the dirt. The treasure must be near."][random(0,4)])

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


