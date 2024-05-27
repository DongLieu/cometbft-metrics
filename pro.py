from check_height import *

heightTimeOuts = heightTimeOut()
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
            if x[2] in stepName:
                if x[3] != 0:
                    numblockParts[x[2]] += float(x[3])
                else:
                    numblockParts[x[2]] += float(y[5])
                blockPartsReceived[x[2]] += float(x[4])
            else:
                stepName.append(x[2])
                if x[3] != 0:
                    numblockParts[x[2]] = float(x[3])
                else:
                    numblockParts[x[2]] = float(y[5])
                blockPartsReceived[x[2]] = float(x[4])


valu1 = [i/len(heightTimeOuts) for i in numblockParts.values()]
valu2 = [i/len(heightTimeOuts) for i in blockPartsReceived.values()]

import matplotlib.pyplot as plt
import numpy as np

# Số lượng môn học
num_subjects = len(stepName)

# Tạo các vị trí cho các cột
indices = np.arange(num_subjects)

# Độ rộng của mỗi cột
width = 0.35

# Tạo biểu đồ
fig, ax = plt.subplots()

# Vẽ cột đầu tiên với màu xanh lá cây
rects1 = ax.bar(indices - width/2, valu1, width, label='numblockParts', color='green')

# Vẽ cột thứ hai với màu đỏ
rects2 = ax.bar(indices + width/2, valu2, width, label='blockPartsReceived', color='red')

# Thêm các nhãn, tiêu đề và chú giải
ax.set_xticks(indices)
ax.set_xticklabels(stepName)
ax.legend()

# Hiển thị số điểm trên mỗi cột
ax.bar_label(rects1, padding=3)
ax.bar_label(rects2, padding=3)

# Hiển thị biểu đồ
plt.show()
