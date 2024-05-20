import sys

sys.path.insert(1, '/Users/donglieu/52024/injective/cometbft-metrics/reader/')

from csv_reader import *

# Dự đoán do size Msg
p2ps = eachP2P()
hieght_outime = heightTimeOut()

avg_size_timout = 0
avg_size = 0
count_timeout = 0

for p2p in p2ps:
    # print(pro[0])
    if p2p[0] in hieght_outime:
        count_timeout += 1
        avg_size_timout += float(p2p[7])
    else:
        avg_size += float(p2p[7])

if count_timeout == 0:
    avg_size = avg_size/len(p2ps)
    avg_size_timout = 0
else:
    avg_size = round(avg_size/(len(p2ps) - count_timeout), 2)
    avg_size_timout = round(avg_size_timout/count_timeout, 2)

title = ["no timout ", "timeout"] 

import matplotlib.pyplot as plt
import numpy

figure, axis = plt.subplots()

y_pos = numpy.arange(len(title))

plt.bar(y_pos, [avg_size, avg_size_timout])
plt.xticks(y_pos, title)

plt.ylabel('size avg') 
plt.title('Bieeur do xxx')

rects = axis.patches

rects = axis.patches
for rect, label in zip(rects, [avg_size, avg_size_timout]):
    height = rect.get_height()
    axis.text(
        rect.get_x() + rect.get_width() / 2, height, label,
        ha='center', va='bottom'
    )

plt.show()