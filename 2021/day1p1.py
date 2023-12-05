
with open('input1.txt', 'r') as f:
    text=f.readlines()

text=[int(x) for x in text]

counter_inc=0
for x in range(len(text)-1):
    if text[x+1]>text[x]:
        counter_inc+=1

print(counter_inc)