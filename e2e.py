def eachHeight():
    file_path = '/Users/donglieu/52024/injective/cometbft-metrics/old_data/data1/data/block.csv'

    return read_file(file_path)

def eachTime():
    file_path = '/Users/donglieu/52024/injective/cometbft-metrics/old_data/data5/blockOnlyTimeStep.csv'

    return read_file(file_path)


def read_file(path):
    file = open(path, "r")

    data = file.read().split("\n")

    data = data[:-1]
    for x in range(len(data)):
        data[x] = data[x].split(",")
     
    return data

import csv

def write_file(path_file, data):
    # data = [70917290, 1, 0.408425436, 4, 9948, 2048, 5, 0.05217152, 0.269370465, 1, 0]
    # for data in datas:
    with open(path_file, 'a', newline='') as csvfile:
        # Tạo writer object
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(data)


def heightTimeOut():
    eachHeigh = eachHeight()
    eachTimes = eachTime()
    height_timeout = []
    max = 0
    for x in eachHeigh:
        if x[-1] == "0" and x[-2] == "0" and x[-3] == "0" and x[-4] == "0":
            continue

        if float(x[2]) > max:
            max = float(x[2])

        if float(x[2]) > 2.7:
            height_timeout.append(x[0])

        write_file("/Users/donglieu/52024/injective/cometbft-metrics/ttt.csv", x)

        
    print(max)
    return height_timeout



print(heightTimeOut())