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
        location=j,i
        value=map[j][i]
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

        if value < left and value < right and value < up and value < down:
            matches.append(location)


#print(matches)


def check(position):
        mask[position[0]][position[1]]=1
        j,i= position
        value=map[j][i]
        if i-1<0:                          #left
            left=9
        else:
            left=map[j][i-1]
            left_position=(j,i-1)
        if i+1>=max_x:                      #right
            right=9                                 
        else:
            right=map[j][i+1]
            right_position=(j,i+1)
        if j-1<0:                          #up
            up=9
        else:
            up=map[j-1][i]
            up_position=(j-1,i)
        if j+1>=max_y:                      #down
            down=9                                
        else:
            down=map[j+1][i]
            down_position=(j+1,i)

        if down<9 and value<down:
            mask[down_position[0]][down_position[1]]=1
            check(down_position)
        if up<9 and value<up:
            mask[up_position[0]][up_position[1]]=1
            check(up_position)
        if right<9 and value<right:
            mask[right_position[0]][right_position[1]]=1
            check(right_position)
        if left<9 and value<left:
                mask[left_position[0]][left_position[1]]=1
                check(left_position)

        


result_list=[]

for match in matches:
    mask=np.zeros(map.shape)
    check(match)
    result=mask.sum()
    #print(mask)
    #print(result)
    result_list.append(result)


result_list.sort(reverse=True)
result=np.prod(result_list[0:3])
print(result)

