import time
from tqdm import tqdm
import numpy as np
from collections import namedtuple

Point = namedtuple('Point', 'x y')


start_time = time.time()
with open("2023/inputs/day10_1.txt") as file:
    data=file.readlines()
data=[x.strip() for x in data]

#print(data)

for y, line in enumerate(data):
    for x, letter in enumerate(line):
        if letter=="S":
            s_pos=Point(x,y)

#print("starting pos ",s_pos)

pipe_map= {"|": ((0,-1), (0,1)),
           "-": ((-1,0), (1,0)),
           "L": ((0,-1), (1,0)),
           "J": ((-1,0), (0,-1)),
           "7": ((-1,0), (0,1)),
           "F": ((1,0), (0,1)),
          }
# find connected
left_dict={}
right_dict={}
for x,y  in [[-1, 0] ,[1, 0], [0,-1], [0,1]]:
        if s_pos.y + y >=0 and s_pos.x+x>=0:
            if data[s_pos.y + y][s_pos.x+x] in pipe_map:
                con_pos=Point(s_pos.x + x,s_pos.y+y)
                offset= (s_pos.x-con_pos.x,s_pos.y- con_pos.y)
                for o in pipe_map[data[s_pos.y + y][s_pos.x+x]]:
                    if offset == o:
                        for out in pipe_map[data[s_pos.y + y][s_pos.x+x]]:
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
        if d[counter+1]["incomming"] != x:
                d[counter+1]["outgoing"]=x
                return d
    print("Not found", symbol)



counter=1
while True:
    left_dict=find_next(left_dict, counter, data)
    right_dict=find_next(right_dict, counter, data)
    #print(left_dict[counter]["current"],right_dict[counter]["current"])
    counter+=1
    if right_dict[counter]["current"]==left_dict[counter]["current"]:
        break
    #if counter==9:
    #    break



points=[(s_pos.x, s_pos.y)]
for i, x in enumerate(left_dict):
    p1=  (left_dict[i+1]["current"].x, left_dict[i+1]["current"].y) 
    p2=  (right_dict[i+1]["current"].x, right_dict[i+1]["current"].y) 
    points.append(p1)
    points.insert(0,p2)
points=points[1:]
#points=list(set(points))

#print(points)
def is_point_inside_pipes(x, y, points):
    n = len(points)
    inside = False
    p1x, p1y = points[0]
    for i in range(n + 1):
        p2x, p2y = points[i % n]
        if y > min(p1y, p2y) and y <= max(p1y, p2y) and x <= max(p1x, p2x):
            if p1y != p2y:
                xinters = (y - p1y) * (p2x - p1x) / (p2y - p1y) + p1x
                if p1x == p2x or x <= xinters:
                    inside = not inside
        p1x, p1y = p2x, p2y

    return inside

point=0
for y, line in tqdm(enumerate(data)):
    for x, char in enumerate(line):
        if is_point_inside_pipes(x,y, points):
            if (x,y) not in points:
                #print(x,y)
                point+=1

print(point)


print("--- %s seconds ---" % (time.time() - start_time))