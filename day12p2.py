with open('input12.txt', 'r') as f:
    data=f.readlines()

data=[line.strip().split('-') for line in data]

container=[]
for line in data:
    container+=line

container=list(set(container))

nodes={key:[] for key in container }
status={key:False for key in container if key.islower() }
for line in data:
    element1=line[0]
    element2=line[1]
    nodes[element1]+=[element2]
    nodes[element2]+=[element1]



nodes['end']=[]
del status['end']
del status['start']
an=False
print(status)
#print(status)

counter=0
def dfs(visited, nodes, node,ways,status, an):
    global counter
    if node=='end':
        counter+=1
        ways.append(node)
        print(str(ways)+',')

    if node not in visited:
        ways.append(node)
        #print(small_cave_visited)
        if node=='start' or node =='end':
            visited.add(node)
        elif node.islower() and an ==True:
            visited.add(node)
            status[node]=True
        elif node.islower() and status[node]==False:
            status[node]=True
        elif node.islower() and status[node]==True:
            for key in status:
                if status[key]==True:
                    visited.add(key)
            an=True
            #print('x')
        

        for neighbour in nodes[node]:
            #print(small_cave_visited)
            dfs(visited.copy(), nodes, neighbour, ways.copy(), status.copy(), an)


            
visited = set()  # Set to keep track of visited nodes.
# Driver Code
ways=[]
small_cave_visited=False
dfs(visited, nodes, 'start', ways, status, an)

print(counter)