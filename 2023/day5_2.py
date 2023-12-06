import time
from tqdm import tqdm
import numpy as np
start_time = time.time()
with open("2023/inputs/day5_1.txt") as file:
    data=file.readlines()
data=[x.strip() for x in data]
#parsing
seeds= data[0].split(":")[1].strip().split(" ")
seeds_setup=[int(x) for x in seeds]

seeds=[]
for i, entry in tqdm(enumerate(seeds_setup)):
    if i%2!=0:
        seeds.append([seeds_setup[i-1], seeds_setup[i]])

print(seeds)


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

print("parsing finished")

def split_interval(seed_start, seed_end, point1, point2,destination):

    before = [seed_start, min(seed_end,point1)]
    between = [max(seed_start, point1), min(point2, seed_end)]
    after = [max(point2, seed_start), seed_end]

    if before[0]>before[1]:
        before=[None, None]
    else:
        before= [before[0], before[1]-before[0]]
    if between[0]>between[1]:
        between=[None, None]
    else:
        #between=[between[0]-point1 +destination, 
        #         between[1]-point1+destination]
        between= [between[0], between[1]-between[0]]
    if after[0]>after[1]:
        after=[None, None]
    else:
        after= [after[0], after[1]-after[0]]
    return before, between, after

def pass_through(input_map, map):
    seeds=input_map
    passed=[]
    for entry in map.values(): 
        not_passed=[]
        #print(seeds)
        for x in seeds:
            seed_start=x[0]
            seed_end= x[0]+x[1]
            before, between, after = split_interval(seed_start, seed_end,
                                                    entry["source"], entry["source"]+ entry["interval"], entry["destination"])
            
            if between[0] != None:
                between[0]+= entry["destination"]-entry["source"]
                #between[1] -=-entry["source"]+entry["destination"]
                passed.append(between)
            
            if before[0]!=None:
                not_passed.append(before)
            if after[0]!=None:
                not_passed.append(after)
            #exit()
        seeds = not_passed
    return passed + not_passed
        


input_map=seeds
for i, map in enumerate(mapping.values()):
    input_map=pass_through(input_map, map)
    print(f"{i},  {input_map}")
    #exit()

min1=100000000000
for i in input_map:
    if i[0]<min1:
        min1=i[0]
print("result ",min1)


print("--- %s seconds ---" % (time.time() - start_time))