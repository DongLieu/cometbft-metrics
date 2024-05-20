import sys

sys.path.insert(1, '/Users/donglieu/52024/injective/cometbft-metrics/reader/')

from csv_reader import *


pros = eachProposal()
hieght_outime = heightTimeOut()
# print(hieght_outime)
avg_num_blockpast_timeout = 0
avg_blockPartsReceived_timeout = 0
count_timeout = 0
# notimeout
avg_num_blockpast = 0
avg_blockPartsReceived = 0


for pro in pros:
    # print(pro[0])
    if pro[0] in hieght_outime:
        count_timeout += 1
        avg_num_blockpast_timeout += float(pro[3])
        avg_blockPartsReceived_timeout += float(pro[4])
    else:
        avg_num_blockpast += float(pro[3])
        avg_blockPartsReceived +=float(pro[4])


avg_num_blockpast_timeout = avg_num_blockpast_timeout/count_timeout
avg_blockPartsReceived_timeout = avg_blockPartsReceived_timeout/count_timeout

avg_num_blockpast = avg_num_blockpast/(len(pros) - count_timeout)
avg_blockPartsReceived = avg_blockPartsReceived/(len(pros) - count_timeout)

title = ["num_blockpast", "blockPartsReceived"] 

# print(, avg_blockPartsReceived])

import matplotlib.pyplot as plt
import numpy as np

num_subjects = len(title)

indices = np.arange(num_subjects)

width = 0.35

fig, ax = plt.subplots()

rects1 = ax.bar(indices - width/2, [avg_num_blockpast, avg_blockPartsReceived], width, label='no timeout', color='green')

# Vẽ cột thứ hai với màu đỏ
rects2 = ax.bar(indices + width/2, [avg_num_blockpast_timeout, avg_blockPartsReceived_timeout], width, label='timeout', color='red')

# Thêm các nhãn, tiêu đề và chú giải
ax.set_xlabel('obj')
ax.set_ylabel('so luong')
ax.set_title('Biểu đồ xxxx')
ax.set_xticks(indices)
ax.set_xticklabels(title)
ax.legend()

# Hiển thị số điểm trên mỗi cột
ax.bar_label(rects1, padding=3)
ax.bar_label(rects2, padding=3)

# Hiển thị biểu đồ
plt.show()
