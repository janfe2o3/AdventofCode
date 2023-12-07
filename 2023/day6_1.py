import time
from tqdm import tqdm
import numpy as np

start_time = time.time()
with open("2023/inputs/day6_1.txt") as file:
    data=file.readlines()
data=[x.strip() for x in data]

times= data[0].split(":")[1].strip().split(" ")
times= [int(x) for x in times if x!=""]

distances= data[1].split(":")[1].strip().split(" ")
distances= [int(x) for x in distances if x!=""]

# x*(a-x)-b=0      a=time    b=distance
#x**2 - ax +b

#quadratic formula
solution=1
for i in range(len(times)):
    a=times[i]
    b= distances[i]+0.001 # should beat so a little bit higer
    roots=np.roots([1, -a, b])
    solution*=(np.floor(roots[0])-np.floor(roots[1]))

print(int(solution))
      

print("--- %s seconds ---" % (time.time() - start_time))

    


