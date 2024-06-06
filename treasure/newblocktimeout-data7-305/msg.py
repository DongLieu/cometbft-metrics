
def read_file(path):
    file = open(path, "r")

    data = file.read().split("\n")

    data = data[:-1]
    for x in range(len(data)):
        data[x] = data[x].split(",")
     
    return data


eachHeigh = read_file("/Users/donglieu/52024/injective/cometbft-metrics/treasure/newblocktimeout-305-true/blockP2P.csv")
x_from = 0
receive = 0
types = []
counts = {}
for x in eachHeigh:
    if x[4] == "":
        x_from +=1
    if x[7] in types:
        counts[x[7]] += 1
    else:
        counts[x[7]] = 1
        types.append(x[7])

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


