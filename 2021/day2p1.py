with open('input2.txt', 'r') as f:
    text=f.readlines()


cor_x=0
cor_y=0

for x in text:
    direction= x.split(' ')[0]
    value= int(x.split(' ')[1])
    if direction=='down':
        cor_y+=value
    elif direction=='up':
        cor_y-=value
    else:
        cor_x+=value

print(cor_y)
print(cor_x)

print(cor_x*cor_y)
