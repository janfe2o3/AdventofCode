import time
from tqdm import tqdm
import numpy as np

start_time = time.time()
with open("2023/inputs/day6_1.txt") as file:
    data=file.readlines()
data=[x.strip() for x in data]

times= data[0].split(":")[1].strip().split(" ")
times= [x for x in times if x!=""]

distances= data[1].split(":")[1].strip().split(" ")
distances= [x for x in distances if x!=""]

time_total= ""
distance_total=""
for i, _ in enumerate(times):
    time_total+=times[i]
    distance_total+=distances[i]

a=int(time_total)
b=int(distance_total) + 0.0001

roots=np.roots([1, -a, b])
solution=(np.floor(roots[0])-np.floor(roots[1]))

print(int(solution))
      

print("--- %s seconds ---" % (time.time() - start_time))

    


