import csv
import os

def write_file(path_file, data):
    os.makedirs(os.path.dirname(path_file), exist_ok=True)
    with open(path_file, 'a', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(data)


def read_file(path, toPath):
    file = open(path, "r")

    data = file.read().split("\n")

    data = data[:-1]
    for x in range(len(data)):
        data[x] = data[x].split(",")
     
    for i in data:
        if float(i[1]) <2 and float(i[0]) >4:
            continue
        write_file(toPath, i)

read_file("/Users/donglieu/62024/injective/cometbft-metrics/old_data/data12/cometbft-metrics/train/train.csv", "/Users/donglieu/62024/injective/cometbft-metrics/old_data/data12/cometbft-metrics/train/train2.csv")