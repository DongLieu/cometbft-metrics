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

import matplotlib.pyplot as plt

fig1, ax1 = plt.subplots()
ax1.pie(listTimeAvg, labels=titleRoundStep, autopct='%1.1f%%', startangle=90)
ax1.axis('equal')  

plt.show()