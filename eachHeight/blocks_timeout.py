import sys

sys.path.insert(1, '/Users/donglieu/52024/injective/cometbft-metrics/reader/')

from csv_reader import *

eachHeight = eachHeight()

# titleEachHeight = ['height', 'numRound', 'blockIntervalSeconds','numTx', 'blockSizeBytes', 'blockParts', 'blockGossipPartsReceived', 'quorumPrevoteDelay', 'fullPrevoteDelay', 'proposalReceiveCount', 'proposalCreateCount']

# timeThreshold = 5

title = ['numRound', 'numTx', 'blockSizeBytes', 'blockParts', 'blockGossipPartsReceived', 'quorumPrevoteDelay', 'fullPrevoteDelay', 'proposalReceiveCount', 'proposalCreateCount']
maxx = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]

num_Obj = len(title)
datas = {}
count_blockLong = 0

for x in eachHeight:
    if float(x[2]) > timeThreshold:
        count_blockLong +=1
        data = [float(x[1])]
        for i in x[3:]:
            data.append(float(i))

        for i in range(len(data)):
            if maxx[i] < data[i]:
                maxx[i] = data[i]
        
        datas[str(count_blockLong)] = data

for i,j in datas.items():
    print(j)
print()
print(maxx)
print()
import matplotlib.pyplot as plt


for i in range(len(maxx)):
    for key, values in datas.items():
        if maxx[i] != 0:
            values[i] = 100*values[i]/maxx[i]
            datas[key] = values


for i,j in datas.items():
    print(j)
print()

# Tạo biểu đồ
plt.figure(figsize=(10, 6))
for key, values in datas.items():
    plt.plot(title, values, marker='o', label=key)


# Tùy chỉnh biểu đồ
plt.title('Biểu đồ đường cho {} đối tượng'.format(count_blockLong))
plt.xlabel('information field')
plt.ylabel('point')
plt.legend()
plt.grid(True)

# Hiển thị biểu đồ
plt.show()
