import json

mapscale=(10,10)

playerroom = "start"


with open("dungeon.json","r") as f:
    map = json.load(f)
    f.close()

for y in range(mapscale[1]):
    for x in range(mapscale[0]):
        for room in map["rooms"]:
            if room['name'] == playerroom: 
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


    