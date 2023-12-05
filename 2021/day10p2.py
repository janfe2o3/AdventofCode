from tqdm import tqdm
from statistics import median

with open('input10.txt', 'r') as f:
    data=f.readlines()

char_dict={
    '>':'<',
    ')':'(',
    '}':'{',
    ']':'['}
Punktekatalog={
    '>':4,
    ')':1,
    '}':3,
    ']':2}
error_dict = {y:x for x,y in char_dict.items()}

def check(line):
    global endline
    global error
    for i,char in enumerate(line):
        if char in char_dict:
            #print(char)
            if line[i-1]==char_dict[char]:
                mod_line=line[0: i-1:] + line[i + 1::]
                endline=mod_line
                check(mod_line)   
            elif line[i-1] in char_dict.values():
                #print('Expected '+error_dict[line[i-1]]+ ', but found '+char+' instead.')
                error=True
                break
            break
    #return mod_line
scores=[]
for line in tqdm(data):
    endline=''
    score=0
    error=False
    check(line)
    if error ==False:
        endline=endline.strip()[::-1]
        list1=[error_dict[x] for x in endline]
        for i,char in enumerate(list1):
            score*=5
            score+=Punktekatalog[char]
        scores.append(score)





#print(scores)
result= median(scores)


print(result)

