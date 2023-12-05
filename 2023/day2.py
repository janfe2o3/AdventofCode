with open("inputs/day2_1.txt") as file:
    data=file.readlines()
data=[x.strip() for x in data]

possible_games=[]

max_values={
    "red": 12,
    "green": 13,
    "blue": 14
}

for line in data:
    possible=True
    game_id=int(line.split(":")[0].split(" ")[1])
    #print(game_id)
    games=line.split(":")[1]
    for game in games.split(";"):
        game_dict={}
        for cube in game.split(","):
            cube=cube.strip()
            color= cube.split(" ")[1]
            value= int(cube.split(" ")[0])
            game_dict[color]=value
        for key in game_dict.keys():
            if game_dict[key]>max_values[key]:
                possible=False
    if possible:
        possible_games.append(game_id)


print(possible_games)
result=sum(possible_games)

print(result)

