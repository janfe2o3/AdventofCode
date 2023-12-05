import numpy as np

with open('input11.txt', 'r') as f:
    data=f.readlines()

container=[]
for h in data:
    line=[int(x) for x in h.strip()]
    container.append(line)

result_list=[]

array= np.array(container)


def flash():
    global list1
    global result_list
    global flashed
    list1=np.where(array>=10)
    list1= np.dstack(list1)[0]
    list1=list1.tolist()
    list1=[x for x in list1 if x not in flashed]
    if len(list1)==0:
        flashes = np.zeros(array.shape)
        flashes[array>9]=1
        result_list.append(flashes.sum())
    else:
        location=list1[0]
        flashed.append([location[0], location[1]])
        #print(location)
        if location[0]==0:
            up=0
        else:
            up= location[0]-1
        down= location[0]+1
        right=location[1]+1
        if location[1]==0:
            left=0
        else:
            left=location[1]-1
        array[up:down+1,left:right+1]+=1
        flash()
        
def step():
    global array
    global result_list
    global flashed
    array +=1
    flashed=[]
    flash()



for i in range(1000000):
    step()
    array[array>10]=0
    print(sum(result_list))
    if result_list[i]==100:
        print(len(result_list))
        break
