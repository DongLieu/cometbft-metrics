import sys

sys.path.insert(1, '/Users/donglieu/52024/injective/cometbft-metrics/reader/')

from csv_reader import *


pros = eachVote()
hieght_outime = heightTimeOut()
# print(hieght_outime)
validatorsPower_timeout      = 0
missingValidatorsPowerPrevote_timeout = 0
count_timeout = 0
# notimeout
validatorsPower = 0
missingValidatorsPowerPrevote = 0


for pro in pros:
    # print(pro[0])
    if pro[0] in hieght_outime:
        count_timeout += 1
        validatorsPower_timeout += float(pro[3])
        missingValidatorsPowerPrevote_timeout += float(pro[4])
    else:
        validatorsPower += float(pro[3])
        missingValidatorsPowerPrevote +=float(pro[4])


validatorsPower_timeout = validatorsPower_timeout/count_timeout
missingValidatorsPowerPrevote_timeout = missingValidatorsPowerPrevote_timeout/count_timeout

validatorsPower = validatorsPower/(len(pros) - count_timeout)
missingValidatorsPowerPrevote = missingValidatorsPowerPrevote/(len(pros) - count_timeout)

title = ["validatorsPower", "missingValidatorsPowerPrevote"] 

# print(, missingValidatorsPowerPrevote])

import matplotlib.pyplot as plt
import numpy as np

num_subjects = len(title)

indices = np.arange(num_subjects)

width = 0.35

fig, ax = plt.subplots()

rects1 = ax.bar(indices - width/2, [validatorsPower, missingValidatorsPowerPrevote], width, label='no timeout', color='green')

# Vẽ cột thứ hai với màu đỏ
rects2 = ax.bar(indices + width/2, [validatorsPower_timeout, missingValidatorsPowerPrevote_timeout], width, label='timeout', color='red')

# Thêm các nhãn, tiêu đề và chú giải
ax.set_xlabel('obj')
ax.set_ylabel('so luong Power')
ax.set_title('Biểu đồ xxxx')
ax.set_xticks(indices)
ax.set_xticklabels(title)
ax.legend()

# Hiển thị số điểm trên mỗi cột
ax.bar_label(rects1, padding=3)
ax.bar_label(rects2, padding=3)

# Hiển thị biểu đồ
plt.show()
