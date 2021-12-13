import numpy as np

with open('input13.txt', 'r') as f:
    data=f.readlines()

data=[line.strip() for line in data]


coordinates=[]
instructions=[]

for line in data:
    if "fold" in line:
        info=line.split()[2].split('=')
        instructions.append([info[0], int(info[1])])
    elif line=='':
        pass
    else:
        info=line.split(',')
        coordinates.append([int(info[0]), int(info[1])])


#print(coordinates)
print(instructions)
max_x=0
max_y=0

for point in coordinates:
    if point[0]>max_x:
        max_x=point[0]
    if point[1]>max_y:
        max_y=point[1]
    


paper= np.zeros((max_y+1, max_x+1))
print(paper.shape)
for point in coordinates:
    paper[point[1],point[0]]=1

for instruction in instructions:
    if instruction[0]=='y':
        print('y')
        paper_fold=np.flip(paper, 0)
        paper=paper_fold+paper
        paper[paper>1]=1
        paper=paper[0:instruction[1],:]
    elif instruction[0]=='x':
        print('x')
        paper_fold=np.flip(paper, 1)
        paper=paper_fold+paper
        paper[paper>1]=1
        paper=paper[:,0:instruction[1]]
    print('\n',paper)
    break

result= paper.sum()


print(paper)
print(result)