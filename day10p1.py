from tqdm import tqdm

with open('input10.txt', 'r') as f:
    data=f.readlines()

char_dict={
    '>':'<',
    ')':'(',
    '}':'{',
    ']':'['}
Bußgeldkatalog={
    '>':25137,
    ')':3,
    '}':1197,
    ']':57}
error_dict = {y:x for x,y in char_dict.items()}

def check(line):
    global error
    for i,char in enumerate(line):
        if char in char_dict:
            #print(char)
            if line[i-1]==char_dict[char]:
                mod_line=line[0: i-1:] + line[i + 1::]
                #print(mod_line)
                check(mod_line)   
            elif line[i-1] in char_dict.values():
                #print('Expected '+error_dict[line[i-1]]+ ', but found '+char+' instead.')
                error=char
                break
            break
    #return mod_line
error_list=[]
for line in tqdm(data):
    error=''
    check(line)
    #print(error)
    error_list.append(error)

error_list=[x for x in error_list if x!='']
print(error_list)
Bußgeld=0
for error in error_list:
    Bußgeld+=Bußgeldkatalog[error]

print(Bußgeld)

