import numpy as np

with open('input4.txt', 'r') as f:
    text=f.readlines()

numbers= text[0].split(',')
numbers=[int(x.strip()) for x in numbers]

text= text[2:]


grid_list=[]
for i in range(0,len(text),6):
    grid=text[i:i+5]
    grid_list.append(grid)

bingo_sets=[]
for grid in grid_list:
    grid1=[]
    for entry in grid:
        list1=entry.split()
        line= [int(x) for x in list1]
        grid1.append(line)
    bingo_sets.append(grid1)

list2= [np.array(bingo) for bingo in bingo_sets]

bingo_list= [(array, np.zeros((5,5))) for array in list2]

break1=False    

for number in numbers:
    if break1==True: break
    for array, status in bingo_list:
        status[array==number]=1
        if 5 in status.sum(axis=0) or 5 in status.sum(axis=1):
            array[status==1]=0
            sum= np.sum(array)
            print(sum*number)
            break1=True
            break

