with open("inputs/day3_1.txt") as file:
    data=file.readlines()
data=[x.strip() for x in data]


print(data)
numbers=[]
symbol=False
digit_active=False
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
        else:
            if symbol:
                numbers.append(int(number))
            digit_active=False
            symbol=False

result= sum(numbers)

print(result)

#print(numbers)

