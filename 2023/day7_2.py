import time
#from tqdm import tqdm

start_time = time.time()
with open("2023/inputs/day7_1.txt") as file:
    data=file.readlines()
data=[x.strip() for x in data]
data = [(x.split(" ")[0], int(x.split(" ")[1])) for x in data]

def five_of_a_kind(e):
    dict1 = {r:e.count(r) for r in set(e)}
    if 5 in dict1.values():
        return True
    elif 4 in dict1.values() and "J" in e:
        return True
    elif 3 in dict1.values() and e.count("J")==2 :
        return True
    elif 2 in dict1.values() and e.count("J")==3 :
        return True
    else:
        return False

def four_of_a_kind(e):
    dict1 = {r:e.count(r) for r in set(e)}
    dict2= dict1.copy()
    if "J" in dict2:
        del dict2["J"]
    if 4 in dict1.values():
        return True
    elif 3 in dict1.values()and "J" in e:
        return True
    elif 2 in dict2.values() and e.count("J")==2:
        return True
    
    else:
        return False
    
def full_house(e):
    dict1 = {r:e.count(r) for r in set(e)}
    dict2=dict1.copy()
    if "J" in dict2:
        del dict2["J"]
    sorted_values= sorted(dict1.values())
    if 3 in dict1.values() and 2 in dict1.values():
        return True
    elif [2,2]==sorted_values[-2:] and "J" in e:
        return True
    elif 3 in dict1.values() and "J" in e:
        return True
    elif 2 in dict2.values() and e.count("J")==2:
        return True   
    else:
        return False
    
def three_of_a_kind(e):
    dict1 = {r:e.count(r) for r in set(e)}
    if 3 in dict1.values():
        return True
    elif 2 in dict1.values() and "J" in e:
        return True
    elif e.count("J")==2:
        return True
    else:
        return False
    
def two_pair(e):
    dict1 = {r:e.count(r) for r in set(e)}
    sorted_values= sorted(dict1.values())
    dict2=dict1.copy()
    if "J" in dict2:
        del dict2["J"]
    if [2,2]==sorted_values[-2:]:
        return True
    elif 2 in dict2.values() and "J" in e:
        return True
    elif e.count("J")==2:
        return True
    elif e.count("J")==3:
        return True
    else:
        return False

def pair(e):
    dict1 = {r:e.count(r) for r in set(e)}
    if 2 in dict1.values():
        return True
    elif "J" in e:
        return True
    else:
        return False

def create_array(e):
    return [five_of_a_kind(e), four_of_a_kind(e), full_house(e),three_of_a_kind(e), two_pair(e), pair(e), True ]

mapping={
"A":14, "K":13, "Q":12, "T":10, "9":9, "8":8, "7":7, "6":6, "5":5, "4":4, "3":3, "2":2,"J":1,
}
def check_high_card(e1, e2):
    for c1,c2 in zip(e1, e2):
        a1=mapping[c1]
        a2=mapping[c2]
        if a1>a2:
            return False
        elif a1<a2:
            return True
        else:
            continue
        
def check(e1, e2):  #e1<e2
    a1= create_array(e1)
    a2= create_array(e2)
    for i in range(len(a1)):
        if a1[i]==True and a2[i]==False:
            return False
        elif a1[i]==False and a2[i]==True:
            return True
        elif a1[i]==True and a2[i]==True:
            return check_high_card(e1, e2)  
    return check_high_card(e1, e2)

#print(check("JJJ45","J2345"))
#exit()
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        less = [x for x in arr[1:] if check(x[0], pivot[0])]
        greater = [x for x in arr[1:] if check(x[0], pivot[0])==False]
        return quicksort(less) + [pivot] + quicksort(greater)
    
sorted_data = quicksort(data)
#print(sorted_data)
 


result=0
for i in range(1,len(sorted_data)+1):
    result+=i*sorted_data[i-1][1]
print(result)

print("--- %s seconds ---" % (time.time() - start_time))
