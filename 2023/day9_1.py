import time
#from tqdm import tqdm
import numpy as np

start_time = time.time()
with open("2023/inputs/day9_1.txt") as file:
    data=file.readlines()
data=[x.strip() for x in data]

data= [[int(i) for i in x.split(" ")] for x in data]

res_list=[]
for line in data:
    t=np.array(line)
    t_list=[t]
    while True:
        z= np.diff(t)
        if np.all(z==0):
            res_list.append(t_list)
            break
        t_list.append(z)
        t=z

right_list=[]
left_list=[]
for i in res_list:
    f1=0
    f2=0
    for x in reversed(i):
        n1= f1+x[-1]
        f1=n1
        n2= x[0]-f2
        f2=n2
    right_list.append(f1)
    left_list.append(f2)

print("part1",sum(right_list))
print("part2",sum(left_list))

print("--- %s seconds ---" % (time.time() - start_time))