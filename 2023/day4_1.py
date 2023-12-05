with open("inputs/day4_1.txt") as file:
    data=file.readlines()
data=[x.strip() for x in data]

result=[]
for card in data:
    subdata= card.split(":")
    winning_numbers=subdata[1].split("|")[0].strip().split(" ")
    my_numbers= subdata[1].split("|")[1].strip().split(" ")
    winning_numbers=[int(x) for x in winning_numbers if x!=""]
    my_numbers=[int(x) for x in my_numbers if x!=""]
    points=0
    for no in winning_numbers:
        count=my_numbers.count(no)
        points+=count
    if points>0:
        res=2**(points-1)
        points=0
        result.append(res)


print("part1 ", sum(result))
    #print(winning_numbers, my_numbers)
