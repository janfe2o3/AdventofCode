from get_input import get_input

#data= get_input(1).splitlines()
with open("inputs/day1_1.txt") as file:
    data=file.readlines()
data=[x.strip() for x in data]



list1=[]

letters= ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
reversed_letters = [x[::-1] for x in letters]
for line in data:
    first=None
    second=None    
    for i,letter in enumerate(line):
        if letter.isnumeric():
            first=letter
            break
        for j,k in enumerate(letters):
            if line[i:len(k)+i]==k:
                first= str(j+1)
                break
        if first !=None:
            break
    reversed_line=line[::-1]
    for i, letter in enumerate(reversed_line):
        if letter.isnumeric():
            second=letter   
            break
        for j,k in enumerate(reversed_letters):
            if reversed_line[i:len(k)+i]==k:
                second= str(j+1)
                break
        if second !=None:
            break
    list1.append(int(first+second))

result=sum(list1)

print(result)