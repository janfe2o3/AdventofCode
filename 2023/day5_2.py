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
        seeds.append([seeds_setup[i-1], seeds_setup[i-1]+seeds_setup[i]])

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
    if before[0]>=before[1]:
        before=[None, None]
    if between[0]>=between[1]:
        between=[None, None]
    if after[0]>=after[1]:
        after=[None, None]
    else:
        pass
    return before, between, after

def pass_through(input_map, map):
    seeds=input_map
    passed=[]
    for entry in map.values(): 
        not_passed=[]
        for x in seeds:
            before, between, after = split_interval(x[0], x[1],
                                                    entry["source"], entry["source"]+ entry["interval"], entry["destination"])
            if between[0] != None:
                between=[between[0]-entry["source"]+entry["destination"], between[1]-entry["source"]+entry["destination"]]
                passed.append(between)
            if before[0]!=None:
                not_passed.append(before)
            if after[0]!=None:
                not_passed.append(after)
        seeds = not_passed
    return passed + not_passed
        


input_map=seeds
for i, map in enumerate(mapping.values()):
    input_map=pass_through(input_map, map)

starts= [i[0] for i in input_map]

print("result ",min(starts))


print("--- %s seconds ---" % (time.time() - start_time))