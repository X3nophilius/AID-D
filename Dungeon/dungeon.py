import json, os, time, random

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
        self.searched = {}

def loadplayer(dungeon):
    name = input("Playername: ")
    age = input("Age: ")
    inventory = []
    location=dungeon["start"]
    tempplayer = player(age,name,location,inventory)
    return tempplayer

def drawanimation(file):
    with open(file) as f:
        animation = json.load(f)
    f.close()
    for i in range(animation["num"]):
        os.system('cls' if os.name == 'nt' else 'clear')
        for i in animation["frames"][str(i)]:
            print(i)
        time.sleep(animation["delay"])

def loaddungeon(file):
    with open(file,"r") as f:
        dungeon = json.load(f)
        f.close()
        return dungeon

def drawinv(dungeon,player):
    for item in player.inventory:
        print(dungeon["items"][item]["name"]+" : "+dungeon["items"][item]["description"])

def drawmap(dungeon,player,dungeonscale):
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


def startdungeon(file, playernum, players):
    dungeon = loaddungeon(file)
    drawanimation("Dungeon/animations/startanimation.json")
    drawanimation("Dungeon/animations/dungeontitle.json")
    for i in range(playernum):
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"============ Player:{i+1} ============")
        players.append(loadplayer(dungeon))
    return dungeon


def intro(dungeon):
    os.system('cls' if os.name == 'nt' else 'clear')
    print(dungeon["intro"])

def stats(player):
    print(f"======== {player.name} ========")
    print(f"location: {player.location}")
    print(f"items: {len(player.inventory)}")
    print(f"=================={len(player.name)*'='}")

def drawroom(name):
    os.system('cls' if os.name == 'nt' else 'clear')
    with open(f"Dungeon/rooms/{name}.json") as f:
        room = json.load(f)
    f.close()
    for i in room["layout"]:
        print(i)

def searchcontainer(player, entry, dungeon):
    with open(f"Dungeon/rooms/{player.location}.json") as f:
        room = json.load(f)
    f.close()
    if player.location not in player.searched:
        player.searched[player.location] = []
    if entry in room["containers"]: 
        if entry not in player.searched[player.location]:
            for i in room["containers"][entry]["items"]:
                if random.random() < room["containers"][entry]["items"][i]:
                    player.inventory.append(i)
                    print(f"you found {(dungeon['items'][i]['name'])}")
            player.searched[player.location].append(entry)
        else:
            print(f"you allready searched {entry}")
    else:
        print(f"{entry} does not exist")