import json, os

PLAYERNUM = 1
players = []

class entity():
    def init():
        print("entity initialized")

class player:
    def __init__(self,age,name,location):
        print("entity initialized")
        self.age = age
        self.name = name
        self.location = location

def loadplayer():
    name = input("Playername: ")
    age = input("Age: ")
    location=map["start"]
    tempplayer = player(age,name,location)
    return tempplayer

def possiblemoves(player):
    for i in map["rooms"]:
        if i["name"]== player.location:
            print(i["connections"])


with open("dungeon.json","r") as f:
    map = json.load(f)
    f.close()

for i in range(PLAYERNUM):
    players.append(loadplayer())

mapscale=(10,10)

while True:
    for i in players:
        os.system('cls' if os.name == 'nt' else 'clear')
        for y in range(mapscale[1]):
            for x in range(mapscale[0]):
                for room in map["rooms"]:
                    if room['name'] == i.location: 
                        color="\033[96m"
                    else: 
                        color="\033[0m"
                    if [x,y] in room["pos"]:
                        char = f"{color}██"
                        break
                    else: 
                        char = f"\033[30m██"
                print(char,end="")    
            print("\n",end="")

        print(f"you are in {i.location}")
        possiblemoves(i)
        entry = input()
        if 'goto' in entry:
            res = entry.split("goto", 1)
            splitString = res[1]
            for j in map["rooms"]:
                print(j["name"])
                if j["name"] in splitString:
                    i.location = j["name"]
        elif 'say' in entry:
            res = entry.split("say", 1)
            splitString = res[1]
            print(f'you said {splitString}')
            input("wait")
            
        
        