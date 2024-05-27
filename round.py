from check_height import *

heightTimeOuts = heightTimeOut()


# onlytime
timesteps  = read_file("/Users/donglieu/52024/injective/cometbft-metrics/treasure/gen/blockOnlyTimeStep.csv")

typeStep = []
timeStep = {}

for x in timesteps:
    for y in heightTimeOuts:
        if x[0] == y:
            if x[2] in typeStep:
                timeStep[x[2]] += float(x[3])
            else:
                typeStep.append(x[2])
                timeStep[x[2]] = float(x[3])
print(typeStep)
print(timeStep)


values = [ i/len(heightTimeOuts) for i in timeStep.values()]

import matplotlib.pyplot as plt
import numpy

figure, axis = plt.subplots()

y_pos = numpy.arange(len(typeStep))

plt.bar(y_pos, values)
plt.xticks(y_pos, typeStep)

# axis.set_ylim(0,3)

plt.ylabel('giây') 
plt.title('thời gian trung bình của các block bị timeout')

rects = axis.patches

for rect,labe1 in zip(rects, values):
	height = rect.get_height()
	axis.text(rect.get_x() + rect.get_width() / 2, height + 0, labe1, ha='center', va='bottom')
	
plt.show()