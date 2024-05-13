import sys

sys.path.insert(1, '/Users/donglieu/52024/injective/cometbft-metrics/reader/')

from csv_reader import *


eachTime = eachTimeStep()

titleRoundStep = ['NewHeight', 'NewRound', 'Propose', 'Prevote', 'PrevoteWait', 'Precommit', 'PrecommitWait', 'Commit']

listTimeAvg = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]

count = 0
for x in eachTime:
    count +=1
    for i in range(len(titleRoundStep)):
        if x[2] == titleRoundStep[i]:
            listTimeAvg[i] += float(x[3])

listTimeAvgs = [round(i/count, 3) for i in listTimeAvg]

#python3 -m pip install matplotlib column chart
import matplotlib.pyplot as plt
import numpy

figure, axis = plt.subplots()

y_pos = numpy.arange(len(titleRoundStep))

plt.bar(y_pos, listTimeAvgs)
plt.xticks(y_pos, titleRoundStep)

axis.set_ylim(0,5)

plt.ylabel('second') 
plt.title('trung bình thời gian của một block khi bị timeout')

rects = axis.patches

for rect,labe1 in zip(rects, listTimeAvgs):
	height = rect.get_height()
	axis.text(rect.get_x() + rect.get_width() / 2, height , labe1, ha='center', va='bottom')
	
plt.show()