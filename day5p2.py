import numpy as np
from collections import Counter

with open('input5.txt', 'r') as f:
    data=f.readlines()
max_x=0
max_y=0
cor_list=[]
for line in data:
    str1=line.split()
    p1=(int(str1[0].split(',')[0]), int(str1[0].split(',')[1]) )
    p2=(int(str1[2].split(',')[0]), int(str1[2].split(',')[1]) )
    temp_list=[]
    if p1[0]==p2[0]:                                                                        #horizontal
        if p1[1]>=p2[1]:
            temp_list= [(p1[0],i) for i in  range(p2[1], p1[1]+1)]
        elif p1[1]<p2[1]:
            temp_list= [(p1[0],i) for i in  range(p1[1], p2[1]+1)]
    elif p1[1]==p2[1]:                                                                      #vertikal
        if p1[0]>=p2[0]:
            temp_list= [(i, p1[1]) for i in  range(p2[0], p1[0]+1)]
        elif p1[0]<p2[0]:
            temp_list= [(i, p1[1]) for i in  range(p1[0], p2[0]+1)]
    elif abs(p1[0]-p2[0]) == abs(p1[1]-p2[1]):                                              #Diagonal
        print('x',p1,p2)
        if p1[0]<p2[0]:                                                                     #aufsteigend
            x1=p1[0]
            x2=p2[0]
            y1=p1[1]
            y2=p2[1]
        else:
            x1=p2[0]
            x2=p1[0]
            y1=p2[1]
            y2=p1[1]
        
        if y1<y2:
            temp_list= [(i, j) for i, j in zip(range(x1, x2+1), range(y1, y2+1))]           #aufsteigend
        else:                                                                                #absteigend
            temp_list= [(i, j) for i, j in zip(range(x1, x2+1), range(y1, y2-1,-1))]

        print(temp_list)

    if p1[0]>max_x: max_x=p1[0]
    if p1[1]>max_y: max_y=p1[1]
    if p2[0]>max_x: max_x=p2[0]
    if p2[1]>max_y: max_y=p2[1]     
    cor_list+=temp_list

dict1=Counter(cor_list)

field= np.zeros((max_y+1,max_x+1))

for cor in dict1:
    field[cor[1]][cor[0]]=dict1[cor]

#print(dict1)
field2= np.zeros((max_y+1,max_x+1)) 

field2[field >= 2] = 1

print(field)
print(field2.sum())


'''    elif abs(p1[0]-p1[1]) - abs(p2[0]-p2[1])<0.1:
        print(p1,p2)
        if p1[0]>=p2[0]:
            temp_list= [(i, j) for i, j in zip(range(p2[0], p1[0]+1), range(p2[1], p1[1]+1))]
        elif p1[0]<p2[0]:
            temp_list= [(i, j) for i,j in  zip(range(p1[0], p2[0]+1), range(p1[1], p2[1]+1))]
        print(temp_list)
    elif abs(p2[0]-p1[1]) - abs(p1[1]-p2[1]) <0.1:
        if p1[0]<p2[0]:
            temp_list= [(i, j) for i, j in zip(range(p1[0], p2[0]+1), range(p1[1], p2[1]-1,-1))]
        elif p1[0]>=p2[0]:
            temp_list= [(i, j) for i, j in zip(range(p1[0], p2[0]-1,-1), range(p1[1], p2[1]+1))]
    else:
        pass'''
    