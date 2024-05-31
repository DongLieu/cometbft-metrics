from treasure.check_height import *

heightTimeOuts = heightsTimeOut("/Users/donglieu/52024/injective/cometbft-metrics/treasure/gen/block.csv")
hi = []

# onlytime
timesteps  = read_file("/Users/donglieu/52024/injective/cometbft-metrics/treasure/gen/blockProposalStep.csv")

heights  = read_file("/Users/donglieu/52024/injective/cometbft-metrics/treasure/gen/block.csv")

a =[]
for i in heightTimeOuts:
    for j in heights:
        if i == j[0]:
            a.append(j)

stepName = []
numblockParts = {}
blockPartsReceived = {}

for x in timesteps:
    for y in a:
        if x[0] == y[0]:
            if x[3] in stepName:
                if x[3] != 0:
                    numblockParts[x[3]] += float(x[3])
                else:
                    numblockParts[x[3]] += float(y[5])
                blockPartsReceived[x[3]] += float(x[4])
            else:
                stepName.append(x[3])
                if x[3] != 0:
                    numblockParts[x[3]] = float(x[3])
                else:
                    numblockParts[x[3]] = float(y[5])
                blockPartsReceived[x[3]] = float(x[4])


valu1 = [i/len(heightTimeOuts) for i in numblockParts.values()]
valu2 = [i/len(heightTimeOuts) for i in blockPartsReceived.values()]

import matplotlib.pyplot as plt
import numpy as np

num_subjects = len(stepName)

indices = np.arange(num_subjects)

width = 0.35

fig, ax = plt.subplots()

rects1 = ax.bar(indices - width/2, valu1, width, label='numblockParts', color='green')

rects2 = ax.bar(indices + width/2, valu2, width, label='blockPartsReceived', color='red')

ax.set_xticks(indices)
ax.set_xticklabels(stepName)
ax.legend()

ax.bar_label(rects1, padding=3)
ax.bar_label(rects2, padding=3)

plt.show()
