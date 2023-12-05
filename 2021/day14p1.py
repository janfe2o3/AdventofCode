import numpy as np

with open('input14.txt', 'r') as f:
    data=f.readlines()

data=[line.strip() for line in data]
template= data[0]
data=data[2:]


insertions ={ i.split('->')[0].strip():i.split('->')[1].strip() for i in data}
 
def step(template):
    new_template=''
    for i, char in enumerate(template):
        if i == 0:
            new_template+=char
        else:
            kombo=template[i-1:i+1]
            if kombo in insertions:
                new_template+=insertions[kombo]+char
            else:
                print('x')
                new_template+=char
    print(len(new_template))
    return new_template



for x in range(40):
    template=step(template)



counter= {e:template.count(e) for e in set(template)}

max_letter=max(counter, key=counter.get)
min_letter=min(counter, key=counter.get)


result= counter[max_letter]-counter[min_letter]
print('result',result)
