import json

#bring data in
with open(r'C:\bigfiles\exportedstring.json', "r") as cvrfile:
    cvr = json.loads(cvrfile.read())
print("loaded")

def rl(x):
    return range(len(x))


#check for double-skipped ranks and remove anything after
for i in cvr:
    for j in rl(i):
        if j > 1:
            if i[j-2] == [] and i[j-1] == []:
                i[j] = []

#check for overvotes and remove ties+later
for i in cvr:
    tied = False
    for j in rl(i):
        if len(i[j]) !=1:
            tied = True
        if tied:
            i[j] = []

#strip writeins
for i in cvr:
    for j in rl(i):
        if 214 in i[j]:
            i[j].remove(214)

#sliiiiiiiiiide to the left and remove duplicates
for i in cvr:
    already = []
    originalsize = len(i)
    for j in rl(i):
        if i[j] in already:
            i[j] = []
        else:
            already.append(i[j])
    while [] in i:
        i.remove([])
    while len(i) < originalsize:
        i.append([])

#chop off all but first two since omitting/ranking the worst candidate indicates the same pair preference, and there are 3 candidates
for i in cvr:
    while len(i)>2:
        i.remove(i[2])

permutations = [] # each unique set of pair preferences found once or more
counts = [] # count[x] = how many times permutations[x] is found in cvr

for i in cvr:
    if i not in permutations:
        permutations.append(i)
        counts.append(0)
    for m in rl(permutations):
        if permutations[m] == i:
            counts[m]+=1

sortp = []
sortc = []

c=0
while len(counts) > c:
    print(counts[c]," ",permutations[c])
    c+=1
