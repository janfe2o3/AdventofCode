
with open('input1.txt', 'r') as f:
    text=f.readlines()

text=[int(x) for x in text]

counter_inc=0
for x in range(len(text)-3):
    window_a= text[x]+text[x+1]+text[x+2]
    window_b= text[x+1]+text[x+2]+text[x+3]
    if window_b>window_a:
        counter_inc+=1

print(counter_inc)