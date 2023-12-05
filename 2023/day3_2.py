with open("inputs/day3_1.txt") as file:
    data=file.readlines()
data=[x.strip() for x in data]


print(data)
numbers=[]
symbol=False
digit_active=False
gears={}
gear="no_gear"
for i, line in enumerate(data):
    for k, pos in enumerate(line):
        if pos.isnumeric():
            if not digit_active:
                number=pos
                digit_active=True
            else:
                number+=pos
            #print(number, symbol)
            # check surrounding
            for d in [-1, 0, 1]:
                for f in [-1, 0, 1]:
                    if i+d>=0 and k+f>=0 and i+d<len(data) and k+f<len(line) :
                        #print(i+d, k+f)
                        neighbour= data[i+d][k+f]
                        if neighbour is not "." and not neighbour.isnumeric():
                            symbol=True
                            if neighbour=="*":
                                gear=f"{i+d}_{k+f}"
        else:
            if symbol:
                numbers.append(int(number))
                if gear in gears.keys():
                    gears[gear].append(int(number))
                else:
                    gears[gear]=[int(number)]
                gear="no_gear"
            digit_active=False
            symbol=False

result1= sum(numbers)

print("part1: ",result1)

result2=[]
del gears["no_gear"]
for pair in gears.values():
    if len(pair)==2:
        result2.append(pair[0]*pair[1])
print("part2", sum(result2))
#print(numbers)

