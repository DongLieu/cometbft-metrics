from csv_reader import *

def heightsTimeOut(file_path):
    eachHeigh = read_file(file_path + "/block.csv")
    heightimeouts = []
    xs = {}
    maxTime = 0
    hightContinue = []
    for x in eachHeigh:
        # print(x)
        if x[0] == "0":
            hightContinue.append(x[0])
            continue
        if x[-1] == "0" and x[-2] == "0" and x[-3] == "0" and x[-4] == "0":
            hightContinue.append(x[0])
            continue
        # if float(x[3]) > max:
        #     max = float(x[3])

        if float(x[3]) > 5:
            heightimeouts.append(x[0])
            xs[x[0]] = float(x[3])

    times = read_file(file_path + "/blockOnlyTimeStep.csv")
    top = "0"
    # sum = float(0)
    for i in times:
        if i[0] in heightimeouts:
           if i[3] == "NewHeight" or i[3] == "Commit":
            if float(i[4]) > 0.8 * xs[i[0]]:
                # print(i[0])
                heightimeouts.remove(i[0])
                hightContinue.append(i[0])
            # else:
            #     print(i, 0.7 * xs[i[0]])

    for i in heightimeouts:
        if maxTime < xs[i]:
            maxTime = xs[i]

    return maxTime, heightimeouts, hightContinue, xs

