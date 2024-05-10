file = open("/Users/donglieu/52024/injective/cometbft-metrics/test/texttest.txt", "r")

data = file.read().split("\n")

head = data[0].split(",")

subject = head[5:16]

students = data[1:]

students.pop()

for x in range(len(students)):
	students[x] = students[x].split(",")

ten_khoi = ["Khoi_A", "Khoi_A1","Khoi_B","Khoi_D","Khoi_C"]

diem_tb_theo_khoi = [0,0,0,0,0]

cout_diem_tb_theo_khoi = [0,0,0,0,0]

#5-toam,6-van,9-lichsu,10địa lí,11gdcd,12sinh học,13vật lí,14hóa học,15tiếng anh,

for student in students:
		#khoi A
	if student[5] != "-1" and student[13] != "-1" and student[14] != "-1":
		cout_diem_tb_theo_khoi[0] += 1
		diem_tb_theo_khoi[0] += float(student[5]) + float(student[13]) + float(student[14])
		#khoi A1
	if student[5] != "-1" and student[13] != "-1" and student[15] != "-1":
		cout_diem_tb_theo_khoi[1] += 1
		diem_tb_theo_khoi[1] += float(student[5]) + float(student[13]) + float(student[15])
		#khoi B
	if student[5] != "-1" and student[12] != "-1" and student[14] != "-1":
		cout_diem_tb_theo_khoi[2] += 1
		diem_tb_theo_khoi[2] += float(student[5]) + float(student[12]) + float(student[14])
		#khoi D
	if student[5] != "-1" and student[6] != "-1" and student[15] != "-1":
		cout_diem_tb_theo_khoi[3] += 1
		diem_tb_theo_khoi[3] += float(student[5]) + float(student[6]) + float(student[15])
		#Khoi C
	if student[6] != "-1" and student[9] != "-1" and student[10] != "-1":
		cout_diem_tb_theo_khoi[4] += 1
		diem_tb_theo_khoi[4] += float(student[6]) + float(student[9]) + float(student[10])
	
	
for i in range(len(cout_diem_tb_theo_khoi)):
	diem_tb_theo_khoi[i] = round(diem_tb_theo_khoi[i] / cout_diem_tb_theo_khoi[i],2)
	
print(diem_tb_theo_khoi)
print(cout_diem_tb_theo_khoi)

import matplotlib.pyplot as plt
import numpy

figure, axis = plt.subplots()



y_pos = numpy.arange(len(ten_khoi))

plt.bar(y_pos, diem_tb_theo_khoi)
plt.xticks(y_pos, ten_khoi)

axis.set_ylim(0,30)

plt.ylabel('Điểm 3 môn theo khối') 
plt.title('Điểm trung bình theo khối')

rects = axis.patches

for rect,labe1 in zip(rects, diem_tb_theo_khoi):
	height = rect.get_height()
	axis.text(rect.get_x() + rect.get_width() / 2, height + 0, labe1, ha='center', va='bottom')
	
# print(axis)
# print(rects)
# print(rect.get_x())
# print(rect.get_width())
plt.show()