import numpy as np

with open('input3.txt', 'r') as f:
    text=f.readlines()
text=[[int(k) for k in x.strip()] for x in text]
array= np.array(text)

o_rating=''
c_rating=''
array2= array.copy()


for i in range(array.shape[1]):
    if array.T[i].mean()>= 0.5:
        criteria=1
    else:
        criteria=0
    array = array[array.T[i] == criteria]
    if array.shape[0]==1:
        break



for i in range(array2.shape[1]):
    if array2.T[i].mean()>= 0.5:
        criteria=0
    else:
        criteria=1
    array2 = (array2[array2.T[i] == criteria])
    if array2.shape[0]==1:
        break


for char in array.T:
    o_rating+=str(int(char))


for char in array2.T:
    c_rating+=str(int(char))

o_rating= int(o_rating,2)
c_rating= int(c_rating,2)

rating= o_rating*c_rating

print(o_rating)
print(c_rating)
print(rating)
