
values = [1, 2, 3, 4, 5]
typeStep = ["m1", "m2", "m3", "m4", "m5"]

import matplotlib.pyplot as plt


fig1, ax1 = plt.subplots()
ax1.pie(values, labels=typeStep, autopct='%1.1f%%', startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.show()