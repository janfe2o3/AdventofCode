with open('input6.txt', 'r') as f:
    data=f.read()

fish_list= data.split(',')

fish_list=[int(x) for x in fish_list]


for days in range(256): 
    for i in range(len(fish_list)):
        if fish_list[i]>0:
            fish_list[i]-=1
        elif fish_list[i]==0:
            fish_list[i]=6
            fish_list.append(8)


#print(fish_list)
print('fish',len(fish_list))
