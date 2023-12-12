
import time
from tqdm import tqdm
import numpy as np
import scipy

start_time = time.time()
with open("2023/inputs/day11_1.txt") as file:
    data=file.readlines()
data=[[u for u in x.strip()] for x in data]

factor=1000000
data= np.array(data)
data[data == '#'] = 1
data[data == '.'] = 0
data= np.array(data, dtype=bool)

data_new=data
count=0
y_values={}
for y, line in tqdm(enumerate(data_new)):
    if not np.isin(line, True).any():
        count+=factor-1
    y_values[y]=count
data=data.T
data_new=data
count=0
x_values={}
for x, line in tqdm(enumerate(data_new)):
    if not np.isin(line, True).any():
        #data= np.insert(data, [x+count], np.pad([line], ((0,factor-2),(0,0)),constant_values=False), axis=0)
        count+=factor-1
    x_values[x]=count
data=data.T

points = np.where(np.isin(data, True))
coords=list(zip(points[0], points[1]))

new_cords=[]
for y_old, x_old in coords:
    (x, y)= x_old+x_values[x_old], y_old+y_values[y_old]
    new_cords.append((y, x))

distances=scipy.spatial.distance.cdist(new_cords, new_cords, metric='cityblock')

distances *= np.tri(*distances.shape)
distances= distances.flatten()


distances= distances[distances != 0]

print(int(sum(distances)))


print("--- %s seconds ---" % (time.time() - start_time))