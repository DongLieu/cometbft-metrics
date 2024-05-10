file = open("/Users/donglieu/52024/injective/cometbft-metrics/test/texttest.txt", "r")

data = file.read().split("\n")

head = data[0].split(",")

subject = head[5:16]

students = data[1:]

students.pop()

for x in range(len(students)):
	students[x] = students[x].split(",")

not_take_exam = [0,0,0,0,0,0,0,0,0,0,0]

for x in students:
	for i in range(5,16):
		if x[i] == "-1":
			not_take_exam[i-5] += 1

not_take_exam_percen = [0,0,0,0,0,0,0,0,0,0,0]
for x in range(0,11):
	not_take_exam_percen[x] = round(not_take_exam[x]*100/len(students),2)


#python3 -m pip install matplotlib
import matplotlib.pyplot as plt
import numpy

figure, axis = plt.subplots()



y_pos = numpy.arange(len(subject))

plt.bar(y_pos, not_take_exam_percen)
plt.xticks(y_pos, subject)

axis.set_ylim(0,100)

plt.ylabel('Phần trăm') 
plt.title('Số học sinh không thi hoặc bỏ thi')

rects = axis.patches

for rect,labe1 in zip(rects, not_take_exam):
	height = rect.get_height()
	axis.text(rect.get_x() + rect.get_width() / 2, height + 5, labe1, ha='center', va='bottom')
	
print(axis)
print(rects)
print(rect.get_x())
print(rect.get_width())
plt.show()