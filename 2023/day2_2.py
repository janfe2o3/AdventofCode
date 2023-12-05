with open("inputs/day2_1.txt") as file:
    data=file.readlines()
data=[x.strip() for x in data]

power_list=[]

max_values={
    "red": 12,
    "green": 13,
    "blue": 14
}

for line in data:
    game_id=int(line.split(":")[0].split(" ")[1])
    #print(game_id)
    games=line.split(":")[1]
    game_dict={}
    for game in games.split(";"):
        for cube in game.split(","):
            cube=cube.strip()
            color= cube.split(" ")[1]
            value= int(cube.split(" ")[0])
            if color in game_dict.keys():
                if value>game_dict[color]:
                    game_dict[color]=value
            else:
                game_dict[color]=value
    power=1
    for value in game_dict.values():
        power= value*power
    power_list.append(power)


result=sum(power_list)

print(result)

