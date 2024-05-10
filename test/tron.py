file = open("/Users/donglieu/52024/injective/cometbft-metrics/test/texttest.txt", "r")

data = file.read().split("\n")

head = data[0].split(",")

subject = head[5:16]

students = data[1:]

students.pop()

for x in range(len(students)):
	students[x] = students[x].split(",")

danh_sach_hoc_sinh_thi_i_mon = [0,0,0,0,0,0,0,0,0,0,0,0]
for x in students:
	dem = 11
	for i in range(5,16):
		if x[i] == "-1":
			dem -= 1
	danh_sach_hoc_sinh_thi_i_mon[dem] +=1

# print(danh_sach_hoc_sinh_thi_i_mon)
import matplotlib.pyplot as plt

# Pie chart, where the slices will be ordered and plotted counter-clockwise:
labels = '0 môn', '1 môn', '2  môn', '3 môn','4 môn', '5 môn', '6 môn', '7 môn', '8 môn', '9 môn','10 môn', '11 môn'
sizes = danh_sach_hoc_sinh_thi_i_mon
# explode = (0, 0.1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')

fig1, ax1 = plt.subplots()
ax1.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.show()