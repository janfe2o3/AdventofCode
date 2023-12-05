with open('input12.txt', 'r') as f:
    data=f.readlines()

data=[line.strip().split('-') for line in data]

container=[]
for line in data:
    container+=line

container=list(set(container))

nodes={key:[] for key in container}
for line in data:
    element1=line[0]
    element2=line[1]
    nodes[element1]+=[element2]
    nodes[element2]+=[element1]



nodes['end']=[]



counter=0
def dfs(visited, nodes, node,ways):
    global counter
    if node=='end':
        counter+=1
        ways.append(node)
        #print(ways)
    if node not in visited:
        ways.append(node)
        if node.islower():
            visited.add(node)
        for neighbour in nodes[node]:
            dfs(visited.copy(), nodes, neighbour, ways)


            
visited = set()  # Set to keep track of visited nodes.
# Driver Code
ways=[]
dfs(visited, nodes, 'start', ways)

print(counter)