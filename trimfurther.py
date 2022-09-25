import json

with open(r'C:\bigfiles\trimmed2.json',"r") as jimmy:
    input = jimmy.read()
input = json.loads(input)

container = []

for i in input:
    vote = [0,0,0,0]
    for j in i.get("Marks"):
        spot = j.get("Rank") - 1
        vote[spot] = j.get("CandidateId")
    container.append(vote)

for m in container:
    for n in m:
        if n == 214:
            m[m.index(n)]=0

for m in container:
    already = [0]
    for n in range(len(m)):
        if m[n] in already:
            m[n] = 0
        else:
            already.append(m[n])


for m in container:
    count=0
    while 0 in m:
        count += 1
        m.remove(0)
    m.extend([0]*count)

for m in container:
    m.remove(m[2])
    m.remove(m[2])
    for n in m:
            if 0 in m:
                m.remove(0)
            else:
                ()


perms = []
tally = []
for m in container:
    if m not in perms:
        perms.append(m)
        tally.append(0)

for a in range(len(perms)):
    for m in container:
        if perms[a] == m:
            tally[a]+=1

for a in range(len(perms)):
    print(str(tally[a]) + " votes of " + str(perms[a]))

with open(r'C:\bigfiles\test3.json', "w") as output:
    for v in container:
        output.write(str(v))
        output.write("\n")

