
values = [1, 2, 3, 4, 5]
typeStep = ["m1", "m2", "m3", "m4", "m5"]


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
