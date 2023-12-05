import time
from tqdm import tqdm
start_time = time.time()
with open("inputs/day5_1.txt") as file:
    data=file.readlines()
data=[x.strip() for x in data]
#parsing
seeds= data[0].split(":")[1].strip().split(" ")
seeds=[int(x) for x in seeds]

mapping={}
for i,line in tqdm(enumerate(data)):
    if i<2:
        continue
    elif "map" in line:
        name=line.split(" ")[0]
        mapping[name]={}
    elif line=="":
        continue
    else:
        mapping_list=[int(x) for x in line.split(" ")]
        mapping[name][i]={
            "source":mapping_list[1],
            "destination":mapping_list[0],
            "interval":mapping_list[2],
        }
        #for k in range(mapping_list[2]):
            #mapping[name][mapping_list[1]+k]=mapping_list[0]+k

print("parsing finished")


locations=[]
for seed in seeds:
    x=seed
    for i, map in enumerate(mapping.values()):
        for entry in map.values():
            if x >= entry["source"] and x< entry["source"] + entry["interval"]:
                x+= entry["destination"]-entry["source"]
                break
    locations.append(x)

#print(locations)
print("result ",min(locations))


print("--- %s seconds ---" % (time.time() - start_time))
#--- 74.34500026702881 seconds ---