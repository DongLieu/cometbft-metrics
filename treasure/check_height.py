from csv_reader import *

def heightsTimeOut(file_path):
    eachHeigh = read_file(file_path + "/block.csv")
    heightimeouts = []
    max = 0
    hightContinue = []
    for x in eachHeigh:
        # print(x)
        if x[0] == "0":
            hightContinue.append(x[0])
            continue
        if x[-1] == "0" and x[-2] == "0" and x[-3] == "0" and x[-4] == "0":
            hightContinue.append(x[0])
            continue
        if float(x[3]) > max:
            max = float(x[3])

        # if float(x[2]) > 3 and float(x[2]) < 5:
        # if float(x[3]) > 4 and float(x[3]) <= 4.5:
        if float(x[3]) > 5:
            heightimeouts.append(x[0])

    times = read_file(file_path + "/blockOnlyTimeStep.csv")
    top = "0"
    sum = float(0)
    for i in times:
        if i[0] in heightimeouts or i[0] in hightContinue:
            continue
        if top == i[0]:
            sum += float(i[4])
        else:
            if sum > 5:
                heightimeouts.append(top)
            top = i[0]
            sum = float(i[4])

    print(max)
    return heightimeouts


print(heightsTimeOut("/Users/donglieu/52024/injective/cometbft-metrics/old_data/data7/cometbft-metrics"))