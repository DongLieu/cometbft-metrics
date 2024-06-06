
# from treasure.check_height import *

def read_file(path):
    file = open(path, "r")

    data = file.read().split("\n")

    data = data[:-1]
    for x in range(len(data)):
        data[x] = data[x].split(",")
     
    return data


dirName = "/Users/donglieu/52024/injective/cometbft-metrics/treasure/newblocktimeout-305-timestep"

blocks = read_file(dirName+"/block.csv")
numBlocks = len(blocks)

header = ['numRound', 'numTx', 'blockSizeBytes', 'blockParts', 'blockGossipPartsReceived', 'quorumPrevoteDelay', 'fullPrevoteDelay', 'proposalReceiveCount', 'proposalCreateCount']

counts = [i*float(0) for i in range(len(header))]

for i in blocks:
    counts[0] += float(i[2])
    counts[1] += float(i[4])
    counts[2] += float(i[5])
    counts[3] += float(i[6])
    counts[4] += float(i[7])
    counts[5] += float(i[8])
    counts[6] += float(i[9])

counts = [round(c/numBlocks, 2) for c in counts]


import matplotlib.pyplot as plt
import numpy

figure, axis = plt.subplots()

y_pos = numpy.arange(len(header))

plt.bar(y_pos, counts)
plt.xticks(y_pos, header)

plt.ylabel('float64') 
plt.title('chung')

rects = axis.patches

for rect,labe1 in zip(rects, counts):
	height = rect.get_height()
	axis.text(rect.get_x() + rect.get_width() / 2, height + 0, labe1, ha='center', va='bottom')
	
plt.show()