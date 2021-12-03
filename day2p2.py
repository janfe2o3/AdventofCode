with open('input2.txt', 'r') as f:
    text=f.readlines()


cor_x=0
cor_y=0
aim=0

for x in text:
    direction= x.split(' ')[0]
    value= int(x.split(' ')[1])
    if direction=='down':
        aim+=value
    elif direction=='up':
        aim-=value
    else:
        cor_x+=value
        cor_y+=aim*value

print(cor_y)
print(cor_x)

print(cor_x*cor_y)
