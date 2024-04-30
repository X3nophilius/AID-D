import json, os

PLAYERNUM = 1
players = []

dungeonscale=(10,10)

colors = {
    "BLACK":'\033[30m',
    "RED":'\033[31m',
    "GREEN":'\033[32m',
    "YELLOW":'\033[33m',
    "BLUE":'\033[34m',
    "MAGENTA":'\033[35m',
    "CYAN":'\033[36m',
    "WHITE":'\033[37m',
    "UNDERLINE":'\033[4m',
    "RESET":'\033[0m'
}

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
        print(dungeon["items"][item]["name"]+" : "+dungeon["items"][item]["description"])

def drawmap(player):
    os.system('cls' if os.name == 'nt' else 'clear')
    for y in range(dungeonscale[1]):
        for x in range(dungeonscale[0]):
            for room in dungeon["rooms"]:
                if room == player.location: 
                    color="\033[31m"
                elif room != player.location:
                    color=colors[dungeon["rooms"][room]["color"]]
                    
                room = dungeon["rooms"][room]
                if [x,y] in room["pos"]:
                    char = f"{color}██"
                    break
                else: 
                    char = f"\033[30m██"
            print(char,end="")    
        print("\n\033[0m",end="")

while True:
    for player in players:
        #drawdungeon 
        drawmap(player)

        print(f"you are in {player.location}")
        print("adjacent locations "+", ".join(dungeon["rooms"][player.location]["connections"]))
        entry = input().split(" ",1)
        #parse user input
        if "goto" in entry[0] and  any(entry[1] in s for s in dungeon["rooms"][player.location]["connections"]):
            if dungeon["rooms"][player.location]["doors"][entry[1]]["key"] == True and dungeon["rooms"][player.location]["doors"][entry[1]]["keyid"] not in player.inventory:
                print(f"You need a key to enter {entry[1]}")
                drawinv(player)
                input()
            else:
                player.location = entry[1].replace(" ","")
                    
        elif 'say' in entry[0]:
            print(f'you said {entry[1]}')
            input()
            
        elif 'inv' in entry[0]:
            drawinv(player)
            input()