import numpy as np

with open('input3.txt', 'r') as f:
    text=f.readlines()
text=[[int(k) for k in x.strip()] for x in text]
array= np.array(text)


gamma=''
epsilon=''
for column in array.T:
    if column.mean() > 0.5:
        gamma+='1'
        epsilon+='0'
    else:
        gamma+='0'
        epsilon+='1'

gamma= int(gamma,2)
epsilon= int(epsilon,2)

consumtion= gamma*epsilon

print(consumtion)



