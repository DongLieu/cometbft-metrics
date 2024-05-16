import sys

sys.path.insert(1, '/Users/donglieu/52024/injective/cometbft-metrics/reader/')

from csv_reader import *

eachHeight = eachHeight()

for x in range(len(eachHeight)):
    eachHeight[x].append('0')

# titleEachHeight = ['height', 'numRound', 'blockIntervalSeconds','numTx', 'blockSizeBytes', 'blockParts', 'blockGossipPartsReceived', 'quorumPrevoteDelay', 'fullPrevoteDelay', 'proposalReceiveCount', 'proposalCreateCount']

# timeThreshold = 5

title = ['numRound', 'numTx', 'blockSizeBytes', 'blockParts', 'blockGossipPartsReceived', 'quorumPrevoteDelay', 'fullPrevoteDelay', 'proposalReceiveCount', 'proposalCreateCount']
num_Obj = len(title)
blockShort = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
blockLong = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
count_blockLong = 0

for x in eachHeight:
    if float(x[2]) > timeThreshold:
        count_blockLong +=1
        # numRound
        blockLong[0] += float(x[1])
        # numTx
        blockLong[1] += float(x[3])
        # blockSizeBytes
        blockLong[2] += float(x[4])
        # blockParts
        blockLong[3] += float(x[5])
        # blockGossipPartsReceived
        blockLong[4] += float(x[6])
        # quorumPrevoteDelay
        blockLong[5] += float(x[7])
        # fullPrevoteDelay
        blockLong[6] += float(x[8])
        # proposalReceiveCount
        blockLong[7] += float(x[9])
        # proposalCreateCount
        blockLong[8] += float(x[10])
    else:
        # numRound
        blockShort[0] += float(x[1])
        # numTx
        blockShort[1] += float(x[3])
        # blockSizeBytes
        blockShort[2] += float(x[4])
        # blockParts
        blockShort[3] += float(x[5])
        # blockGossipPartsReceived
        blockShort[4] += float(x[6])
        # quorumPrevoteDelay
        blockShort[5] += float(x[7])
        # fullPrevoteDelay
        blockShort[6] += float(x[8])
        # proposalReceiveCount
        blockShort[7] += float(x[9])
        # proposalCreateCount
        blockShort[8] += float(x[10])

blockShortAvg = [round(i/(len(eachHeight)-count_blockLong), 3) for i in blockShort]
blockLongAvg = [round(i/count_blockLong, 3) for i in blockLong]

for i in range(num_Obj):
    if blockShortAvg[i] == 0 or blockLongAvg[i] == 0:continue
    if blockShortAvg[i]>blockLongAvg[i]:
        blockLongAvg[i] = round(blockLongAvg[i]/blockShortAvg[i], 3)*100
        blockShortAvg[i] = 100
    else:
        blockShortAvg[i] = round(blockShortAvg[i]/blockLongAvg[i], 3)*100
        blockLongAvg[i] = 100


import matplotlib.pyplot as plt
import numpy as np

# Tạo các vị trí cho các cột
indices = np.arange(num_Obj)

# Độ rộng của mỗi cột
width = 0.35

# Tạo biểu đồ
fig, ax = plt.subplots()

# Vẽ cột đầu tiên với màu xanh lá cây
rects1 = ax.bar(indices - width/2, blockShortAvg, width, label='block short', color='green')

# Vẽ cột thứ hai với màu đỏ
rects2 = ax.bar(indices + width/2, blockLongAvg, width, label='block long', color='red')

# Thêm các nhãn, tiêu đề và chú giải
ax.set_xlabel('Obj')
ax.set_ylabel('%')
ax.set_title('each hieght')
ax.set_xticks(indices)
ax.set_xticklabels(title)
ax.legend()

# Hiển thị số điểm trên mỗi cột
ax.bar_label(rects1, padding=3)
ax.bar_label(rects2, padding=3)

# Hiển thị biểu đồ
plt.show()
