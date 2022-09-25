import json

#bring data in
with open(r'C:\bigfiles\CvrExport.json', "r") as cvrfile:
    fullcvr = json.loads(cvrfile.read())
print("loaded")
#     cvrstr = cvrfile.read()
# fullcvr = json.loads(cvrstr)
# del cvrstr

#make empty array to receive data about the special general, strip the rest
receiver = []
for i in fullcvr.get("Sessions"):
    for j in i.get("Original").get("Cards"):
        for k in j.get("Contests"):
            if k.get("Id") == 69:
                receiver.append(k)
print("trimmed")
del fullcvr
print("cleared")
container = []
for i in receiver:
    ballot = [[],[],[],[]]
    for mark in i.get("Marks"):
        ballot[mark.get("Rank")-1].append(mark.get("CandidateId"))
    container.append(ballot)
print("matrixified")
with open (r'C:\bigfiles\exportedstring.json',"w") as dump:
    dump.write(json.dumps(container))