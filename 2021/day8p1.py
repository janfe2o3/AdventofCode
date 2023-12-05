with open('input8.txt', 'r') as f:
    data=f.readlines()

output_list=[]
for line in data:
    output= line.split('|')[1]
    output= output.split()
    output_list+=output

dict1={key: 0 for key in range(2,8)}

for number in output_list:
    length=len(number)
    dict1[length]+=1

print(dict1)

result= dict1[2]+dict1[4]+dict1[3]+dict1[7]

print(result)