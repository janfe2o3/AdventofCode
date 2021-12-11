import numpy as np

with open('input9.txt', 'r') as f:
    data=f.readlines()


tmp_data = []
for line in data:
    tmp_data.append([int(x) for x in line.strip()])

map= np.array(tmp_data)

max_y, max_x = map.shape

matches=[]
for i in range(max_x):
    for j in range(max_y):
        location=map[j][i]
        if i-1<0:                          #left
            left=10
        else:
            left=map[j][i-1]
        if i+1>=max_x:                      #right
            right=10                                 
        else:
            right=map[j][i+1]
        if j-1<0:                          #up
            up=10
        else:
            up=map[j-1][i]
        if j+1>=max_y:                      #down
            down=10                                 
        else:
            down=map[j+1][i]
        #print('coordinates',i,j)
        #print(location)
        #print(left, right, up, down)
        if location < left and location < right and location < up and location < down:
            matches.append(location)


print(matches)
result=sum(matches)+len(matches)
print(result)