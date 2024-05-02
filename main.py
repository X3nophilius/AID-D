import dungeon as dg
import os

PLAYERNUM = 1
players = []
dungeonscale=(25,25)

dungeon = dg.startdungeon("dungeon.json",PLAYERNUM,players)

dg.intro(dungeon)

while True:
    for player in players:
        os.system('cls' if os.name == 'nt' else 'clear')
        dg.stats(player)
        entry = input().split(" ",1)
        #parse user input
        if "goto" in entry[0] and  any(entry[1] in s for s in dungeon["rooms"][player.location]["connections"]):
            if dungeon["rooms"][player.location]["doors"][entry[1]]["key"] == True and dungeon["rooms"][player.location]["doors"][entry[1]]["keyid"] not in player.inventory:
                print(f"You need a key to enter {entry[1]}")
                dg.drawinv(dungeon,player)
                input()
            else:
                player.location = entry[1].replace(" ","")
                    
        elif 'say' in entry[0]:
            print(f'you said {entry[1]}')
            input()
            
        elif 'inv' in entry[0]:
            dg.drawinv(dungeon,player)
            input()

        elif 'map' in entry[0]:
            dg.drawmap(dungeon,player,dungeonscale)
            print(f"you are in {player.location}")
            print("adjacent locations "+", ".join(dungeon["rooms"][player.location]["connections"]))
            input()