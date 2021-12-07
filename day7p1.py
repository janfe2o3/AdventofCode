import numpy as np

with open('input7.txt', 'r') as f:
    data=f.read()

positions=np.array([int(x) for x in data.split(',')])

max=positions.max()
min=positions.min()

fuel_total=[]
for i in range(min,max+1):
    fuel_move=[]
    for j in positions:
        fuel=abs(j-i)
        fuel_move.append(fuel)
    fuel_total.append(sum(fuel_move))

print(fuel_total)

print('min:', np.array([fuel_total]).min())
