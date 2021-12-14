import numpy as np

with open('input14.txt', 'r') as f:
    data=f.readlines()

data=[line.strip() for line in data]
template= data[0]
data=data[2:]

insertions ={ i.split('->')[0].strip():i.split('->')[1].strip() for i in data}

def crate_pairs(template):
    pairs ={ i.split('->')[0].strip():0 for i in data}
    for i, char in enumerate(template):
        if i == 0:
            pass
        else:
            kombo=template[i-1:i+1]
            if kombo in insertions:
                pairs[kombo]+=1
            else:
                print('x')
    last_letter=template[-1]
    return pairs, last_letter

pairs, last_letter= crate_pairs(template)

def step(pairs):
    new_pairs={x:0 for x in pairs}  
    for kombo in pairs:
        new_pairs[kombo[0]+insertions[kombo]]+=pairs[kombo]
        new_pairs[insertions[kombo]+kombo[1]]+=pairs[kombo]
    #print(pairs)
    return new_pairs

for x in range(40):
    pairs=step(pairs)

letter_list=[]
for pair in pairs:
    letter_list.append(pair[0])
    letter_list.append(pair[1])
letter_list=set(letter_list)

counter= {e:0 for e in letter_list}

for pair in pairs:
    counter[pair[0]]+=pairs[pair]
counter[last_letter]+=1
max_letter=max(counter, key=counter.get)
min_letter=min(counter, key=counter.get)

result= counter[max_letter]-counter[min_letter]
print('result',result)