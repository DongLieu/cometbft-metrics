def read_file(path):
    file = open(path, "r")

    data = file.read().split("\n")

    data = data[:-1]
    for x in range(len(data)):
        data[x] = data[x].split(",")
     
    return data


# onlytime
timesteps  = read_file("/Users/donglieu/52024/injective/cometbft-metrics/treasure/newblocktimeout-305-timestep/time.csv")
blocks  = read_file("/Users/donglieu/52024/injective/cometbft-metrics/treasure/newblocktimeout-305-timestep/block.csv")

typeStep = []
timeStep = {}

for x in timesteps:
    if x[3] in typeStep:
        timeStep[x[3]] += float(x[4])
    else:
        typeStep.append(x[3])
        timeStep[x[3]] = float(x[4])

print(typeStep)
print(timeStep)


values = [ round(i/len(blocks),2) for i in timeStep.values()]

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

# import matplotlib.pyplot as plt


# fig1, ax1 = plt.subplots()
# ax1.pie(timeStep.values(), labels=timeStep.keys(), autopct='%1.1f%%', startangle=90)
# ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

# plt.show()

