import json

def kInTypes(k: float):
    if k < (min_val+avg_val)/2:
        return 1
    if k >= (min_val+avg_val)/2 and k < avg_val:
        return 2
    if k >= avg_val and k < (max_val+avg_val)/2:
        return 3
    if k >= (max_val+avg_val)/2:
        return 4

def read_file(path):
    file = open(path, "r")

    data = file.read().split("\n")

    data = data[:-1]
    for x in range(len(data)):
        data[x] = data[x].split(",")
     
    return data

def ReadIfNotAxist():
    with open("/Users/donglieu/52024/injective/cometbft-metrics/treasure/newblocktimeout-305-timestep/cacheNumByte.txt", "r") as file:
        counts_try = file.read()

    data = json.loads(counts_try)
    if counts_try != "":
        return data

    eachHeigh = read_file("/Users/donglieu/52024/injective/cometbft-metrics/treasure/newblocktimeout-305-true/blockP2P.csv")
    types = []
    counts = {}
    for x in eachHeigh:
        if x[8] in types:
            counts[x[8]] += 1
        else:
            if x[8] == "0": print(x)
            types.append(x[8])
            counts[x[8]] = 1
    json_counts = json.dumps(counts)
    with open("/Users/donglieu/52024/injective/cometbft-metrics/treasure/newblocktimeout-305-timestep/cacheNumByte.txt", "w") as file:
        file.write(json_counts)
    return counts


counts = ReadIfNotAxist()
max_val = 0
min_val = 999999
mn = 0
for c in counts.keys():
    mn+=1
    if float(c) < min_val:
        min_val = float(c)
    
    if float(c) > max_val:
        max_val = float(c)

sizes = 0
for v, k in counts.items():
    sizes += float(v)*float(k)

print(sizes/882368)

avg_val = round(sizes/882368,2)


numCol=5
col = [min, (min_val+avg_val)/2, avg_val, (max_val+avg_val)/2, max_val]
c = {}
typess = []

for k,v in counts.items():
    types =  kInTypes(float(k))
    if types in typess:
        c[types] +=v
    else:
        typess.append(types)
        c[types] = v


tital = [
    str(min_val) + "->" + str((min_val + avg_val) / 2),
    str((min_val + avg_val) / 2) + "->" + str(avg_val),
    str(avg_val) + "->" + str((max_val + avg_val) / 2),
    str((max_val + avg_val) / 2) + "->" + str(max_val)
]
print(c)

import matplotlib.pyplot as plt
import numpy

figure, axis = plt.subplots()

y_pos = numpy.arange(len(tital))

plt.bar(y_pos, c.values())
plt.xticks(y_pos, tital)

# axis.set_ylim(0,3)

plt.ylabel('size') 
plt.title('số lượng msg theo size')

rects = axis.patches

for rect,labe1 in zip(rects, c.values()):
	height = rect.get_height()
	axis.text(rect.get_x() + rect.get_width() / 2, height + 0, labe1, ha='center', va='bottom')
	
plt.show()