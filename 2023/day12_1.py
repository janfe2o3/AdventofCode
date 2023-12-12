
import time
from tqdm import tqdm
import numpy as np
import scipy
import itertools


start_time = time.time()
with open("2023/inputs/day12_1.txt") as file:
    data=file.readlines()
data=[x.strip() for x in data]
rows=[x.split(" ")[0] for x in data]
records=[[int(i) for i in x.split(" ")[1].split(",")] for x in data] 



def next(instruction, string, full_instruction, check_gear, guess):
    #print(instruction, string, full_instruction)
    if len(instruction)==0 and len(string)==0:
        posibility.append(full_instruction)
        guesses.append(guess)
        #print("return", full_instruction)
        return
    if len(instruction)==0:
        if "#" in string:
            return
        else:
           # print("retun because instr=0 and no #")
            guess+= len(string)*"."
            posibility.append(full_instruction)
            guesses.append(guess)
            
            return
    if len(string)==0 and len(instruction)>0:
        return
    #check direct
    if string>=string[:instruction[0]] and check_gear:
        check= string[:instruction[0]]
       # print("check", check)
        if "." in check:
            pass
            #print("check not passed")
        else:
            if string[instruction[0]:instruction[0]+1]=="#":
                pass
            else:
                #print("next instruction")
                #print("input",instruction[1:], string[instruction[0]:], full_instruction )
                guess=guess+len(check)*"#"
                #print(guess)
                #print(instruction[1:],string[instruction[0]:], len(instruction[1:]),len(string[instruction[0]:]))
                #print(instruction,string, len(instruction[1:]),len(string[instruction[0]:]))
                next(instruction[1:], string[instruction[0]:], full_instruction, check_gear=False,guess= guess)

        #chek empty
    if len(string)>0:
        if "#" in string[0]:
            #print("unable to move")
            pass
        else:
           # print("moving")
            if len(string[1:])==0:
                return
            next(instruction, string[1:], full_instruction, check_gear=True, guess=guess+".")


guesses=[]
posibility=[]
for i, row in enumerate(rows):

    #per= list(set(list(itertools.permutations(records[i]))))
    #per= [list(x) for x in per]
    #print(per)
    #guesses=[]
    #print("start_______________________________________________________")
    next(records[i], row, records[i], check_gear=True, guess="")
    #print("new__________________________________________________________________________________")
    #guesses= [x for x in guesses if len(x)==len(row)]
print(posibility)
print(len(posibility))

#for i in guesses:
#    print(i)

print(len(guesses))
#print(rows[0], records[0])


print("--- %s seconds ---" % (time.time() - start_time))