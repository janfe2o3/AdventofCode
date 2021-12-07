f = open('input6.txt')
F = [int(x) for x in f.readlines()[0].split(',')]
agegroup = [0]*9 ## 0-8 days old




for f in F: agegroup[f] += 1

for d in range(8):
    agegroup[(d+7)%9] += agegroup[d%9]
print(sum(agegroup))

'''from collections import Counter

with open('data/06.txt') as fh:
    data = fh.read().strip()

timers = [int(x) for x in data.split(',')]

def daily(school):
    newschool = Counter()
    for k, v in school.items():
        if k == 0:
            newschool[6] += v
            newschool[8] += v
        else:
            newschool[k-1] += v
    return newschool

school = Counter(timers)
for _ in range(80):
    school = daily(school)
part_1 = sum(school.values())
print(part_1)

school = Counter(timers)
for _ in range(256):
    school = daily(school)
part_2 = sum(school.values())
print(part_2)'''