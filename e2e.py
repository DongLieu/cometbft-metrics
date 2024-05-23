def eachHeight():
    file_path = '/Users/donglieu/52024/injective/cometbft-metrics/treasure/block.csv'

    return read_file(file_path)

def eachTime():
    file_path = '/Users/donglieu/52024/injective/cometbft-metrics/old_data/data1/data/blockOnlyTimeStep.csv'

    return read_file(file_path)


def eachPro():
    file_path = '/Users/donglieu/52024/injective/cometbft-metrics/old_data/data1/data/blockProposalStep.csv'

    return read_file(file_path)

def eachVote():
    file_path = '/Users/donglieu/52024/injective/cometbft-metrics/old_data/data1/data/blockVoteStep.csv'

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
    eachVotes = eachVote()
    height_timeout = []

    for x in eachHeigh:
        for y in eachVotes:
            if y[0] == x[0]:
                write_file("/Users/donglieu/52024/injective/cometbft-metrics/ttt.csv", y)
            

        # write_file("/Users/donglieu/52024/injective/cometbft-metrics/ttt.csv", x)

        

    return height_timeout


heightTimeOut()