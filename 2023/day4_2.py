import time
start_time = time.time()
with open("inputs/day4_1.txt") as file:
    data=file.readlines()
data=[x.strip() for x in data]


cards= {i :1 for i,x in enumerate(data)}


for i, card in enumerate(data):
    for j in range(cards[i]):
        subdata= card.split(":")
        winning_numbers=subdata[1].split("|")[0].strip().split(" ")
        my_numbers= subdata[1].split("|")[1].strip().split(" ")
        winning_numbers=[int(x) for x in winning_numbers if x!=""]
        my_numbers=[int(x) for x in my_numbers if x!=""]
        count=0
        for no in winning_numbers:
            count+=my_numbers.count(no)
        for k in range(count):
            cards[i+k+1]+=1
    print(f"{i}/{len(data)}")


result=sum(cards.values())

print(result)


print("--- %s seconds ---" % (time.time() - start_time))
#--- 74.34500026702881 seconds ---
