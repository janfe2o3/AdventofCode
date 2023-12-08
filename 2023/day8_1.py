import time
#from tqdm import tqdm

start_time = time.time()
with open("2023/inputs/day8_1.txt") as file:
    data=file.readlines()
data=[x.strip() for x in data]
directions=[x for x in data[0]]

nav= {}

for line in data[2:]:
    key= line.split("=")[0].strip()
    value= (line.split("=")[1].strip().split(",")[0][1:].strip(),line.split("=")[1].strip().split(",")[1][:-1].strip())
    nav[key]=value


i=0
res=1
key="AAA"
while True:
    if directions[i]=="L":
        value= nav[key][0]
    else:
        value= nav[key][1]
    if value== "ZZZ":
        break
    else:
        key=value
        i+=1
        res+=1
        if i>=len(directions):
            i=0

print(res)






print("--- %s seconds ---" % (time.time() - start_time))