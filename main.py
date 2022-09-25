import json

#bring data in
with open(r'C:\bigfiles\CvrExport.json', "r") as cvrfile:
    cvrstr = cvrfile.read()
fullcvr = json.loads(cvrstr)

#make empty array to receive data about the special general, strip the rest
receiver = []
for i in fullcvr.get("Sessions"):
    for j in i.get("Original").get("Cards"):
        for k in j.get("Contests"):
            if k.get("Id") == 69:
                receiver.append(k)

#if a candidate is already given an early rank, strip the candidate from later ranks
grandtotal = len(receiver)
for i in receiver:
    for m in i.get("Marks"):
        for n in i.get("Marks"):
            if m.get("CandidateId") == n.get("CandidateId"):
                if m.get("Rank") < n.get("Rank"):
                        i.get("Marks").remove(n)

#special receiver and count, for items in main receiver with overvotes
overvotes = 0
ovreceiver = []

container = []
for i in receiver:
    vote = [0,0,0,0]
    filled = [0,0,0,0]
    for j in i.get("Marks"):
        spot = j.get("Rank") - 1
        if j.get("CandidateId") != 214:
            vote[spot] = j.get("CandidateId")
            filled[spot] += 1
    if 2 not in filled:
        container.append(vote)
    else:
        overvotes += 1
        ovreceiver.append(i)

ovcontainer = []

for i in ovreceiver:
    ovote = [[],[],[],[]]
    for mark in i.get("Marks"):
        rank = mark.get("Rank") - 1
        if mark.get("CandidateId") != 214:
            ovote[rank].append(mark.get("CandidateId"))
    ovcontainer.append(ovote)

missedwriteins=0
for m in container:
    for n in m:
        if n == 214:
            m[m.index(n)]=0
            missedwriteins+=1
print(missedwriteins," write-ins escaped sweep")

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

#overvote info
operms = []
otally = []

#pick one block to uncomment

#raw totals
# for m in ovcontainer:
#     if m not in operms:
#         operms.append(m)
#         otally.append(0)

#where did people place their overvotes in a "if it were cardinal" sense
# for m in ovcontainer:
#     for n in range(len(m)):
#         m[n]=len(m[n])
#     if m not in operms:
#         operms.append(m)
#         otally.append(0)

#strip empty arrays to push everything to the front of the line
for m in ovcontainer:
    for n in range(len(m)):
        m.remove([]) if [] in m else ()
    for n in range(len(m)):
        if len(m[n]) != 1:
            m[n] = "other"

    if m not in operms:
        if len(m) > 1 or "other" in m:
            operms.append(m)
            otally.append(0)

#end pick one

for a in range(len(operms)):
    for m in ovcontainer:
        if operms[a] == m:
            otally[a]+=1


votes = sum([sum(otally),sum(tally)])

#printout
print("---totals---")
print(grandtotal," total votes")
print(votes)
print(sum(tally)," normal votes")
print(overvotes," overvotes")
print(sum(otally))
print("---preferences from standard votes---")
for a in range(len(perms)):
    print(str(tally[a]) + " votes of " + str(perms[a]))
print("---recovered preferences from overvotes---")
for a in range(len(operms)):
    print(str(otally[a]) + " votes of " + str(operms[a]))
