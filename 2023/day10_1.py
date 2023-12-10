import time
#from tqdm import tqdm
import numpy as np
from collections import namedtuple

Point = namedtuple('Point', 'x y')


start_time = time.time()
with open("2023/inputs/day10_1.txt") as file:
    data=file.readlines()
data=[x.strip() for x in data]

print(data)

for y, line in enumerate(data):
    for x, letter in enumerate(line):
        if letter=="S":
            s_pos=Point(x,y)

print("starting pos ",s_pos)

pipe_map= {"|": ((0,-1), (0,1)),
           "-": ((-1,0), (1,0)),
           "L": ((0,-1), (1,0)),
           "J": ((1,0), (0,-1)),
           "7": ((-1,0), (0,1)),
           "F": ((1,0), (0,1)),
          }
# find connected
left_dict={}
right_dict={}
for x,y  in[ [-1, 0] ,[1, 0], [0,-1], [0,1]]:
        if data[s_pos.x + x][s_pos.y+y] in pipe_map:
            con_pos=Point(s_pos.x + x,s_pos.y+y)
            offset= (con_pos.x-s_pos.x, con_pos.y-s_pos.y)
            print(con_pos, s_pos, offset)
            for o in pipe_map[data[s_pos.x + x][s_pos.y+y]]:
                if offset== o:
                    for out in pipe_map[data[s_pos.x + x][s_pos.y+y]]:
                        if  out != offset:
                            outgoing= out
                            break
                    if not left_dict:
                        left_dict[1]={"previous": s_pos,
                                     "current": con_pos,
                                     "incomming": o,
                                     "outgoing": out
                                     }
                    else:
                        right_dict[1]={"previous": s_pos,
                                    "current": con_pos,
                                    "incomming": o,
                                    "outgoing": out
                                    }



def find_next(d, counter, data):
    d[counter+1]={}
    d[counter+1]["previous"] = d[counter]["current"]
    d[counter+1]["current"]=Point(d[counter]["current"].x + d[counter]["outgoing"][0],
                                  d[counter]["current"].y + d[counter]["outgoing"][1])
    d[counter+1]["incomming"] = (-d[counter]["outgoing"][0],-d[counter]["outgoing"][1])
    symbol=data[d[counter+1]["current"].y][d[counter+1]["current"].x]
    for x in pipe_map[symbol]:
        print(symbol, d[counter+1]["incomming"],x)
        if d[counter+1]["incomming"] != x:
                d[counter+1]["outgoing"]=x
                return d
    print("Not found", symbol)



counter=1
while True:
    left_dict=find_next(left_dict, counter, data)
    right_dict=find_next(right_dict, counter, data)
    print(left_dict[counter]["current"],right_dict[counter]["current"])
    counter+=1
    if right_dict[counter]["current"]==left_dict[counter]["current"]:
        break
    #if counter==9:
    #    break

print(counter)
#print(left_dict)

print("--- %s seconds ---" % (time.time() - start_time))