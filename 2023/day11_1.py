import time
from tqdm import tqdm
import numpy as np
import scipy

start_time = time.time()
with open("2023/inputs/day11_1.txt") as file:
    data=file.readlines()
data=[[u for u in x.strip()] for x in data]


data= np.array(data)
data_new=data
count=0
for x, line in enumerate(data_new):
    if not np.isin(line, "#").any():
        data= np.insert(data, [x+count], line, axis=0)
        count+=1
data=data.T
data_new=data
count=0
for x, line in enumerate(data_new):
    if not np.isin(line, "#").any():
        data= np.insert(data, [x+count], line, axis=0)
        count+=1
data=data.T

points = np.where(np.isin(data, "#"))
coords=list(zip(points[0], points[1]))

distances=scipy.spatial.distance.cdist(coords, coords, metric='cityblock', )

distances *= np.tri(*distances.shape)
distances= distances.flatten()


distances= distances[distances != 0]
print(coords)
print(int(sum(distances)))


print("--- %s seconds ---" % (time.time() - start_time))