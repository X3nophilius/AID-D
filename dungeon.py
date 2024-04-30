import json, os

PLAYERNUM = 1
players = []

class entity():
    def init():
        print("entity initialized")

class player:
    def __init__(self,age,name,location,inventory):
        print("entity initialized")
        self.age = age
        self.name = name
        self.location = location
        self.inventory = inventory

def loadplayer():
    name = input("Playername: ")
    age = input("Age: ")
    inventory = ["0001"]
    location=dungeon["start"]
    tempplayer = player(age,name,location,inventory)
    return tempplayer

with open("dungeon.json","r") as f:
    dungeon = json.load(f)
    f.close()

for i in range(PLAYERNUM):
    players.append(loadplayer())

def drawinv(player):
    for item in player.inventory:
        print(dungeon["items"][item]["name"]+" "+dungeon["items"][item]["description"])

def drawmap(player):
    os.system('cls' if os.name == 'nt' else 'clear')
    for y in range(dungeonscale[1]):
        for x in range(dungeonscale[0]):
            for room in dungeon["rooms"]:
                if room == player.location: 
                    color="\033[96m"
                else: 
                    color="\033[0m"
                    
                room = dungeon["rooms"][room]
                if [x,y] in room["pos"]:
                    char = f"{color}██"
                    break
                else: 
                    char = f"\033[30m██"
            print(char,end="")    
        print("\n\033[0m",end="")


dungeonscale=(10,10)

while True:
    for player in players:
        #drawdungeon 
        drawmap(player)

        print(f"you are in {player.location}")
        print("adjacent locations "+", ".join(dungeon["rooms"][player.location]["connections"]))
        entry = input().split(" ",1)
        print(entry)
        input()
        #parse user input
        if "goto" in entry[0] and entry[1] in dungeon["rooms"][player.location]["connections"]:
            if dungeon["rooms"][player.location]["doors"][entry[1]]["key"] == True:
                if dungeon["rooms"][player.location]["doors"][entry[1]]["keyid"] not in player.inventory:
                    print(f"You need a key to enter {splitString}")
                    drawinv(player)
                    input()
                    break
            else:
                player.location = entry[1]
                    
        elif 'say' in entry:
            res = entry.split("say ", 1)
            splitString = res[1]
            print(f'you said {entry[1]}')
            input()
            
        elif 'inv' in entry[0]:
            drawinv(player)
            input()