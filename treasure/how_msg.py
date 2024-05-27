def eachP2P():
    file_path = '/Users/donglieu/52024/injective/cometbft-metrics/treasure/blockP2P1.csv'

    return read_file(file_path)

def read_file(path):
    file = open(path, "r")

    data = file.read().split("\n")

    data = data[:-1]
    for x in range(len(data)):
        data[x] = data[x].split(",")
     
    return data


eachHeigh = eachP2P()
x_from = 0
receive = 0
types = []
counts = {}
for x in eachHeigh:
    if x[3] == "":
        x_from +=1
    if x[6] in types:
        counts[x[6]] += 1
    else:
        counts[x[6]] = 1
        types.append(x[6])

receive = len(eachHeigh)-x_from
print("send",x_from)
print("receive", receive)
print(types)
print(counts)
                
import matplotlib.pyplot as plt


fig1, ax1 = plt.subplots()
ax1.pie(counts.values(), labels=counts.keys(), autopct='%1.1f%%', startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.show()


